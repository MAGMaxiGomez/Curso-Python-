'''
Práctica sobre Interacción entre Funciones 3
Crea una función (llamada lanzar_moneda) que devuelva el resultado de lanzar una moneda (al azar). 
Dicha función debe poder devolver los resultados "Cara" o "Cruz", y no debe recibir argumentos para funcionar.
Crea una segunda función (llamada probar_suerte), que tome dos argumentos: el primero, debe ser el resultado del lanzamiento de la moneda. 
El segundo argumento, será una lista de números cualquiera (debes crear una lista con valores y llamarla lista_numeros).
Si se le proporciona una "Cara", debe mostrar el mensaje al usuario: "La lista se autodestruirá", y eliminarla (devolverla como lista vacía []).
Si se le proporciona una "Cruz", debe imprimir en pantalla: "La lista fue salvada" y devolver la lista intacta.
Pistas: utiliza el método choice de la biblioteca random para elegir un elemento al azar de una secuencia.
'''
from random import *

lista_numeros = [1, 2, 3, 4, 5]

def lanzar_moneda():
    valores = ["Cara", "Cruz"]
    azar = choice(valores)
    return azar

azar = lanzar_moneda()

def probar_suerte(azar, lista):
    resultado = lanzar_moneda()
    if resultado == "Cara":
        print("La lista se autodestruirá")
        return []
    else:
        print("La lista fue salvada")
    return lista

print(lanzar_moneda())
print(probar_suerte(azar, lista_numeros))