# Ejercicio 6: Secuencia de Fibonacci

def Fibonacci(n):
    
    a, b = 0, 1  # Inicializamos los dos primeros números de Fibonacci.
    for _ in range(n):
        print(a, end=', ' if _ < n - 1 else '\n')  # Imprimimos el número actual.
        a, b = b, a + b  # Actualizamos los números para la siguiente iteración.

try:
    n = int(input('Ingrese el número de términos: '))
    if n <= 0:
        print('Por favor, ingrese un número entero positivo.')
    else:
        print('Secuencia de Fibonacci:')
        Fibonacci(n)
except ValueError:
    print('¡Error! Por favor, ingrese un número entero válido.')