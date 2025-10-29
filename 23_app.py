#Evaluación trimestral de desempeño - Empresa Soluciones tech


def clasificar(p):
    if p < 70:
        return "Necesita Mejora"
    elif p < 90:
        return "Cumple Expectativas"
    else:
        return "Sobresaliente"

def calcular_ponderado(cal, prod, com, pun):
    return cal * 0.30 + prod * 0.30 + com * 0.20 + pun * 0.20

def pedir_float(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            if 0 <= valor <= 100:
                return valor
            else:
                print(" Ingrese un número entre 0 y 100.")
        except ValueError:
            print(" Valor inválido. Intente nuevamente.")

def main():
    print("=== EVALUACIÓN TRIMESTRAL DE DESEMPEÑO ===\n")

    #Cantidad de empleados
    while True:
        try:
            n = int(input("Ingrese la cantidad total de empleados a evaluar: "))
            if n > 0:
                break
            else:
                print(" Debe ser un número mayor que cero.")
        except ValueError:
            print(" Ingrese un número válido.")

    empleados = []

    # Ingreso de datos
    for i in range(1, n + 1):
        print(f"\nEmpleado {i} de {n}")
        codigo = input("Código único: ").strip()
        nombre = input("Nombre completo: ").strip()
        departamento = input("Departamento: ").strip()
        if nombre == "":
            nombre = "(Sin nombre)"
        if departamento == "":
            departamento = "(Sin especificar)"

        cal = pedir_float("Calidad de trabajo (0-100): ")
        prod = pedir_float("Productividad (0-100): ")
        com = pedir_float("Comunicación (0-100): ")
        pun = pedir_float("Puntualidad (0-100): ")

        total = calcular_ponderado(cal, prod, com, pun)
        clas = clasificar(total)

        empleados.append({
            "codigo": codigo,
            "nombre": nombre,
            "departamento": departamento,
            "calidad": cal,
            "productividad": prod,
            "comunicacion": com,
            "puntualidad": pun,
            "total": total,
            "clasificacion": clas
        })

    #Reporte tabulado
    print("\n=== REPORTE DE DESEMPEÑO ===")
    print("Código   Nombre                      Depto.             Total     Clasificación")
    print("-" * 80)
    for e in empleados:
        print(f"{e['codigo']:<8} {e['nombre'][:22]:<25} {e['departamento'][:12]:<15} {e['total']:7.2f}   {e['clasificacion']}")

    #Estadísticas generales
    total_mejora = sum(1 for e in empleados if e["clasificacion"] == "Necesita Mejora")
    total_cumple = sum(1 for e in empleados if e["clasificacion"] == "Cumple Expectativas")
    total_sobres = sum(1 for e in empleados if e["clasificacion"] == "Sobresaliente")

    mayor = max(empleados, key=lambda x: x["total"])
    menor = min(empleados, key=lambda x: x["total"])

    print("\n=== ESTADÍSTICAS ===")
    print(f"Total empleados evaluados: {n}")
    print(f"Necesita Mejora: {total_mejora}")
    print(f"Cumple Expectativas: {total_cumple}")
    print(f"Sobresaliente: {total_sobres}")
    print(f"Empleado con mayor puntaje: {mayor['nombre']} ({mayor['total']:.2f}) - {mayor['departamento']}")
    print(f"Empleado con menor puntaje: {menor['nombre']} ({menor['total']:.2f}) - {menor['departamento']}")

     #Exportar a CSV
    guardar = input("\n¿Desea guardar los resultados en CSV? (s/n): ").strip().lower()
    if guardar == "s":
        archivo = input("Nombre del archivo (ejemplo: resultados.csv): ").strip()
        if archivo == "":
            archivo = "resultados.csv"
        with open(archivo, "w", newline='', encoding="utf-8") as f:
            campos = ["id", "nombre", "calidad", "productividad", "comunicacion", "puntualidad", "total", "clasificacion"]
            writer = csv.DictWriter(f, fieldnames=campos)
            writer.writeheader()
            writer.writerows(empleados)
        print(f"Datos guardados en '{archivo}' correctamente.")


if __name__ == "__main__":
    main()