'''
Práctica Funciones Dinámicas 3
Crea una función (cantidad_pares) que cuente la cantidad de números pares que existen 
en una lista (lista_numeros), y devuelva el resultado de dicha cuenta.
'''
lista_numeros = [1,2,3,4,5,6,7,8]

def cantidad_pares(lista_numeros):
    cantidad = 0
    for n in lista_numeros:
        if n %2 == 0:
            cantidad += 1
            pass
        else:
            pass
    return cantidad

resultado = cantidad_pares(lista_numeros)
print(resultado)    