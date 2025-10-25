from rich.console import Console
from rich.panel import Panel
from rich.table import Table
import funciones

console = Console()

def mostrar_encabezado():
    """Limpia pantalla y muestra título"""
    console.clear()
    console.print(Panel.fit(
        "🎯 [bold cyan]GESTIÓN DE DATOS DE PAÍSES[/bold cyan]",
        subtitle="[bold green]TPI - Programación 1[/bold green]",
        style="bold magenta"
    ))

def mostrar_menu_principal():
    """Muestra todas las opciones disponibles"""
    mostrar_encabezado()
    
    table = Table(show_header=True, header_style="bold yellow", width=70)
    table.add_column("Opción", style="dim", width=8)
    table.add_column("Descripción", style="white")
    
    menu_items = [
        ("1", "🔍 Buscar país en API y guardar"),
        ("2", "📋 Buscar países en local"),
        ("3", "📊 Ver estadísticas"),
        ("4", "🌎 Filtrar países"),
        ("5", "📈 Ordenar países"),
        ("6", "🗑️ Reiniciar archivo CSV"),
        ("0", "🚪 Salir del sistema")
    ]
    
    for opcion, descripcion in menu_items:
        table.add_row(opcion, descripcion)
    
    console.print(table)
    console.print()

def mostrar_paises(paises, titulo="LISTA DE PAÍSES"):
    """Muestra países en tabla formateada"""
    if not paises:
        console.print("[red]❌ No hay países para mostrar[/red]")
        return
        
    table = Table(title=f"📋 {titulo} - {len(paises)} países")
    table.add_column("País", style="cyan", no_wrap=True)
    table.add_column("Población", style="green", justify="right")
    table.add_column("Superficie", style="blue", justify="right") 
    table.add_column("Continente", style="magenta")
    
    for pais in paises[:15]:
        table.add_row(
            pais['nombre'],
            f"{pais['poblacion']:,}",
            f"{pais['superficie']:,} km²",
            pais['continente']
        )
    
    console.print(table)
    
    if len(paises) > 15:
        console.print(f"[dim]... y {len(paises) - 15} países más[/dim]")

def mostrar_estadisticas(stats, total_paises):
    """Muestra estadísticas formateadas"""
    if not stats["mayor_poblacion"]:
        console.print("[yellow]⚠️ No hay datos para mostrar estadísticas[/yellow]")
        return
        
    console.print(Panel("📊 [bold cyan]ESTADÍSTICAS GLOBALES[/bold cyan]"))
    
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
    
    if stats["cantidad_por_continente"]:
        console.print(Panel("🌍 [bold cyan]DISTRIBUCIÓN POR CONTINENTE[/bold cyan]"))
        
        cont_table = Table(show_header=True, header_style="bold yellow")
        cont_table.add_column("Continente", style="magenta")
        cont_table.add_column("Cantidad", style="green", justify="center")
        cont_table.add_column("Porcentaje", style="blue", justify="center")
        
        for cont, cant in stats["cantidad_por_continente"].items():
            porcentaje = (cant / total_paises) * 100
            cont_table.add_row(cont, f"{cant} países", f"{porcentaje:.1f}%")
        
        console.print(cont_table)

