# Ejercicio 10: Generador de Contraseñas

import random

def generar_contrasenna(longitud):
    mayusculas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    minusculas = 'abcdefghijklmnopqrstuvwxyz'
    numeros = '0123456789'
    simbolos = '!@#$%^&*()_+-=[]{}|;:,.<>?/'
    caracteres = mayusculas + minusculas + numeros + simbolos
    contrasenna = ''
    for _ in range(longitud):
        indice = random.randint(0, len(caracteres) - 1)
        contrasenna += caracteres[indice]
    return contrasenna

control = True
long = None

while control:
    try:
        if long is None:
            long = int(input('Ingrese la longitud de la contraseña (mínimo 8): '))
        if long < 8:
            print('La longitud de la contraseña debe ser mayor o igual a 8.')
            long = None
        else:
            control = False
    except ValueError:
        print('Ingrese un valor válido, intente de nuevo.')
        long = None

contrasenna_generada = generar_contrasenna(long)

if contrasenna_generada:
    print('Contraseña generada: ' +contrasenna_generada)