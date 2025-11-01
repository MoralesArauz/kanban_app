document.addEventListener('DOMContentLoaded', () => {
  // ✅ Drag-and-drop setup
  document.querySelectorAll('.card-container').forEach(container => {
    new Sortable(container, {
      group: 'cards',
      animation: 150,
      onEnd: function (evt) {
        const cardId = evt.item.dataset.cardId;
        const newListId = evt.to.id.replace('cards-', '');
        console.log(`Moved card: ${cardId} to list: ${newListId}`);

        document.querySelectorAll('.card-container').forEach(c => {
          c.classList.remove('drag-over');
        });

        fetch(`/move_card/${cardId}`, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ list_id: newListId })
        });
      }
    });

    container.addEventListener('dragover', () => {
      container.classList.add('drag-over');
    });

    container.addEventListener('dragleave', () => {
      container.classList.remove('drag-over');
    });
  });

  // ✅ Add card via AJAX
  document.querySelectorAll('.add-card-form').forEach(form => {
    form.addEventListener('submit', e => {
      e.preventDefault();

      const listId = form.dataset.listId;
      const formData = new FormData(form);

      fetch(`/add_card/${listId}`, {
        method: 'POST',
        body: formData
      })
      .then(response => {
        if (response.ok) {
          location.reload();
        } else {
          alert('Error adding card');
        }
      });
    });
  });

  // ✅ Inline list name editing
  document.querySelectorAll('.list-header').forEach(header => {
    const title = header.querySelector('.list-name');
    const icon = header.querySelector('.edit-icon');
    const form = header.querySelector('.edit-list-form');
    const input = form.querySelector('input');

    icon.addEventListener('click', () => {
      title.style.display = 'none';
      icon.style.display = 'none';
      form.classList.remove('d-none');
      input.focus();
    });

    input.addEventListener('keydown', (e) => {
      if (e.key === 'Enter') {
        e.preventDefault();
        form.submit();
      } else if (e.key === 'Escape') {
        form.classList.add('d-none');
        title.style.display = '';
        icon.style.display = '';
      }
    });
  });
});