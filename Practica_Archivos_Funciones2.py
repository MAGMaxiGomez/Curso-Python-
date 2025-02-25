'''
Práctica Archivos y Funciones 2
Crea una función llamada sobrescribir() que abra (open) un archivo indicado como parámetro, 
y sobrescriba cualquier contenido anterior por el texto "contenido eliminado"
'''

def sobrescribir(nombre_archivo):
    mi_archivo = open(nombre_archivo , "w")
    
    mi_archivo.write("contenido eliminado")

    mi_archivo.close

    mi_archivo = open(nombre_archivo, "r")

    return mi_archivo.read()

print(sobrescribir("prueba.txt"))