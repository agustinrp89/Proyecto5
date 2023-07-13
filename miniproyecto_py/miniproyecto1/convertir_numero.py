# Diccionario para convertir números en palabras
numeros = {
    0: 'cero',
    1: 'uno',
    2: 'dos',
    3: 'tres',
    4: 'cuatro',
    5: 'cinco',
    6: 'seis',
    7: 'siete',
    8: 'ocho',
    9: 'nueve',
    10: 'diez',
    11: 'once',
    12: 'doce',
    13: 'trece',
    14: 'catorce',
    15: 'quince',
    16: 'dieciséis',
    17: 'diecisiete',
    18: 'dieciocho',
    19: 'diecinueve',
    20: 'veinte',
    30: 'treinta',
    40: 'cuarenta',
    50: 'cincuenta',
    60: 'sesenta',
    70: 'setenta',
    80: 'ochenta',
    90: 'noventa',
    100: 'cien',
    200: 'doscientos',
    300: 'trescientos',
    400: 'cuatrocientos',
    500: 'quinientos',
    600: 'seiscientos',
    700: 'setecientos',
    800: 'ochocientos',
    900: 'novecientos'
}

def convertir_a_palabras(numero):
    if numero in numeros:
        return numeros[numero]

    if numero < 100:
        decenas = (numero // 10) * 10
        unidades = numero % 10
        return numeros[decenas] + " y " + numeros[unidades]

    if numero < 1000:
        centenas = (numero // 100) * 100
        resto = numero % 100
        if resto == 0:
            return numeros[centenas]
        else:
            return numeros[centenas] + " " + convertir_a_palabras(resto)

    return "Número fuera de rango"

# Ejemplo de uso
numero = int(input("Ingresa un número: "))
palabras = convertir_a_palabras(numero)
print(palabras)
