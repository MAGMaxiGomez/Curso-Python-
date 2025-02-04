'''
Pidale al usuario un texto, luego que ingrese 3 letras a su eleccion, escribir en pantalla las veces que aparecen las letras elegidas
la cantidad de palbras, letra de incio y de fin, el texto invertido y si dentro del texto se encuentra la palabra 'python'
'''
texto = input("ingrese un texto : ")
letras =[]

texto = texto.lower()

letras.append(input("ingrese la primera letra : ").lower())
letras.append(input("ingrese la segunda letra : ").lower())
letras.append(input("ingrese la tercera letra : ").lower())

print("\n")
print("CANTIDAD DE LETRAS :")

cantidad_letras1 = texto.count(letras[0])
cantidad_letras2 = texto.count(letras[1])
cantidad_letras3 = texto.count(letras[2])

print(f"Se ha encontrado la letra {letras[0]} un total de : {cantidad_letras1} veces")
print(f"Se ha encontrado la letra {letras[1]} un total de : {cantidad_letras2} veces")
print(f"Se ha encontrado la letra {letras[2]} un total de : {cantidad_letras3} veces")

print("\n")
print("CANTIDAD DE PALABRAS : ")
palabras = texto.split()
print(f"Se ha encontrado {len(palabras)} palabras en el texto")

print("\n")
print("LETRAS DE INICIO Y FIN : ")
letra_inicio = texto[0]
letra_final = texto[-1]
print(f"La letra de inicio es '{letra_inicio}' y la letra final es '{letra_final}'")

print("\n")
print("TEXTO INVERTIDO : ")
palabras.reverse()
texto_invertido = ' '.join(palabras)
print(f"Si ordenamos el texto al reves seria : {texto_invertido}")

print("\n")
print("BUSCANDO LA PALABRA 'Python' : ")
if "python" in texto:
    print("La palabra 'Python' si se encuentra en el texto")
else :
    print("Lastimosamente la Palabra 'Python' no se encuentra en el texto")