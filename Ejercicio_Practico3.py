'''
Ejercicio 3
Escribe una función que requiera una cantidad indefinida de argumentos. 
Lo que hará esta función es devolver True si en algún momento se ha ingresado al numero cero repetido dos
veces consecutivas.
por ejemplo:
(5,6,1,0,0,9,3,5) >>> True
(6,0,5,1,0,3,0,1) >>> Fals
'''

def ceros_seguidos(*args):
    for i in range(len(args) - 1):
        if args[i] == 0 and args[i + 1] == 0:
            return True
    return False
 
print(ceros_seguidos(5,6,1,0,0,9,3,5)) 
print(ceros_seguidos(6,0,5,1,0,3,0,1)) 