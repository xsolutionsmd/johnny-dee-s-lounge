#!/usr/bin/env python3
"""Verify the four public documents directly, including an uncached reload."""
import argparse
import json
import re
from urllib.request import Request, urlopen

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("base")
parser.add_argument("--revision")
args = parser.parse_args()
base = args.base.rstrip("/")
routes = ("/", "/menu/", "/catering/", "/visit/")
report = {"base": base, "pages": []}
mains = set()
for route in routes:
    row = {"route": route, "statuses": []}
    for refresh in (False, True):
        request = Request(base + route, headers={"Cache-Control": "no-cache"} if refresh else {})
        with urlopen(request, timeout=20) as response:
            html = response.read().decode("utf-8")
            row["statuses"].append(response.status)
            assert response.status == 200, f"{route}: not HTTP 200"
            assert "noindex" in response.headers.get("X-Robots-Tag", ""), f"{route}: noindex header missing"
            assert "xs-stage" not in html, f"{route}: placeholder remains"
            assert re.search(r'<meta[^>]+name=[\"\']robots[\"\'][^>]+noindex', html, re.I), f"{route}: noindex meta missing"
            main = re.search(r"<main\b[^>]*>(.*?)</main>", html, re.S | re.I)
            assert main, f"{route}: main missing"
            h1 = re.findall(r"<h1\b[^>]*>(.*?)</h1>", html, re.S | re.I)
            assert len(h1) == 1, f"{route}: expected one h1"
            row["heading"] = re.sub(r"<[^>]+>", " ", h1[0]).strip()
            if not refresh:
                mains.add(main.group(1))
    report["pages"].append(row)
assert len(mains) == len(routes), "Routes duplicate main content"
with urlopen(base + "/version.json", timeout=20) as response:
    report["revision"] = json.load(response)["revision"]
    assert "no-store" in response.headers.get("Cache-Control", ""), "Revision is cacheable"
if args.revision:
    assert report["revision"] == args.revision, "Live source revision mismatch"
report["passed"] = True
print(json.dumps(report, indent=2))
