"""
COMMIT 1: Estructura básica del menú con Rich
Integración inicial con las funciones existentes
"""

from rich.console import Console
from rich.panel import Panel
import funciones

console = Console()

def mostrar_encabezado():
    """Muestra el encabezado bonito del sistema"""
    console.clear()
    console.print(Panel.fit(
        "🎯 [bold cyan]GESTIÓN DE DATOS DE PAÍSES[/bold cyan]",
        subtitle="[bold green]TPI - Programación 1[/bold green]",
        style="bold magenta"
    ))

def mostrar_menu_principal():
    """COMMIT 1: Menú principal básico con Rich"""
    mostrar_encabezado()
    
    console.print("[bold]Opciones disponibles:[/bold]")
    console.print("1. 🔍 Buscar país en API y guardar")
    console.print("2. 📋 Buscar países en local")
    console.print("3. 📊 Ver estadísticas")
    console.print("4. 🚪 Salir")
    console.print()

def main():
    """Función principal - Versión inicial"""
    funciones.inicializar_csv()
    
    while True:
        try:
            mostrar_menu_principal()
            opcion = input("Seleccione una opción: ")
            
            if opcion == "1":
                console.print(Panel("🔍 [bold yellow]BUSCAR EN API[/bold yellow]"))
                nombre = input("Ingrese nombre del país: ").strip()
                if nombre:
                    # Usar la función de tu compañero que conecta con la API
                    funciones.getPais(nombre)
                else:
                    console.print("[red]❌ Debe ingresar un nombre[/red]")
                    
            elif opcion == "2":
                console.print(Panel("📋 [bold yellow]BUSCAR EN LOCAL[/bold yellow]"))
                termino = input("Término de búsqueda: ").strip()
                # Cargar países desde CSV (función de tu compañero)
                paises = funciones.cargar_paises_csv()
                # Buscar en local (función de tu compañero)
                resultados = funciones.buscar_pais_local(paises, termino)
                # Mostrar resultados (función de tu compañero)
                funciones.mostrar_paises(resultados)
                
            elif opcion == "3":
                console.print(Panel("📊 [bold yellow]ESTADÍSTICAS[/bold yellow]"))
                paises = funciones.cargar_paises_csv()
                stats = funciones.estadisticas(paises)
                # Mostrar stats básicas (versión simple por ahora)
                if stats["mayor_poblacion"]:
                    console.print(f"[cyan]País más poblado:[/cyan] {stats['mayor_poblacion']['nombre']}")
                    console.print(f"[cyan]País menos poblado:[/cyan] {stats['menor_poblacion']['nombre']}")
                    console.print(f"[cyan]Población promedio:[/cyan] {stats['promedio_poblacion']:,.0f} hab")
                    console.print(f"[cyan]Total de países:[/cyan] {len(paises)}")
                else:
                    console.print("[yellow]⚠️ No hay datos para mostrar estadísticas[/yellow]")
                    
            elif opcion == "4":
                console.print(Panel.fit("[green]¡Gracias por usar el sistema! 👋[/green]", style="bold green"))
                break
            else:
                console.print("[red]❌ Opción inválida[/red]")
            
            input("\n⏎ Presione Enter para continuar...")
            
        except KeyboardInterrupt:
            console.print("\n\n[yellow]⚠️ Programa interrumpido por el usuario[/yellow]")
            break
        except Exception as e:
            console.print(f"[red]❌ Error inesperado: {e}[/red]")
            input("\n⏎ Presione Enter para continuar...")

if __name__ == "__main__":
    main()