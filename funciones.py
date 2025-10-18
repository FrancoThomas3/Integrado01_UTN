import requests
import csv
import os

ARCHIVO_CSV = "paises.csv"

# Funciones para manejar el archivo CSV
def inicializar_csv():
    if not os.path.exists(ARCHIVO_CSV):
        with open(ARCHIVO_CSV, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["nombre", "poblacion", "superficie", "continente"])
        print("Archivo 'paises.csv' creado.")
# Función para guardar o actualizar un país en el CSV
def guardar_pais_csv(nombre, poblacion, superficie, continente):
    paises = []

    # Leer el contenido existente (si existe)
    if os.path.exists(ARCHIVO_CSV):
        with open(ARCHIVO_CSV, "r", newline="", encoding="utf-8") as f:
            lector = csv.DictReader(f)
            paises = list(lector)

    # Revisar si ya existe el país (comparación case-insensitive)
    encontrado = False
    for p in paises:
        if p["nombre"].lower() == nombre.lower():
            p["poblacion"] = str(poblacion)
            p["superficie"] = str(superficie)
            p["continente"] = continente
            encontrado = True
            break

    if not encontrado:
        paises.append({
            "nombre": nombre,
            "poblacion": str(poblacion),
            "superficie": str(superficie),
            "continente": continente
        })

    # Escribir de nuevo todo el contenido actualizado
    with open(ARCHIVO_CSV, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["nombre", "poblacion", "superficie", "continente"])
        writer.writeheader()
        writer.writerows(paises)
        
# Función principal para obtener datos del país desde la API
def getPais(pais):
    api_url = f'https://restcountries.com/v3.1/name/{pais}'

    try:
        response = requests.get(api_url, timeout=10)
        response.raise_for_status()  
        data = response.json()

        # Verificar que vinieron datos válidos
        if not data or not isinstance(data, list):
            print("No se recibieron datos válidos de la API.")
            return

        # Tomamos el primer resultado
        item = data[0]
        nombre_oficial = item.get('name', {}).get('official') or item.get('name', {}).get('common')
        area = item.get('area') or 0
        poblacion = item.get('population') or 0
        continentes = item.get('continents') or []
        continente = continentes[0] if continentes else ""

        # Mostrar datos en consola
        print("País encontrado:")
        print(f"Nombre: {nombre_oficial}")
        print(f"Área: {area} km²")
        print(f"Continente: {continente}")
        print(f"Población: {poblacion}\n")

        # Guardar en CSV (esta línea SÍ se ejecuta cuando la API responde OK)
        guardar_pais_csv(nombre_oficial, poblacion, area, continente)
        print("País guardado o actualizado en paises.csv")

    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error: {e}")
    except requests.exceptions.ConnectionError as e:
        print(f"Connection Error: {e}")
    except requests.exceptions.Timeout as e:
        print(f"Timeout Error: {e}")
    except requests.exceptions.RequestException as e:
        print(f"Error de petición: {e}")
    except (KeyError, IndexError, TypeError) as e:
        print("No se encontró información válida del país.", e)
        
# Función para reiniciar el archivo CSV       
def reiniciar_csv():
    with open(ARCHIVO_CSV, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["nombre", "poblacion", "superficie", "continente"])
    print("Archivo 'paises.csv' reiniciado correctamente (vacío con encabezados).")

# Ejemplo de uso
if __name__ == "__main__":
    inicializar_csv()

    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Buscar país y guardarlo")
        print("2. Reiniciar archivo CSV")
        print("3. Salir")
        opcion = input("Elegí una opción: ")

        if opcion == "1":
            nombre = input("🔎 Ingresá el nombre del país: ").strip()
            if nombre:
                getPais(nombre)
        elif opcion == "2":
            confirmar = input("⚠️ ¿Seguro que querés borrar todos los datos? (s/n): ")
            if confirmar.lower() == "s":
                reiniciar_csv()
        elif opcion == "3":
            print("👋 Saliendo del programa...")
            break
        else:
            print("❌ Opción inválida, intentá nuevamente.")
