const filters = [...document.querySelectorAll('[data-menu-filter]')];
const groups = [...document.querySelectorAll('[data-menu-category]')];
const board = document.querySelector('.menu-board');
const status = document.querySelector('#menu-status');
let entrance;
function showCategory(category, animate = true) {
  if (!filters.some(button => button.dataset.menuFilter === category)) return;
  filters.forEach(button => button.setAttribute('aria-pressed', String(button.dataset.menuFilter === category)));
  let count = 0;
  groups.forEach(group => {
    group.hidden = category !== 'all' && group.dataset.menuCategory !== category;
    if (!group.hidden) count += group.querySelectorAll('.dish-list > li').length;
  });
  if (status) status.textContent = `Showing ${count} dishes`;
  entrance?.cancel();
  if (animate && board && !matchMedia('(prefers-reduced-motion: reduce)').matches) {
    entrance = board.animate([{opacity: .2, transform: 'translateY(8px)'}, {opacity: 1, transform: 'translateY(0)'}], {duration: 400, easing: 'ease-out'});
  }
}
filters.forEach(button => button.addEventListener('click', () => showCategory(button.dataset.menuFilter)));
if (filters.length) showCategory('all', false);
