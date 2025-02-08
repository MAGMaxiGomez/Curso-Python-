'''
Primero el programa preguntara el nombre del usuario.
Escribira en pantalla "piensa en un numero del 1 al 100"
y tenes 8 vidas
4 tipos de respuestas:
1 = Menor a 1 o superior a 100, msj diciendo que no esta permitido 
2 = Numero menor = respuesta incorrecta y que es menor al numero secreto
3 = Numero mayor = respuesta incorrecta y que es mayor al numero secreto
4 = Numero correcto = msj de que a ganado y de la cantidad de intentos que le a tomado 
si no acierta se le volvera a preguntar por un numero hasta que gane o se quede sin vidas o intentos
'''
from random import *

nombre_usuario = input("ingrese su nombre : ")
intentos = 8
numero_secreto =  randint(1, 100)

while intentos > 0:
    numero_elegido = int(input("adivina el numero secreto, elije un numero del 1 al 100 :"))
    if numero_elegido < 0 or numero_elegido > 100:
            print("El numero que elegiste esta fuera de las reglas, intenta con un numero del 1 al 100")
    elif numero_elegido < numero_secreto:
            print("Respuesta erroenea, el numero que elegiste es menor al numero secreto, intentalo otra vez")
            intentos -= 1
            print(f"Te quedan {intentos} intentos")
    elif numero_elegido > numero_secreto:
            print("Respuesta erronea, el numero que elegiste es mayor al numero secreto, intentalo otra vez")
            intentos -= 1
            print(f"Te quedan {intentos} intentos")
    else:
           print(f"felicitaciones tu respuesta es corresta, el numero secreto si era {numero_secreto}")
if intentos == 0:
       print("Lastimosamente te quedaste sin intentos y has perdido. Pero no te rindas y intentalo de nuevo.")