# Ejercicio 7: Tabla de Multiplicar

try:
    numero = int(input('Ingrese un número: '))
    
    print(f'Tabla de multiplicar del {numero}:')
    
    for i in range(1, 11):  # Del 1 al 10.
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")
        
except ValueError:
    print('¡Error! Por favor, ingrese un número entero válido.')