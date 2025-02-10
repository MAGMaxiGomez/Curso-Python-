'''
Práctica Funciones Dinámicas 1
Crea una función (todos_positivos) que reciba una lista de números como parámetro, 
y devuelva True si todos los valores de una lista son positivos, y False si al menos uno de los valores es negativo. 
Crea una lista llamada lista_numeros con valores positivos y negativos.
No invoques la función, solo es necesario definirla.
'''
lista_numeros = [100, 56, 23]


def todos_positivos(lista):
    for n in lista:
        if n > 0:
            pass
        else:
            return False
    return True

resultado = todos_positivos(lista_numeros)
print(lista_numeros)