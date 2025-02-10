'''
Práctica Funciones Dinámicas 2
Crea una función (suma_menores) que sume los números de una lista (almacenada en la variable lista_numeros) 
siempre y cuando sean mayores a 0 y menores a 1000, y devuelva el resultado de dicha suma.
'''
lista_numeros = [1,50,500,5000,750,600]
 
def suma_menores(lista_numeros):
    suma=0
    for numero in lista_numeros:
        if numero > 0 and numero < 1000:
            suma += numero
        else:
            pass
    return suma

resultado = suma_menores(lista_numeros)
print(resultado)