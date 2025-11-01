document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('.card-container').forEach(container => {
    new Sortable(container, {
      group: 'cards',
      animation: 150,
      onEnd: function (evt) {
        const cardId = evt.item.dataset.cardId;
        const newListId = evt.to.id.replace('cards-', '');
        console.log(`Moved card: ${cardId} to list: ${newListId}`);

        // ✅ Remove drag-over class from all containers
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
});