def menu_filtrar(paises):
    """Menú para filtrar países"""
    console.print(Panel("🌎 [bold yellow]FILTRAR PAÍSES[/bold yellow]"))
    
    console.print("1. 🗺️ Por continente")
    console.print("2. 👥 Por rango de población") 
    console.print("3. 📏 Por rango de superficie")
    console.print("4. ↩️ Volver al menú principal")
    
    sub_op = input("\nSeleccione opción: ")
    
    if sub_op == "1":
        cont = input("Ingrese el continente: ").strip()
        if cont:
            resultados = funciones.filtrar_por_continente(paises, cont)
            mostrar_paises(resultados, f"Países de: {cont}")
        else:
            console.print("[red]❌ Debe ingresar un continente[/red]")
            
    elif sub_op == "2":
        min_p = input("Población mínima: ").strip()
        max_p = input("Población máxima: ").strip()
        if min_p or max_p:
            resultados = funciones.filtrar_por_rango_poblacion(paises, min_p, max_p)
            mostrar_paises(resultados, f"Población entre {min_p} y {max_p}")
        else:
            console.print("[red]❌ Debe ingresar al menos un valor[/red]")
            
    elif sub_op == "3":
        min_s = input("Superficie mínima (km²): ").strip()
        max_s = input("Superficie máxima (km²): ").strip()
        if min_s or max_s:
            resultados = funciones.filtrar_por_rango_superficie(paises, min_s, max_s)
            mostrar_paises(resultados, f"Superficie entre {min_s} y {max_s} km²")
        else:
            console.print("[red]❌ Debe ingresar al menos un valor[/red]")
            
    elif sub_op == "4":
        return
    else:
        console.print("[red]❌ Opción inválida[/red]")

def menu_ordenar(paises):
    """Menú para ordenar países"""
    console.print(Panel("📈 [bold yellow]ORDENAR PAÍSES[/bold yellow]"))
    
    console.print("1. 🔤 Por nombre (A-Z)")
    console.print("2. 👥 Por población (menor a mayor)")
    console.print("3. 📏 Por superficie (menor a mayor)")
    console.print("4. 🔤 Por nombre (Z-A)")
    console.print("5. 👥 Por población (mayor a menor)")
    console.print("6. 📏 Por superficie (mayor a menor)")
    console.print("7. ↩️ Volver al menú principal")
    
    sub_op = input("\nSeleccione opción: ")
    
    claves = {
        "1": ("nombre", False, "nombre (A-Z)"),
        "2": ("poblacion", False, "población (menor a mayor)"),
        "3": ("superficie", False, "superficie (menor a mayor)"),
        "4": ("nombre", True, "nombre (Z-A)"),
        "5": ("poblacion", True, "población (mayor a menor)"), 
        "6": ("superficie", True, "superficie (mayor a menor)")
    }
    
    if sub_op in claves:
        clave, descendente, descripcion = claves[sub_op]
        try:
            ordenados = funciones.ordenar_paises(paises, clave, descendente)
            mostrar_paises(ordenados, f"Ordenado por {descripcion}")
        except Exception as e:
            console.print(f"[red]❌ Error al ordenar: {e}[/red]")
            
    elif sub_op == "7":
        return
    else:
        console.print("[red]❌ Opción inválida[/red]")

def reiniciar_csv():
    """Pide confirmación para reiniciar el archivo CSV"""
    console.print(Panel("🗑️ [bold yellow]REINICIAR ARCHIVO CSV[/bold yellow]"))
    console.print("[red]⚠️ Esta acción borrará todos los datos guardados[/red]")
    
    confirmar = input("\n¿Está seguro? (s/n): ").lower()
    if confirmar == 's':
        funciones.reiniciar_csv()
        console.print("[green]✅ Archivo reiniciado correctamente[/green]")
    else:
        console.print("[yellow]Operación cancelada[/yellow]")

def main():
    """Función principal del programa"""
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
                mostrar_paises(resultados, f"Resultados para: '{termino}'")
                
            elif opcion == "3":
                console.print(Panel("📊 [bold yellow]ESTADÍSTICAS[/bold yellow]"))
                paises = funciones.cargar_paises_csv()
                stats = funciones.estadisticas(paises)
                mostrar_estadisticas(stats, len(paises))
                    
            elif opcion == "4":
                paises = funciones.cargar_paises_csv()
                menu_filtrar(paises)
                
            elif opcion == "5":
                paises = funciones.cargar_paises_csv()
                menu_ordenar(paises)
                
            elif opcion == "6":
                reiniciar_csv()
                
            elif opcion == "0":
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
>>>>>>> main
