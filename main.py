# Primer inicio de Menu, base.
def main():
    print("=== SISTEMA DE GESTIÓN DE PAÍSES ===")
    print("1. Buscar país por nombre")
    print("2. Filtrar por continente")
    print("3. Salir")
    
    opcion = input("Seleccione una opción: ")
    print(f"Opción seleccionada: {opcion}")

if __name__ == "__main__":
    main()