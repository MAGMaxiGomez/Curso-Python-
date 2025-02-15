'''
Crea una función lamada devolver_distintos() que reciba 3 integers como parámetros.
Si la suma de los 3 numeros es mayor a 15, va a devolver el número mayor.

 Si la suma de los 3 numeros es menor a 10, va a devolver el número menor.

 Si la suma de los 3 números es un valor entre 10 y 15 (incluidos) va a devolver el número de valor intermedio
'''
def devolver_distintos(num1, num2, num3):
    lista = [num1, num2, num3]
    suma = sum(lista)

    if suma > 15:
        print(max(lista))
    elif suma < 10:
        print(min(lista))
    else:
        lista.sort()
        print(lista[1])
        
    return 0


print(devolver_distintos(2, 10, 1))