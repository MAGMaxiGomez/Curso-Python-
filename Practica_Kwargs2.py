'''
Práctica sobre Argumentos Indefinidos (**kwargs) 2
Crea una función llamada lista_atributos que devuelva en forma de lista los valores de los atributos 
entregados en forma de palabras clave (keywords). La función debe preveer recibir cualquier cantidad de argumentos de este tipo.
'''

def lista_atributos(**kwargs):
    lista = []
    i = 0

    for clave,valor in kwargs.items():
        nuevo_elemento2 = lista.append(valor)
        i += 1

    return lista    


print(lista_atributos(x = 100, y = "hola"))