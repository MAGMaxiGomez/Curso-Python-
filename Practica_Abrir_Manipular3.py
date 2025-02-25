'''
Práctica Abrir y Manipular Archivos 3
Abre el archivo texto.txt e imprime únicamente la segunda línea.
'''
mi_archivo = open("texto.txt")

lista = mi_archivo.readlines()

print(lista[1])