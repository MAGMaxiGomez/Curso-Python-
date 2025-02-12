'''
Práctica sobre Argumentos Indefinidos (**kwargs) 1
Crea una función llamada cantidad_atributos que cuente la cantidad de parémetros que se entregan, y devuelva esa cantidad como resultado.
'''
def cantidad_atributos(**kwargs):
    cantidad = 0

    for clave, valor in kwargs.items():
        cantidad += 1

    return cantidad

print(cantidad_atributos(x = 100, y = 200, z = 300))