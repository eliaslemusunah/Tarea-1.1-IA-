# Ejercicio 8: Contador de Vocales

def contar_vocales(frase):
    vocales = 'aeiouáéíóúAEIOUÁÉÍÓÚ'
    contador = 0
    
    for letra in frase:
        if letra in vocales:
            contador += 1
    
    return contador

frase_usuario = input('Ingrese una frase: ')
total_vocales = contar_vocales(frase_usuario)
print(f'Número total de vocales en la frase: {total_vocales}')