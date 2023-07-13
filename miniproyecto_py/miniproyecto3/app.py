import pyttsx3

# Inicializar el motor de síntesis de voz
engine = pyttsx3.init()

# Configurar la velocidad de habla
engine.setProperty('rate', 150)

# Definir las opciones del menú
menu_options = {
    '1': 'Opción 1: Información general',
    '2': 'Opción 2: Servicios disponibles',
    '3': 'Opción 3: Consultas y soporte',
    '4': 'Opción 4: Hablar con un representante'
}

# Función para reproducir la opción seleccionada
def play_option(option):
    if option in menu_options:
        engine.say(menu_options[option])
        engine.runAndWait()
    else:
        engine.say('Opción inválida')
        engine.runAndWait()

# Reproducir el menú principal
engine.say('Bienvenido al menú telefónico. Por favor, seleccione una opción.')
engine.runAndWait()

# Mostrar las opciones y esperar la entrada del usuario
for key, value in menu_options.items():
    print(key, "-", value)

selected_option = input('Seleccione una opción: ')

# Reproducir la opción seleccionada
play_option(selected_option)
