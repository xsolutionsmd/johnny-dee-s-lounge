// Progressive enhancement: native page links remain usable without JavaScript.
document.documentElement.classList.add('has-js');
const toggle = document.querySelector('.nav-toggle');
const nav = document.getElementById('site-nav');
const close = document.querySelector('.nav-close');
const backdrop = document.querySelector('.nav-backdrop');
const wide = matchMedia('(min-width: 861px)');
const outside = [...document.querySelectorAll('main, footer, .header-inner > :not(nav)')];
if (toggle && nav) {
  function setOpen(open, restore = false) {
    toggle.setAttribute('aria-expanded', String(open));
    document.documentElement.classList.toggle('nav-open', open);
    nav.classList.toggle('is-open', open);
    nav.inert = !wide.matches && !open;
    outside.forEach(el => { el.inert = open; });
    if (open) {
      nav.setAttribute('role', 'dialog'); nav.setAttribute('aria-modal', 'true');
      // Wait for the open visibility style before moving keyboard focus.
      requestAnimationFrame(() => {
        if (nav.classList.contains('is-open')) close?.focus({ preventScroll: true });
      });
    } else {
      nav.removeAttribute('role'); nav.removeAttribute('aria-modal');
      if (restore) toggle.focus({ preventScroll: true });
    }
  }
  toggle.addEventListener('click', () => setOpen(true));
  close?.addEventListener('click', () => setOpen(false, true));
  backdrop?.addEventListener('click', () => setOpen(false, true));
  document.addEventListener('keydown', event => {
    if (!nav.classList.contains('is-open')) return;
    if (event.key === 'Escape') { event.preventDefault(); setOpen(false, true); }
    if (event.key === 'Tab') {
      const targets = [...nav.querySelectorAll('a, button')].filter(el => el.getBoundingClientRect().width);
      const first = targets[0], last = targets.at(-1);
      if (event.shiftKey && document.activeElement === first) { event.preventDefault(); last.focus(); }
      else if (!event.shiftKey && document.activeElement === last) { event.preventDefault(); first.focus(); }
    }
  });
  wide.addEventListener('change', () => setOpen(false));
  window.addEventListener('pageshow', () => setOpen(false));
  setOpen(false);
}
