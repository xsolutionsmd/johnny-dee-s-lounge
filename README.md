# Johnny Dee's Lounge

A four-page restaurant website: Home, Menu, Catering & Events, and Visit & Contact. Each primary navigation destination is a distinct HTML document and URL. Public business facts and source limitations are in [kb](kb/INDEX.md).

## Development

From `app/`, run `npm ci`, then `npm run dev`. Run `npm run check` for a production build and static contract checks, including all four documents, distinct content, page navigation and local resources. The repository launchers provide container-based development as well.

The container listens on port 8080, serves `/health`, and reports its exact source revision at `/version.json`. It runs read-only and has no application database, credentials or submission endpoint. Phone, directions and the business Facebook profile are ordinary external links. All environments remain noindex.

## Releases

- `main`: production at https://johnny-dee-s-lounge.xsolutionsmd.com
- `derek-dev`: https://johnny-dee-s-lounge-derek-dev.xsolutionsmd.com
- `abdul-dev`: https://johnny-dee-s-lounge-abdul-dev.xsolutionsmd.com

Each preview branch publishes only its own environment. Production changes require an authorized pull request into `main`. See [Oracle operations](docs/ORACLE_DEPLOYMENT.md) and [handoff](kb/HANDOFF.md) for actual verified deployment state.

Verify all routes on a running environment with `python scripts/verify-pages.py https://HOST --revision COMMIT`. This checks direct page loads and uncached reloads, distinct main content, noindex headers and exact revision.

Current content gaps: owner-confirmed full menu/prices, daily hours, catering terms and photography reuse permission. No ordering, reservation or form delivery is represented as connected.
