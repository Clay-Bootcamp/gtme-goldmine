const items = document.querySelectorAll('.note-item');
const contents = document.querySelectorAll('.note-content');

function selectNote(id) {
  items.forEach((item) => {
    item.classList.toggle('active', item.dataset.note === id);
  });
  contents.forEach((content) => {
    content.hidden = content.dataset.note !== id;
  });
  const pane = document.querySelector('.pane');
  if (pane) pane.scrollTop = 0;
}

items.forEach((item) => {
  item.addEventListener('click', () => selectNote(item.dataset.note));
});
