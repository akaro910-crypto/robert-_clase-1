#Sistema de Registro y Análisis de Libros - Biblioteca Municipal
# Funciones del sistema

def ingresar_libros():
    
    libros = []
    cantidad = int(input("Ingrese la cantidad de títulos (libros diferentes) a registrar: "))

    for i in range(cantidad):
        print(f"\nIngresando datos del libro {i + 1}:")

        # Ingreso de datos y validaciones
        while True:
            isbn = input("Código ISBN (único y alfanumérico): ").strip()
            if isbn and all(libro["isbn"] != isbn for libro in libros):
                break
            print("ISBN inválido o repetido. Intente nuevamente.")

        titulo = input("Título del libro: ").strip()
        genero = input("Género (Ficción, No-Ficción, Ciencia, Historia, etc.): ").strip()

        while True:
            try:
                precio = float(input("Precio de reposición (en soles): "))
                if precio > 0:
                    break
                else:
                    print("El precio debe ser mayor a 0.")
            except ValueError:
                print("Ingrese un valor numérico válido.")

        while True:
            try:
                stock = int(input("Cantidad de copias en stock: "))
                if stock >= 0:
                    break
                else:
                    print("El stock no puede ser negativo.")
            except ValueError:
                print("Ingrese un valor entero válido.")

        # Estructura del libro (diccionario)
        libro = {
            "isbn": isbn,
            "titulo": titulo,
            "genero": genero,
            "precio": precio,
            "stock": stock
        }

        libros.append(libro)

    return libros


def calcular_estadisticas(libros):
    
   
    valor_total = 0
    valor_por_genero = {}
    valores_individuales = []

    for libro in libros:
        valor_libro = libro["precio"] * libro["stock"]
        valor_total += valor_libro
        valores_individuales.append((libro["titulo"], valor_libro))

        # Acumular por género
        if libro["genero"] in valor_por_genero:
            valor_por_genero[libro["genero"]] += valor_libro
        else:
            valor_por_genero[libro["genero"]] = valor_libro

    # Determinar género con mayor valor
    genero_mayor_valor = max(valor_por_genero, key=valor_por_genero.get)

    # Libro con mayor y menor valor
    libro_mayor = max(valores_individuales, key=lambda x: x[1])
    libro_menor = min(valores_individuales, key=lambda x: x[1])

    estadisticas = {
        "valor_total": valor_total,
        "genero_mayor_valor": genero_mayor_valor,
        "libro_mayor": libro_mayor,
        "libro_menor": libro_menor
    }

    return estadisticas


def generar_reporte(libros):
    
    print("\n==============================")
    print("REPORTE DE INVENTARIO")
    print("==============================\n")

    for libro in libros:
        valor_total_titulo = libro["precio"] * libro["stock"]
        print(f"ISBN: {libro['isbn']}")
        print(f"Título: {libro['titulo']}")
        print(f"Género: {libro['genero']}")
        print(f"Precio de reposición: S/ {libro['precio']:.2f}")
        print(f"Stock disponible: {libro['stock']}")
        print(f"Valor total del título: S/ {valor_total_titulo:.2f}")
        print("-" * 35)

    # Mostrar estadísticas
    stats = calcular_estadisticas(libros)
    print("\n===== ESTADÍSTICAS =====")
    print(f"Valor total de la colección: S/ {stats['valor_total']:.2f}")
    print(f"Género con mayor valor en inventario: {stats['genero_mayor_valor']}")

    # ==============================
# Programa principal
# ==============================

def main():
    print("=====================================")
    print("SISTEMA DE REGISTRO DE LIBROS")
    print("=====================================\n")

    libros = ingresar_libros()
    generar_reporte(libros)


if __name__ == "__main__":
    main()


