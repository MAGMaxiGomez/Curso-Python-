'''
Práctica Crear y Escribir Archivos 2
Abre el archivo llamado "mi_archivo.txt", y añade una línea al final del mismo que diga: "Nuevo inicio de sesión".

Imprime el contenido completo de "mi_archivo.txt" al finalizar.

Pista: deberás cerrarlo en modo escritura y volverlo a abrir en modo lectura.
'''
archivo = open("mi_archivo.txt", "a")
archivo.write("Nuevo inicio de sesión")
archivo.close()
archivo = open("mi_archivo.txt", "r")
print(archivo.read())
archivo.close()