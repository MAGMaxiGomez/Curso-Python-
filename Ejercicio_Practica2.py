'''
Ejercicio 2
Escribe una función (puedes ponerle cualquier nombre que
quieras) que reciba cualquier palabra como parámetro, y que
devuelva todas sus letras únicas (sin repetir) pero en orden
alfabético.
Por ejemplo si al invocar esta función pasamos la palabra
"entretenido"
, debería devolver ['d', 'e', 'i', 'n', 'o', 'r', 't']
'''

def ingresar_nombre(nombre):
    mi_set = set()

    for letra in nombre:
        mi_set.add(letra)

    mi_lista = list(mi_set)
    mi_lista.sort()
    
    return mi_lista

print(ingresar_nombre("cascarrabia"))