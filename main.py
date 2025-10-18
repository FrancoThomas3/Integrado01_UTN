"""
Trabajo Integrador - Gestión de Datos de Países
"""

def mostrar_menu_principal():
    """Muestra el menú principal del sistema"""
    print("\n" + "="*50)
    print("      SISTEMA DE GESTIÓN DE PAÍSES")
    print("="*50)
    print("1. Buscar país por nombre")
    print("2. Filtrar por continente")
    print("3. Filtrar por rango de población")
    print("4. Filtrar por rango de superficie")
    print("5. Ordenar países")
    print("6. Ver estadísticas")
    print("0. Salir")
    print("-"*50)

def main():
    """Función principal del programa"""
    print("Iniciando sistema de gestión de países...")
    
    while True:
        mostrar_menu_principal()
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            print("Función de búsqueda por nombre - En desarrollo")
        elif opcion == "2":
            print("Función de filtro por continente - En desarrollo")
        elif opcion == "3":
            print("Función de filtro por población - En desarrollo")
        elif opcion == "4":
            print("Función de filtro por superficie - En desarrollo")
        elif opcion == "5":
            print("Función de ordenamiento - En desarrollo")
        elif opcion == "6":
            print("Función de estadísticas - En desarrollo")
        elif opcion == "0":
            print("¡Gracias por usar el sistema!")
            break
        else:
            print("Opción inválida. Intente nuevamente.")
        
        input("\nPresione Enter para continuar...")

if __name__ == "__main__":
    main()