# Programa de cálculo automático de tarifas para la empresa MoviExpress

# Solicitar al usuario la edad del pasajero
edad = int(input("Ingrese la edad del pasajero: "))

# Determinar la tarifa según la edad usando condicionales
if edad < 12:
    tarifa = 3.00
    mensaje = "Tarifa infantil"
elif edad <= 59:  # entre 12 y 59 años
    tarifa = 5.00
    mensaje = "Tarifa regular"
else:  # mayores de 60
    tarifa = 2.00
    mensaje = "Tarifa especial"

# Mostrar el precio final
print(f"{mensaje}: S/ {tarifa:.2f}")