'''
Práctica Path 2
Implementa y crea una ruta relativa que nos permita llegar al archivo "practicas_path.py" a partir de la siguiente estructura de carpetas:


Almacena el directorio obtenido en la variable ruta. No olvides importar Path.
'''

"Curso Python"
"Día 6"
"practicas_path.py"
from pathlib import Path
 
ruta = Path("Curso Python","Día 6","practicas_path.py")

print(ruta)