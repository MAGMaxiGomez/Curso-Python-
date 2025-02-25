'''
Práctica Archivos y Funciones 1
Crea una función llamada abrir_leer() que abra (open) un archivo indicado como parámetro, y devuelva su contenido (read).
'''

def abrir_leer(nombre_archivo):
    mi_archivo = open(nombre_archivo)

    return mi_archivo.read()

print(abrir_leer("prueba.txt"))