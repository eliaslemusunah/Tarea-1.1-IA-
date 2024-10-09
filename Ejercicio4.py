# Ejercicio 4: Clase Calculadora

class Calculadora:
    def Sumar(self, a, b):
        return a + b
    def Restar(self, a, b):
        return a - b
    def Multiplicar(self, a, b):
        return a * b
    
    def Dividir(self, a, b):
        if b == 0:
            print('¡Error! No se puede dividir entre cero.')
            return None
        else:
            return a / b
        
calculadora = Calculadora()


try:
    numero1 = int(input('Ingrese el primero número: '))
    numero2 = int(input('Ingrese el segundo número: '))

    suma = calculadora.Sumar(numero1, numero2)
    resta = calculadora.Restar(numero1, numero2)
    multiplicacion = calculadora.Multiplicar(numero1, numero2)
    division = calculadora.Dividir(numero1, numero2)

    print(f'\nLa suma es: {suma}')
    print(f'La resta es: {resta}')
    print(f'La multiplicación es: {multiplicacion}')

    if division is not None:
        print(f'La división es: {division}')
except ValueError:
    print('¡ERROR!')