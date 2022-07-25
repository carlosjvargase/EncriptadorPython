#Criptador de documentos.
#Python Write/ Create Files - Escribir/Modificar archivos
#Codigo#

# Para el encriptor se agrego la letra X a cada letra para encriptar

def encriptar(texto):
    textoFinal = ''
    for letra in texto:
        numero = ord(letra)
        #usamos x = ord('h') para pasar la letra a numero
        numero += 1
        # el texto ord le sumamos 1 numero más para cambiar el valor ascii
        textoFinal += chr(numero)
        # chr función que hace lo contrario de ord! pasamos un numero y nos devuelve la letra a usar
    return textoFinal

#Para desencriptar, debe existir una reversa al agregar la letra X
def desencriptar(texto):
    print('El texto a desencriptar es: ' + texto)
    textoFinal = ''
    for letra in texto:
        numero = ord(letra)
        numero -= 1
        textoFinal += chr(numero)
    return textoFinal

    print('El texto a desencriptar es: ' + textoFinal)

def encriptarArchivo(rutaArchivo):
    archivo = open(rutaArchivo, 'r')
    texto = archivo.read()
    archivo.close()
    textoEncriptado = encriptar(texto)

    archivo = open(rutaArchivo, 'w')
    archivo.write(textoEncriptado)
    archivo.close()
    print('El archivo se encripto correctamente')
def desencriptarArchivo(rutaArchivo):
    archivo = open(rutaArchivo, 'r')
    texto = archivo.read()
    archivo.close()
    textoDesencriptado = desencriptar(texto)

    archivo = open(rutaArchivo, 'w')
    archivo.write(textoDesencriptado)
    archivo.close()
    print('El archivo se desencripto correctamente')

respuestaEoD = input('Presione ¨E¨ para encriptar, o ¨D¨ para desencriptar')
rutaArchivo = input('Ingrese la ruta del archivo')

if respuestaEoD == 'E':
    encriptarArchivo(rutaArchivo)
else:
    desencriptarArchivo(rutaArchivo)
