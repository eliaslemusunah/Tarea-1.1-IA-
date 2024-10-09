# Ejercicio 5: Número Primo

def es_primo(n):
    if n <= 1:
        return False  # Los números menores o iguales a 1 no son primos.
    for i in range(2, int(n**0.5) + 1):  # Solo se necesita comprobar hasta la raíz cuadrada de n.
        if n % i == 0:  # Si n es divisible por i, no es primo.
            return False
    return True

try:
    numero = int(input('Ingrese un número entero: '))
    if es_primo(numero):
        print(f'{numero} es un número primo.')
    else:
        print(f'{numero} no es un número primo.')
except ValueError:
    print('¡Error! Por favor, ingrese un número entero válido.')