// Obtenemos la referencia al formulario y al elemento de salida
const form = document.getElementById('audioForm');
const translatedText = document.getElementById('translatedText');

// Función para iniciar el reconocimiento de voz
function startRecognition() {
  // Verificamos si el navegador es compatible con el reconocimiento de voz
  if ('webkitSpeechRecognition' in window) {
    // Creamos una instancia de reconocimiento de voz
    const recognition = new webkitSpeechRecognition();

    // Establecemos el idioma de reconocimiento
    recognition.lang = 'es-ES'; // Configura el idioma según tus necesidades

    // Configuramos el evento de resultado del reconocimiento
    recognition.onresult = function(event) {
      const result = event.results[0][0].transcript;
      translatedText.textContent = result;
    }

    // Iniciamos el reconocimiento de voz
    recognition.start();
  } else {
    // El navegador no es compatible con el reconocimiento de voz
    translatedText.textContent = 'El reconocimiento de voz no es compatible con este navegador.';
  }
}
