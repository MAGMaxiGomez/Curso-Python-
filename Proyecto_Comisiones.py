porcentaje_comision = 13
nombre_usuario = input("Ingrese su nombre : ")
ventas_usuario = int(input("Ingrese la cantidad de ventas : "))

comisiones = round(ventas_usuario * porcentaje_comision / 100, 2)

print(f"Hola {nombre_usuario}, Su comision por parte de las ventas es ${comisiones}")