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
# ...existing code...

def cargar_paises_csv():
    """
    Lee ARCHIVO_CSV y devuelve una lista de diccionarios normalizados con los datos de países.
    Returns:
        list: Lista de diccionarios con formato {nombre, poblacion, superficie, continente}
    """
    paises = []
    if not os.path.exists(ARCHIVO_CSV):
        return paises

    with open(ARCHIVO_CSV, "r", newline="", encoding="utf-8") as f:
        lector = csv.DictReader(f)
        for fila in lector:
            if not fila:
                continue
            # Normalizar datos
            nombre = (fila.get("nombre") or "").strip()
            pobl_raw = (fila.get("poblacion") or "").strip()
            sup_raw = (fila.get("superficie") or "").strip()
            continente = (fila.get("continente") or "").strip()

            # Convertir valores numéricos
            try:
                poblacion = int(str(pobl_raw).replace(".", "").replace(",", "")) if pobl_raw else 0
            except Exception:
                poblacion = 0
            try:
                superficie = int(str(sup_raw).replace(".", "").replace(",", "")) if sup_raw else 0
            except Exception:
                superficie = 0

            if nombre:
                paises.append({
                    "nombre": nombre,
                    "poblacion": poblacion, 
                    "superficie": superficie,
                    "continente": continente
                })
    return paises
# Funciones para buscar, filtrar, ordenar y estadísticas
def buscar_pais_local(paises, termino):
    if not termino:
        return []
    termino = termino.strip().lower()
    return [p for p in paises if termino in p["nombre"].lower()]

# Funciones para filtrar países
def filtrar_por_continente(paises, continente):
    if not continente:
        return []
    continente = continente.strip().lower()
    return [p for p in paises if p["continente"].lower() == continente]

# Funciones para filtrar países por rango
def filtrar_por_rango_poblacion(paises, min_p, max_p):
    try:
        min_v = int(min_p)
    except Exception:
        min_v = 0
    try:
        max_v = int(max_p)
    except Exception:
        max_v = 0
    if min_v > max_v:
        min_v, max_v = max_v, min_v
    return [p for p in paises if min_v <= p["poblacion"] <= max_v]

# Funciones para filtrar países por rango de superficie
def filtrar_por_rango_superficie(paises, min_s, max_s):
    try:
        min_v = int(min_s)
    except Exception:
        min_v = 0
    try:
        max_v = int(max_s)
    except Exception:
        max_v = 0
    if min_v > max_v:
        min_v, max_v = max_v, min_v
    return [p for p in paises if min_v <= p["superficie"] <= max_v]
# Funciones para ordenar países
def ordenar_paises(paises, clave, descendente=False):
    if clave not in ("nombre", "poblacion", "superficie"):
        raise ValueError("Clave de ordenamiento inválida")
    
    if clave == "nombre":
        return sorted(paises, key=lambda x: x["nombre"].lower(), reverse=descendente)
    return sorted(paises, key=lambda x: x.get(clave, 0) or 0, reverse=descendente)

# Funciones para estadísticas
def estadisticas(paises):
    stats = {
        "mayor_poblacion": None,
        "menor_poblacion": None,
        "promedio_poblacion": 0.0,
        "promedio_superficie": 0.0,
        "cantidad_por_continente": {}
    }
    
    if not paises:
        return stats
        
    # Mayor y menor población
    stats["mayor_poblacion"] = max(paises, key=lambda x: x["poblacion"])
    stats["menor_poblacion"] = min(paises, key=lambda x: x["poblacion"])
    
    # Promedios
    total = len(paises)
    stats["promedio_poblacion"] = sum(p["poblacion"] for p in paises) / total
    stats["promedio_superficie"] = sum(p["superficie"] for p in paises) / total
    
    # Conteo por continente
    for p in paises:
        cont = p["continente"] or "Desconocido"
        stats["cantidad_por_continente"][cont] = stats["cantidad_por_continente"].get(cont, 0) + 1
        
    return stats

