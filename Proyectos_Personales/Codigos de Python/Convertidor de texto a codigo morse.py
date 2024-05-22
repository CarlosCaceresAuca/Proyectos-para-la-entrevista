TEXTO_A_MORSE = {
    'A': '— .', 'B': '— . . .', 'C': '— . — .', 'D': '— . .',
    'E': '.', 'F': '. . — .', 'G': '— — .', 'H': '. . . .',
    'I': '. .', 'J': '. — — —', 'K': '— . —', 'L': '. — . .',
    'M': '— —', 'N': '— .', 'O': '— — —', 'P': '. — — .',
    'Q': '— — . —', 'R': '. — .', 'S': '. . .', 'T': '—',
    'U': '. . —', 'V': '. . . —', 'W': '. — —', 'X': '— . . —',
    'Y': '— . — —', 'Z': '— — . .',
    '1': '. — — — —', '2': '. . — — —', '3': '. . . — —',
    '4': '. . . . —', '5': '. . . . .', '6': '— . . . .',
    '7': '— — . . .', '8': '— — — . .', '9': '— — — — .', '0': '— — — — —',
    ', ': '— — . . — —', '.': '. — . — . —', '?': '. . — — . .',
    '/': '— . . — .', '-': '— . . . . —', '(': '— . — — .', ')': '— . — — . —',
    ' ': '  '
}

MORSE_A_TEXTO = {v: k for k, v in TEXTO_A_MORSE.items()}

def texto_a_morse(texto):
    codigo_morse = []
    for char in texto.upper():
        if char in TEXTO_A_MORSE:
            codigo_morse.append(TEXTO_A_MORSE[char])
    return ' '.join(codigo_morse)

def morse_a_texto(morse):
    texto = []
    letras_morse = morse.split(' ')
    for letra_morse in letras_morse:
        if letra_morse == '':
            texto.append(' ')
        elif letra_morse in MORSE_A_TEXTO:
            texto.append(MORSE_A_TEXTO[letra_morse])
    return ''.join(texto)

def almacenar_en_vector(codigo_morse):
    import numpy as np
    lista_morse = list(codigo_morse.replace(' ', ''))  
    return np.array(lista_morse)

def contar_simbolos(vector_morse):
    import numpy as np
    cantidad_puntos = np.count_nonzero(vector_morse == '.')
    cantidad_rayas = np.count_nonzero(vector_morse == '—')
    return cantidad_puntos, cantidad_rayas

def detectar_y_convertir(texto_entrada, tipo_conversion):
    if tipo_conversion == 'texto_a_morse':
        texto_convertido = texto_a_morse(texto_entrada)
        codigo_morse = texto_convertido
    elif tipo_conversion == 'morse_a_texto':
        texto_convertido = morse_a_texto(texto_entrada)
        codigo_morse = texto_entrada
    else:
        raise ValueError("Tipo de conversión no válido. Use 'texto_a_morse' o 'morse_a_texto'.")

    vector_morse = almacenar_en_vector(codigo_morse)
    cantidad_puntos, cantidad_rayas = contar_simbolos(vector_morse)

    return texto_convertido, vector_morse, cantidad_puntos, cantidad_rayas

def menu_conversion():
    print("Selecciona una opción:")
    print("1. Convertir texto a Morse")
    print("2. Convertir Morse a texto")
    opcion = input("Opción (1 o 2): ")

    if opcion == '1':
        texto = input("Introduce el texto para convertir a Morse: ")
        texto_convertido, vector_morse, cantidad_puntos, cantidad_rayas = detectar_y_convertir(texto, 'texto_a_morse')
    elif opcion == '2':
        morse = input("Introduce el código Morse para convertir a texto (usa — para rayas y . para puntos): ")
        texto_convertido, vector_morse, cantidad_puntos, cantidad_rayas = detectar_y_convertir(morse, 'morse_a_texto')
    else:
        print("Opción no válida.")
        return

    print(f"Texto convertido: {texto_convertido}")
    print(f"Vector Morse: {vector_morse}")
    print(f"Conteo de puntos: {cantidad_puntos}")
    print(f"Conteo de rayas: {cantidad_rayas}")

menu_conversion()
#Franz Carlos Caceres Auca