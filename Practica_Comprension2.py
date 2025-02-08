'''
Práctica Comprensión de Listas 2
Crea una lista valores_pares formada por los números de la lista valores que (¡adivinaste!) sean pares.
'''
valores = [1, 2, 3, 4, 5, 6, 9.5] 
valores_pares = [n for n in valores  if n % 2 == 0]

print(valores_pares)