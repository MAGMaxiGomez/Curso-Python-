'''
Práctica Crear y Escribir Archivos 2
Abre el archivo llamado "mi_archivo.txt", y añade una línea al final del mismo que diga: "Nuevo inicio de sesión".

Imprime el contenido completo de "mi_archivo.txt" al finalizar.

Pista: deberás cerrarlo en modo escritura y volverlo a abrir en modo lectura.
'''

mi_archivo = open("mi_archivo.txt", "a")

mi_archivo.write("Nuevo inicio de sesión")

mi_archivo.close()

mi_archivo = open("mi_archivo.txt", "r")

print(mi_archivo.read())

mi_archivo.close()