#!/usr/bin/env python3
# -- coding: utf-8 --


import csv

def clasificar(p):
    if p < 70:
        return "Necesita Mejorar"
    elif p < 90:
        return "Cumple Expectativas"
    else:
        return "Sobresaliente"

def calcular_ponderado(c, prod, com, pun):
    return c * 0.30 + prod * 0.30 + com * 0.20 + pun * 0.20

def pedir_float(mensaje):
    while True:
        texto = input(mensaje).strip()
        try:
            v = float(texto)
            if 0 <= v <= 100:
                return v
            else:
                print("⚠️  Ingrese un valor entre 0 y 100.")
        except ValueError:
            print("⚠️  Valor no válido. Intente nuevamente (ejemplo: 85.5).")

def main():
    empleados = []
    print("=== SISTEMA DE EVALUACIÓN DE EMPLEADOS ===\n")

    # Solicitar cantidad de empleados
    while True:
        try:
            n = int(input("¿Cuántos empleados desea evaluar?: "))
            if n > 0:
                break
            else:
                print("⚠️  Ingrese un número mayor que cero.")
        except ValueError:
            print("⚠️  Ingrese un número válido.")

    print("\n--- INGRESO DE DATOS ---\n")

    for i in range(1, n + 1):
        print(f"Empleado {i} de {n}")
        emp_id = input("ID del empleado: ").strip()
        nombre = input("Nombre completo: ").strip()
        if nombre == "":
            nombre = "(sin nombre)"

        calidad = pedir_float("Puntaje Calidad (0-100): ")
        productividad = pedir_float("Puntaje Productividad (0-100): ")
        comunicacion = pedir_float("Puntaje Comunicación (0-100): ")
        puntualidad = pedir_float("Puntaje Puntualidad (0-100): ")

        total = calcular_ponderado(calidad, productividad, comunicacion, puntualidad)
        estado = clasificar(total)

        empleados.append({
            "id": emp_id,
            "nombre": nombre,
            "calidad": round(calidad, 2),
            "productividad": round(productividad, 2),
            "comunicacion": round(comunicacion, 2),
            "puntualidad": round(puntualidad, 2),
            "total": round(total, 2),
            "clasificacion": estado
        })

        print(f"✅ {nombre}: Total ponderado = {total:.2f} → {estado}\n")

    # Mostrar resumen
    print("\n=== RESUMEN DE EVALUACIONES ===")
    print("ID       Nombre                     Calidad   Productividad   Comunicacion   Puntualidad     Total      Clasificación")
    print("-" * 110)
    for e in empleados:
        print(f"{e['id']:<8} {e['nombre'][:25]:<25} {e['calidad']:8.2f} {e['productividad']:13.2f} {e['comunicacion']:13.2f} {e['puntualidad']:12.2f} {e['total']:8.2f} {e['clasificacion']:>16}")

    # Estadísticas
    prom_cal = sum(e["calidad"] for e in empleados) / n
    prom_prod = sum(e["productividad"] for e in empleados) / n
    prom_com = sum(e["comunicacion"] for e in empleados) / n
    prom_pun = sum(e["puntualidad"] for e in empleados) / n
    prom_total = sum(e["total"] for e in empleados) / n

    mayor = max(empleados, key=lambda x: x["total"])
    menor = min(empleados, key=lambda x: x["total"])

    print("\n=== ESTADÍSTICAS GENERALES ===")
    print(f"Empleados evaluados: {n}")
    print(f"Promedio Calidad:         {prom_cal:.2f}")
    print(f"Promedio Productividad:   {prom_prod:.2f}")
    print(f"Promedio Comunicación:    {prom_com:.2f}")
    print(f"Promedio Puntualidad:     {prom_pun:.2f}")
    print(f"Promedio Total Ponderado: {prom_total:.2f}")
    print(f"Mayor puntaje: {mayor['nombre']} ({mayor['total']:.2f})")
    print(f"Menor puntaje: {menor['nombre']} ({menor['total']:.2f})")

    # Exportar a CSV
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
        print(f"📂 Datos guardados en '{archivo}' correctamente.")

if _name_ == "_main_":
    main()