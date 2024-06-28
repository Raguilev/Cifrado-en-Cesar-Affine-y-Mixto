# Se crea la funcion mapeo en reemplazo a la función nativa "map" de Python
def mapeo(funcionalidad, iteracion): 
    resultados = [] 
    for item in iteracion:
        resultados.append(funcionalidad(item))
    return resultados

# Cifrados
def cifrado_cesar(texto, desplazamiento=3):
    def cifrar_caracter(char):
        if char.isupper(): 
            return chr((ord(char) + desplazamiento - 65) % 26 + 65)
        elif char.islower(): 
            return chr((ord(char) + desplazamiento - 97) % 26 + 97)
        else:
            return char

    return ''.join(mapeo(cifrar_caracter, texto))

def cifrado_affine(texto, a=5, b=8):
    m = 26

    def cifrar_caracter(char):
        if char.isupper():
            return chr(((a * (ord(char) - 65) + b) % m) + 65)
        elif char.islower():
            return chr(((a * (ord(char) - 97) + b) % m) + 97)
        else:
            return char

    return ''.join(mapeo(cifrar_caracter, texto))

def cifrado_mixto(texto):
    return cifrado_affine(cifrado_cesar(texto))