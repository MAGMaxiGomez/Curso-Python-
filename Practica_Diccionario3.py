'''
Práctica Diccionarios 3
Actualiza la información de nuestro diccionario llamado mi_dic  (reasignando nuevos valores a las claves según corresponda), y agrega una nueva clave llamada "pais" (sin tilde). 
Los nuevos datos son:
* nombre: Karen
* apellido: Jurgens
* edad: 36
* ocupacion: Editora
* pais: Colombia
para ello, no debes cambiar la línea de código ya escrita, sino actualizar los valores mediante métodos de diccionarios.
'''
mi_dic = {"nombre":"Karen", "apellido":"Jurgens", "edad":35, "ocupacion":"Periodista"}
agregando1 = mi_dic["edad"] = 36
agregando2 = mi_dic["ocupacion"] = "Editora"
agregando3 = mi_dic["pais"] = "Colombia"
print(mi_dic.items())