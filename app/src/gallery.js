const photos = [...document.querySelectorAll('[data-gallery]')];
const dialog = document.querySelector('#photo-viewer');
if (photos.length && dialog) {
  const image = dialog.querySelector('img');
  const caption = dialog.querySelector('figcaption');
  let index = 0;
  let opener;
  const show = next => {
    index = (next + photos.length) % photos.length;
    const source = photos[index].querySelector('img');
    image.src = source.currentSrc || source.src;
    image.alt = source.alt;
    caption.textContent = source.alt;
    if (!matchMedia('(prefers-reduced-motion: reduce)').matches) image.animate([{opacity: .15}, {opacity: 1}], {duration: 350});
  };
  photos.forEach((link, i) => link.addEventListener('click', event => {
    event.preventDefault(); opener = link; show(i); dialog.showModal();
    document.documentElement.classList.add('photo-open');
    dialog.querySelector('[data-close]').focus();
  }));
  dialog.querySelector('[data-close]').addEventListener('click', () => dialog.close());
  dialog.querySelector('[data-prev]').addEventListener('click', () => show(index - 1));
  dialog.querySelector('[data-next]').addEventListener('click', () => show(index + 1));
  dialog.addEventListener('click', event => { if (event.target === dialog) dialog.close(); });
  dialog.addEventListener('keydown', event => {
    if (event.key === 'ArrowLeft') { event.preventDefault(); show(index - 1); }
    if (event.key === 'ArrowRight') { event.preventDefault(); show(index + 1); }
  });
  dialog.addEventListener('close', () => {
    document.documentElement.classList.remove('photo-open'); opener?.focus({preventScroll: true});
  });
}
