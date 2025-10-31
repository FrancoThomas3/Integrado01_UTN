Gestión de Datos de Países – Trabajo Práctico Integrador (Programación I)
Universidad Tecnológica Nacional – Tecnicatura Universitaria en Programación (UTN)
 Cátedra: Programación I  2025
Alumno: Lautaro Ojeda - Franco Tarditi

 LINKS:
Docker del proyecto: https://hub.docker.com/r/lautroxi/paises-app
Video explicativo del proyecto: https://www.youtube.com/watch?v=Ew98iG_h2m8



Descripción del Proyecto
Este proyecto forma parte del Trabajo Práctico Integrador (TPI) de la asignatura Programación I, y tiene como propósito demostrar la aplicación de los conceptos fundamentales del lenguaje Python en el desarrollo de un sistema funcional.
El programa implementa un sistema de gestión de información de países mediante la lectura y manipulación de archivos CSV, permitiendo realizar operaciones de búsqueda, filtrado, ordenamiento y análisis estadístico.
La información procesada incluye el nombre del país, su población, superficie y continente.
El sistema fue desarrollado en Python 3, utilizando la librería Rich para mejorar la presentación visual de la interfaz en consola.


Estructura del Proyecto
gestion-paises/
 --- main.py              # Programa principal: menú e interacción con el usuario
 --- funciones.py         # Módulo auxiliar: lectura, filtrado, ordenamiento, estadísticas
 --- paises.csv           # Archivo de datos (dataset persistente)
 --- README.md            # Documento explicativo del proyecto
 --- informe.pdf          # Informe académico del TPI




Objetivos del Trabajo
* Aplicar estructuras de datos dinámicas (listas y diccionarios) para representar y manipular información.

* Desarrollar funciones modulares que realicen tareas específicas dentro del sistema.

* Implementar operaciones de búsqueda, filtrado, ordenamiento y cálculo de estadísticas.

* Garantizar la persistencia de datos mediante el manejo correcto de archivos CSV.

* Presentar los resultados de forma ordenada en consola mediante la librería Rich.

* Documentar el proceso con un informe teórico y un README profesional.



Instalación y Requisitos
Versión recomendada de Python: 3.9 o superior
Librería y API externa utilizada:
   * Rich
   * REST countries
Instalación:
pip install rich/request




Instrucciones de Ejecución
   1. Clonar o descargar el repositorio del proyecto.

   2. Verificar que el archivo paises.csv se encuentre en el mismo directorio que los archivos .py.

Ejecutar el archivo principal desde la terminal:


      3. python main.py
      4. Seleccionar las opciones del menú para realizar búsquedas, filtros, ordenamientos o generar estadísticas.
Descripción Funcional
El programa ofrece un menú principal que permite acceder a diferentes operaciones:
      * Buscar país: realiza búsquedas por coincidencia parcial o exacta dentro del archivo CSV.

      * Filtrar países: permite aplicar filtros por continente, rango de población o superficie.

      * Ordenar países: organiza los datos por nombre, población o superficie (ascendente o descendente).

      * Estadísticas globales: calcula y muestra países con mayor y menor población, promedios y distribución continental.

      * Reinicio del archivo CSV: permite vaciar el archivo de forma segura, previa confirmación.

El sistema valida las entradas del usuario, controla los errores comunes y muestra los resultados en tablas legibles gracias al uso de Rich.


Ejemplo de Ejecución
LISTA DE PAÍSES - 3 países
-------------------------------------------------
País        | Población     | Superficie | Continente
-------------------------------------------------
Argentina   | 45,376,763    | 2,780,400  | América
Brasil      | 213,993,437   | 8,515,767  | América
Japón       | 125,800,000   |   377,975  | Asia




Casos de Prueba
1. Búsqueda local:
Entrada: "arg"
Salida:  Argentina | 45,376,763 | 2,780,400 | América


2. Filtro por continente:
Entrada: América
Salida:  Argentina, Brasil, México, Canadá


3. Ordenamiento por superficie (mayor a menor):
1. Rusia
2. Canadá
3. China
4. Estados Unidos
5. Brasil


4. Estadísticas globales:
País más poblado: China (1,411,000,000)
País menos poblado: Uruguay (3,485,000)
Población promedio: 274,600,000
Superficie promedio: 3,012,000 km²
Distribución por continente: América 40%, Asia 35%, Europa 25%




Validaciones y Control de Errores
         * Verificación de formato correcto en el archivo CSV.

         * Control de búsquedas y filtros vacíos o con valores inválidos.

         * Prevención de sobrescritura accidental en el archivo de datos.

         * Manejo de excepciones mediante bloques try / except para evitar cierres inesperados.



Reflexión Final
El desarrollo del sistema permitió consolidar los conceptos fundamentales de la programación estructurada en Python, especialmente en lo relativo al manejo de listas, diccionarios, modularización y persistencia de datos.
El proyecto demostró la importancia de la planificación y la organización del código, así como del uso de herramientas de presentación y documentación profesional, como Rich y Markdown.
El trabajo también evidenció la relevancia de la documentación y del README como medio de comunicación técnica, garantizando la comprensión del proyecto incluso por parte de terceros.

