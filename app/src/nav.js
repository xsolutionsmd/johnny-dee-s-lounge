// Mobile navigation disclosure. Without JavaScript the links stay visible as a wrapped row.
document.documentElement.classList.add('has-js');

const toggle = document.querySelector('.nav-toggle');
const nav = document.getElementById('site-nav');

if (toggle && nav) {
  const setOpen = open => {
    toggle.setAttribute('aria-expanded', String(open));
    toggle.setAttribute('aria-label', open ? 'Close navigation' : 'Open navigation');
    nav.classList.toggle('is-open', open);
  };
  setOpen(false);
  toggle.addEventListener('click', () => setOpen(toggle.getAttribute('aria-expanded') !== 'true'));
  document.addEventListener('keydown', event => {
    if (event.key === 'Escape' && toggle.getAttribute('aria-expanded') === 'true') {
      setOpen(false);
      toggle.focus();
    }
  });
  const wide = window.matchMedia('(min-width: 861px)');
  wide.addEventListener('change', event => { if (event.matches) setOpen(false); });
  // Pages restored from the back/forward cache should not reopen with a stale panel.
  window.addEventListener('pageshow', event => { if (event.persisted) setOpen(false); });
}
