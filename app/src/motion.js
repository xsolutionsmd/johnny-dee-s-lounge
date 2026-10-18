const reduced = matchMedia('(prefers-reduced-motion: reduce)');
const reveals = [...document.querySelectorAll('[data-reveal]')];
let observer;
if (!reduced.matches && 'IntersectionObserver' in window) {
  observer = new IntersectionObserver(entries => {
    entries.forEach(({target, isIntersecting}) => {
      if (!isIntersecting) return;
      target.classList.add('is-visible');
      observer.unobserve(target);
    });
  }, {threshold: .08, rootMargin: '0px 0px -24px 0px'});
  reveals.forEach(el => { el.classList.add('reveal-ready'); observer.observe(el); });
}
reduced.addEventListener('change', event => {
  if (event.matches) { observer?.disconnect(); reveals.forEach(el => el.classList.add('is-visible')); }
});
window.addEventListener('pageshow', event => {
  if (event.persisted) reveals.forEach(el => el.classList.add('is-visible'));
});
