'''
Práctica Abrir y Manipular Archivos 3
Abre el archivo texto.txt e imprime únicamente la segunda línea.
'''

mi_archivo = open("texto.txt")

primer_linea = mi_archivo.readline()
segunda_linea = mi_archivo.readline()

print(segunda_linea)