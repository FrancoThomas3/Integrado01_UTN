"""
COMMIT 2: Mejora visual con tablas Rich
Tablas profesionales para mostrar países y estadísticas
"""

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
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
    """COMMIT 2: Menú principal mejorado"""
    mostrar_encabezado()
    
    console.print("[bold]Opciones disponibles:[/bold]")
    console.print("1. 🔍 Buscar país en API y guardar")
    console.print("2. 📋 Buscar países en local")
    console.print("3. 📊 Ver estadísticas")
    console.print("4. 🚪 Salir")
    console.print()

def mostrar_paises_rich(paises, titulo="LISTA DE PAÍSES"):
    """COMMIT 2: Mostrar países con tabla Rich profesional"""
    if not paises:
        console.print("[red]❌ No hay países para mostrar[/red]")
        return
        
    table = Table(title=f"📋 {titulo} - {len(paises)} países")
    table.add_column("País", style="cyan", no_wrap=True)
    table.add_column("Población", style="green", justify="right")
    table.add_column("Superficie", style="blue", justify="right") 
    table.add_column("Continente", style="magenta")
    
    # Mostrar máximo 15 países para no saturar
    for pais in paises[:15]:
        table.add_row(
            pais['nombre'],
            f"{pais['poblacion']:,}",
            f"{pais['superficie']:,} km²",
            pais['continente']
        )
    
    console.print(table)
    
    # Mostrar advertencia si hay más países
    if len(paises) > 15:
        console.print(f"[dim]... y {len(paises) - 15} países más (use filtros para ver más)[/dim]")

def mostrar_estadisticas_rich(stats, total_paises):
    """COMMIT 2: Mostrar estadísticas con formato Rich profesional"""
    if not stats["mayor_poblacion"]:
        console.print("[yellow]⚠️ No hay datos para mostrar estadísticas[/yellow]")
        return
        
    console.print(Panel("📊 [bold cyan]ESTADÍSTICAS GLOBALES[/bold cyan]"))
    
    # Tabla de estadísticas principales
    stats_table = Table(show_header=False, style="bold", width=60)
    stats_table.add_column("Métrica", style="cyan", width=25)
    stats_table.add_column("Valor", style="white")
    
    stats_table.add_row("Total de países", f"[green]{total_paises}[/green]")
    stats_table.add_row("País más poblado", 
                       f"[red]{stats['mayor_poblacion']['nombre']}[/red] ({stats['mayor_poblacion']['poblacion']:,})")
    stats_table.add_row("País menos poblado", 
                       f"[green]{stats['menor_poblacion']['nombre']}[/green] ({stats['menor_poblacion']['poblacion']:,})")
    stats_table.add_row("Población promedio", f"[yellow]{stats['promedio_poblacion']:,.0f} hab[/yellow]")
    stats_table.add_row("Superficie promedio", f"[blue]{stats['promedio_superficie']:,.0f} km²[/blue]")
    
    console.print(stats_table)
    
    # Tabla de países por continente
    if stats["cantidad_por_continente"]:
        console.print(Panel("🌍 [bold cyan]DISTRIBUCIÓN POR CONTINENTE[/bold cyan]"))
        
        cont_table = Table(show_header=True, header_style="bold yellow")
        cont_table.add_column("Continente", style="magenta")
        cont_table.add_column("Cantidad", style="green", justify="center")
        cont_table.add_column("Porcentaje", style="blue", justify="center")
        
        for cont, cant in stats["cantidad_por_continente"].items():
            porcentaje = (cant / total_paises) * 100
            cont_table.add_row(
                cont,
                f"{cant} países",
                f"{porcentaje:.1f}%"
            )
        
        console.print(cont_table)

def main():
    """Función principal - Versión mejorada con tablas Rich"""
    # Inicializar el archivo CSV
    funciones.inicializar_csv()
    
    while True:
        try:
            mostrar_menu_principal()
            opcion = input("Seleccione una opción: ")
            
            if opcion == "1":
                console.print(Panel("🔍 [bold yellow]BUSCAR EN API[/bold yellow]"))
                nombre = input("Ingrese nombre del país: ").strip()
                if nombre:
                    funciones.getPais(nombre)
                else:
                    console.print("[red]❌ Debe ingresar un nombre[/red]")
                    
            elif opcion == "2":
                console.print(Panel("📋 [bold yellow]BUSCAR EN LOCAL[/bold yellow]"))
                termino = input("Término de búsqueda: ").strip()
                paises = funciones.cargar_paises_csv()
                resultados = funciones.buscar_pais_local(paises, termino)
                # Mostrar resultados con Rich (nuevo)
                mostrar_paises_rich(resultados, f"Resultados para: '{termino}'")
                
            elif opcion == "3":
                console.print(Panel("📊 [bold yellow]ESTADÍSTICAS[/bold yellow]"))
                paises = funciones.cargar_paises_csv()
                stats = funciones.estadisticas(paises)
                # Mostrar stats con Rich (nuevo)
                mostrar_estadisticas_rich(stats, len(paises))
                    
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