// Función para calcular y mostrar la cuenta regresiva
function countdown() {
    // Obtener la fecha actual y la fecha del año nuevo
    var now = new Date();
    var newYear = new Date(now.getFullYear() + 1, 0, 1);
    
    // Calcular la diferencia entre las fechas
    var timeLeft = newYear - now;
    
    // Calcular los días, horas, minutos y segundos restantes
    var days = Math.floor(timeLeft / (1000 * 60 * 60 * 24));
    var hours = Math.floor((timeLeft % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    var minutes = Math.floor((timeLeft % (1000 * 60 * 60)) / (1000 * 60));
    var seconds = Math.floor((timeLeft % (1000 * 60)) / 1000);
    
    // Mostrar la cuenta regresiva en el elemento con el id "countdown"
    document.getElementById("countdown").innerHTML = days + " días, " + hours + " horas, " + minutes + " minutos, " + seconds + " segundos.";
  }
  
  // Actualizar la cuenta regresiva cada segundo
  setInterval(countdown, 1000);
  