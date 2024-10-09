# Ejercicio 3: Clase CuentaBancaria

class CuentaBancaria:
    def __init__(self, titular):
        self.titular = str(titular)
        self.saldo = 0.0

    def depositar(self, cantidad: float):

        if cantidad > 0:
            self.saldo += cantidad
            print(f'Has depositado  {cantidad}. Tu nuevo saldo:  {self.saldo}')
        else:
            print(f'¡ERROR!')
            
    def retirar(self, cantidad: float):

        if cantidad > 0:
            if self.saldo >= cantidad:
                self.saldo -= cantidad
                print(f'Has retirado {cantidad}. Tu nuevo saldo: {self.saldo}')
            else:
                print(f'¡Fondos insuficientes! :(. Tu saldo: {self.saldo}')
        else:
            print(f'¡ERROR!')

    def mostrar_saldo(self):
        print(f'Su saldo actual es de: {self.saldo}')

cuentapersonal = CuentaBancaria('Elías J. Lemus')
cuentapersonal.mostrar_saldo()
cuentapersonal.depositar(1.0)
cuentapersonal.depositar(100.0)
cuentapersonal.retirar(201.0)
cuentapersonal.retirar(79.9)