// Local menu browsing only; no ordering, inventory or remote requests.
const filters = [...document.querySelectorAll('[data-menu-filter]')];
const groups = [...document.querySelectorAll('[data-menu-category]')];
const status = document.querySelector('#menu-status');

function showCategory(category) {
  if (!['all', 'seafood', 'classics'].includes(category)) return;
  filters.forEach(button => button.setAttribute('aria-pressed', String(button.dataset.menuFilter === category)));
  groups.forEach(group => {
    const shown = category === 'all' || group.dataset.menuCategory === category;
    group.hidden = !shown;
    group.style.display = shown ? '' : 'none';
  });
  if (status) status.textContent = category === 'all' ? 'Showing all dishes' : `Showing ${category}`;
}

filters.forEach(button => button.addEventListener('click', () => showCategory(button.dataset.menuFilter)));
if (filters.length) showCategory('all');
