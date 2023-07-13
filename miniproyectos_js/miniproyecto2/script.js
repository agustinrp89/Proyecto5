  var page = 1;
  var isLoading = false;

  function fetchData() {
    isLoading = true;
    
    // Simular una llamada a una API o carga de datos
    setTimeout(function() {
      var data = ['Elemento 1', 'Elemento 2', 'Elemento 3', 'Elemento 4', 'Elemento 5', 'Elemento 6', 'Elemento 7', 'Elemento 8', 'Elemento 9', 'Elemento 10', 'Elemento 11', 'Elemento 12', 'Elemento 13', 'Elemento 14', 'Elemento 15', 'Elemento 16', 'Elemento 17', 'Elemento 18'];
      var content = document.getElementById('content');

      for (var i = 0; i < data.length; i++) {
        var item = document.createElement('div');
        item.innerHTML = data[i];
        content.appendChild(item);
      }

      isLoading = false;
      page++;
    }, 1000);
  }

  function handleScroll() {
    var contentHeight = document.getElementById('content').offsetHeight;
    var yOffset = window.pageYOffset;
    var y = yOffset + window.innerHeight;

    if (y >= contentHeight && !isLoading) {
      fetchData();
    }
  }

  window.addEventListener('scroll', handleScroll);

  // Cargar datos iniciales
  fetchData();
