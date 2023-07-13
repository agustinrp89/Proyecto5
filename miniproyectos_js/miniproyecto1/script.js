function calcularIngresos() {
    var horasTrabajadas = parseInt(document.getElementById("horas").value);
    var tarifaHora = parseFloat(document.getElementById("tarifa").value);
  
    if (isNaN(horasTrabajadas) || isNaN(tarifaHora)) {
      alert("Por favor, ingresa valores numéricos válidos.");
      return;
    }
  
    var ingresos = horasTrabajadas * tarifaHora;
  
    var tablaResultados = document.getElementById("tabla-resultados");
    var fila = tablaResultados.insertRow();
  
    var celdaSemana = fila.insertCell();
    celdaSemana.innerHTML = tablaResultados.rows.length - 1;
  
    var celdaHoras = fila.insertCell();
    celdaHoras.innerHTML = horasTrabajadas;
  
    var celdaTarifa = fila.insertCell();
    celdaTarifa.innerHTML = "$" + tarifaHora.toFixed(2);
  
    var celdaIngresos = fila.insertCell();
    celdaIngresos.innerHTML = "$" + ingresos.toFixed(2);
  }
  