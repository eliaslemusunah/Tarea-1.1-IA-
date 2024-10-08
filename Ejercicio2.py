# Ejercicio 2: Clase Libro

class Libro:
    def __init__(self, titulo, autor, anno_publicacion, numero_paginas):
        self.titulo = str(titulo)
        self.autor = str(autor)
        self.anno_publicacion = int(anno_publicacion)
        self.numero_paginas = int(numero_paginas)

    def mostrar_informacion(self):
        print(f'Título: {self.titulo}\nAutor: {self.autor}\nAño de publicación: {self.anno_publicacion}\nNo. de páginas: {self.numero_paginas}')

donquijote = Libro('Don Quijote de la Mancha', 'Miguel de Cervantes', 1605, 863)
donquijote.mostrar_informacion()