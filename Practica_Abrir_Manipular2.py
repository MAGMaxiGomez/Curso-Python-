'''
Práctica Abrir y Manipular Archivos 2
Imprime la primera línea del archivo texto.txt

No olvides abrir el archivo y cerrarlo luego de ejecutar tu código.

Nota: el archivo se encuentra guardado en la misma carpeta donde se aloja tu código
'''

mi_archivo = open("texto.txt")

primer_linea = mi_archivo.readline()

print(primer_linea)

mi_archivo.close()