# variables

# las variables son palabras especificas que utilizamos para asignar y almacenar valores especificos que podemos recuperar en cualquier momento.

# variable nombre
nombre = "robert"
telefono = 987654321
name = "joel"

# vizualizando el contenido de las variables
print(nombre)
print(telefono)
print(name)

# jugando con variables
edad = 30
print(edad)
print(f"edad : {edad}")

distrito = "la molina"
print(distrito)
print(f"nombre del distrito : {distrito}")

# precio de un producto
precio = 55
print(precio)
print(f"precio del producto : {precio}")

# es un cliente activo
is_active_client = True
print(is_active_client)
print(f"¿esta actvo? :{is_active_client}")

# trabajando con fechas
from datetime import date
fecha_clase = date(2025, 9, 22) # (yyyy, mm, dd)
print(fecha_clase)
print(f"fecha de hoy : {fecha_clase}")

fecha_formateada = fecha_clase.strftime("%d/%m/%y")
print(f"la fecha de hoy formateada es : {fecha_formateada}")