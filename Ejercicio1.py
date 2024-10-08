# Ejercicio 1: Clase Rectángulo

class Rectangulo:
    def __init__(self, base, altura):
        self.base = float(base)
        self.altura = float(altura)

    def area(self) -> float:
        return self.base * self.altura
    
    def perimetro(self) -> float:
        return 2 * (self.base + self.altura)
    
rectangulo = Rectangulo(5.5, 3.0)
print(f'El área del rectángulo es {rectangulo.area()} y su perímetro es {rectangulo.perimetro()}.')