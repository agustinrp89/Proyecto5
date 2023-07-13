document.addEventListener('DOMContentLoaded', function() {
    var form = document.querySelector('form');
    var movieInput = document.getElementById('movie');
    var ratingMessage = document.getElementById('rating-message');
  
    form.addEventListener('submit', function(event) {
      event.preventDefault();
  
      var movie = movieInput.value.trim();
  
      if (movie === '') {
        alert('Por favor, ingresa el título de una película.');
        return;
      }
  
      ratingMessage.textContent = 'Cargando...';
  
      fetch('/rating', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ movie: movie })
      })
        .then(response => response.json())
        .then(data => {
          ratingMessage.textContent = data.rating;
        })
        .catch(error => {
          console.error('Error:', error);
          ratingMessage.textContent = 'Error al obtener el rating.';
        });
    });
  });
  