# Función para mostrar países en formato tabular
def mostrar_paises(paises, limite=None):
    if not paises:
        print("No hay países para mostrar.")
        return
        
    if limite:
        paises = paises[:limite]
        
    # Calcular anchos de columna
    col_nombre = max(max(len(p["nombre"]) for p in paises), 6)
    col_pob = 10
    col_sup = 12
    
    # Imprimir encabezado
    print(f"{'NOMBRE'.ljust(col_nombre)} | {'POBLACION'.rjust(col_pob)} | {'SUPERFICIE'.rjust(col_sup)} | CONTINENTE")
    print("-" * (col_nombre + col_pob + col_sup + 15))
    
    # Imprimir datos
    for p in paises:
        print(f"{p['nombre'].ljust(col_nombre)} | {str(p['poblacion']).rjust(col_pob)} | "
              f"{str(p['superficie']).rjust(col_sup)} | {p['continente']}")

# Modificar el menú principal para incluir las nuevas funciones
if __name__ == "__main__":
    inicializar_csv()
    
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Buscar país y guardarlo")
        print("2. Buscar países en local")
        print("3. Mostrar estadísticas")
        print("4. Filtrar países")
        print("5. Ordenar países")
        print("6. Reiniciar archivo CSV") 
        print("7. Salir")
        
        opcion = input("Elegí una opción: ")
        
        if opcion == "1":
            nombre = input("Ingresá el nombre del país: ").strip()
            if nombre:
                getPais(nombre)
                
        elif opcion == "2":
            termino = input("Ingresá el término de búsqueda: ").strip()
            paises = cargar_paises_csv()
            resultados = buscar_pais_local(paises, termino)
            mostrar_paises(resultados)
            
        elif opcion == "3":
            paises = cargar_paises_csv()
            stats = estadisticas(paises)
            print("\nEstadísticas:")
            if stats["mayor_poblacion"]:
                print(f"Mayor población: {stats['mayor_poblacion']['nombre']}")
                print(f"Menor población: {stats['menor_poblacion']['nombre']}")
                print(f"Promedio población: {stats['promedio_poblacion']:.0f}")
                print(f"Promedio superficie: {stats['promedio_superficie']:.0f}")
                print("\nPaíses por continente:")
                for cont, cant in stats["cantidad_por_continente"].items():
                    print(f"  {cont}: {cant}")
                    
        elif opcion == "4":
            print("\n1. Filtrar por continente")
            print("2. Filtrar por rango de población")
            print("3. Filtrar por rango de superficie")
            sub_op = input("Elegí una opción: ")
            
            paises = cargar_paises_csv()
            if sub_op == "1":
                cont = input("Ingresá el continente: ")
                resultados = filtrar_por_continente(paises, cont)
            elif sub_op == "2":
                min_p = input("Población mínima: ")
                max_p = input("Población máxima: ")
                resultados = filtrar_por_rango_poblacion(paises, min_p, max_p)
            elif sub_op == "3":
                min_s = input("Superficie mínima: ")
                max_s = input("Superficie máxima: ")
                resultados = filtrar_por_rango_superficie(paises, min_s, max_s)
            else:
                print("Opción inválida")
                continue
            mostrar_paises(resultados)
            
        elif opcion == "5":
            print("\nOrdenar por:")
            print("1. Nombre")
            print("2. Población")
            print("3. Superficie")
            sub_op = input("Elegí una opción: ")
            
            claves = {"1": "nombre", "2": "poblacion", "3": "superficie"}
            if sub_op in claves:
                desc = input("¿Orden descendente? (s/n): ").lower() == "s"
                paises = cargar_paises_csv()
                ordenados = ordenar_paises(paises, claves[sub_op], desc)
                mostrar_paises(ordenados)
            else:
                print("Opción inválida")
                
        elif opcion == "6":
            confirmar = input("¿Seguro que querés borrar todos los datos? (s/n): ")
            if confirmar.lower() == "s":
                reiniciar_csv()
                
        elif opcion == "7":
            print("Saliendo del programa...")
            break
            
        else:
            print("Opción inválida, intentá nuevamente.")
 
