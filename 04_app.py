# Calcular el 18% de IGV a partir de un monto de pago

# Inicio: Definir o crear las variables
monto_pago = 600
igv = 0.18

# Proceso: Realizar las operaciones de cálculo 
monto_a_pagar = monto_pago + (monto_pago * igv)

# Salida: Visualización de resultados
print(monto_a_pagar)
print(f"El monto es: {monto_pago}")
print(f"El IGV es: {igv}")
print(f"El monto a pagar es: {monto_a_pagar}")
igv_total = (monto_pago * igv)
print(f"el 18% es : {igv_total}")