# Ejercicio 9: Adivina el Número

import random

def adivina_el_numero():
    numero_a_adivinar = random.randint(1, 100)
    intentos = 0

    print('¡Adivina el número entre 1 y 100!')

    while True:
        try:
            intento = int(input('Ingresa tu intento: '))
            intentos += 1

            if intento < numero_a_adivinar:
                print('El número es mayor.')
            elif intento > numero_a_adivinar:
                print('El número es menor.')
            else:
                print(f'¡Felicitaciones! Has adivinado el número en {intentos} intentos.')
                break
                
        except ValueError:
            print('¡ERROR! Por favor, ingresa un número entero válido.')

adivina_el_numero()