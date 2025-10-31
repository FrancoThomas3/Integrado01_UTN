Gesti�n de Datos de Pa�ses � Trabajo Pr�ctico Integrador (Programaci�n I)
Universidad Tecnol�gica Nacional � Tecnicatura Universitaria en Programaci�n (UTN)
 C�tedra: Programaci�n I  2025
Alumno: Lautaro Ojeda - Franco Tarditi

 LINKS:
Docker del proyecto: https://hub.docker.com/r/lautroxi/paises-app
Video explicativo del proyecto: https://www.youtube.com/watch?v=Ew98iG_h2m8



Descripci�n del Proyecto
Este proyecto forma parte del Trabajo Pr�ctico Integrador (TPI) de la asignatura Programaci�n I, y tiene como prop�sito demostrar la aplicaci�n de los conceptos fundamentales del lenguaje Python en el desarrollo de un sistema funcional.
El programa implementa un sistema de gesti�n de informaci�n de pa�ses mediante la lectura y manipulaci�n de archivos CSV, permitiendo realizar operaciones de b�squeda, filtrado, ordenamiento y an�lisis estad�stico.
La informaci�n procesada incluye el nombre del pa�s, su poblaci�n, superficie y continente.
El sistema fue desarrollado en Python 3, utilizando la librer�a Rich para mejorar la presentaci�n visual de la interfaz en consola.


Estructura del Proyecto
gestion-paises/
 --- main.py              # Programa principal: men� e interacci�n con el usuario
 --- funciones.py         # M�dulo auxiliar: lectura, filtrado, ordenamiento, estad�sticas
 --- paises.csv           # Archivo de datos (dataset persistente)
 --- README.md            # Documento explicativo del proyecto
 --- informe.pdf          # Informe acad�mico del TPI




Objetivos del Trabajo
* Aplicar estructuras de datos din�micas (listas y diccionarios) para representar y manipular informaci�n.

* Desarrollar funciones modulares que realicen tareas espec�ficas dentro del sistema.

* Implementar operaciones de b�squeda, filtrado, ordenamiento y c�lculo de estad�sticas.

* Garantizar la persistencia de datos mediante el manejo correcto de archivos CSV.

* Presentar los resultados de forma ordenada en consola mediante la librer�a Rich.

* Documentar el proceso con un informe te�rico y un README profesional.



Instalaci�n y Requisitos
Versi�n recomendada de Python: 3.9 o superior
Librer�a y API externa utilizada:
   * Rich
   * REST countries
Instalaci�n:
pip install rich/request




Instrucciones de Ejecuci�n
   1. Clonar o descargar el repositorio del proyecto.

   2. Verificar que el archivo paises.csv se encuentre en el mismo directorio que los archivos .py.

Ejecutar el archivo principal desde la terminal:


      3. python main.py
      4. Seleccionar las opciones del men� para realizar b�squedas, filtros, ordenamientos o generar estad�sticas.
Descripci�n Funcional
El programa ofrece un men� principal que permite acceder a diferentes operaciones:
      * Buscar pa�s: realiza b�squedas por coincidencia parcial o exacta dentro del archivo CSV.

      * Filtrar pa�ses: permite aplicar filtros por continente, rango de poblaci�n o superficie.

      * Ordenar pa�ses: organiza los datos por nombre, poblaci�n o superficie (ascendente o descendente).

      * Estad�sticas globales: calcula y muestra pa�ses con mayor y menor poblaci�n, promedios y distribuci�n continental.

      * Reinicio del archivo CSV: permite vaciar el archivo de forma segura, previa confirmaci�n.

El sistema valida las entradas del usuario, controla los errores comunes y muestra los resultados en tablas legibles gracias al uso de Rich.


Ejemplo de Ejecuci�n
LISTA DE PA�SES - 3 pa�ses
-------------------------------------------------
Pa�s        | Poblaci�n     | Superficie | Continente
-------------------------------------------------
Argentina   | 45,376,763    | 2,780,400  | Am�rica
Brasil      | 213,993,437   | 8,515,767  | Am�rica
Jap�n       | 125,800,000   |   377,975  | Asia




Casos de Prueba
1. B�squeda local:
Entrada: "arg"
Salida:  Argentina | 45,376,763 | 2,780,400 | Am�rica


2. Filtro por continente:
Entrada: Am�rica
Salida:  Argentina, Brasil, M�xico, Canad�


3. Ordenamiento por superficie (mayor a menor):
1. Rusia
2. Canad�
3. China
4. Estados Unidos
5. Brasil


4. Estad�sticas globales:
Pa�s m�s poblado: China (1,411,000,000)
Pa�s menos poblado: Uruguay (3,485,000)
Poblaci�n promedio: 274,600,000
Superficie promedio: 3,012,000 km�
Distribuci�n por continente: Am�rica 40%, Asia 35%, Europa 25%




Validaciones y Control de Errores
         * Verificaci�n de formato correcto en el archivo CSV.

         * Control de b�squedas y filtros vac�os o con valores inv�lidos.

         * Prevenci�n de sobrescritura accidental en el archivo de datos.

         * Manejo de excepciones mediante bloques try / except para evitar cierres inesperados.



Reflexi�n Final
El desarrollo del sistema permiti� consolidar los conceptos fundamentales de la programaci�n estructurada en Python, especialmente en lo relativo al manejo de listas, diccionarios, modularizaci�n y persistencia de datos.
El proyecto demostr� la importancia de la planificaci�n y la organizaci�n del c�digo, as� como del uso de herramientas de presentaci�n y documentaci�n profesional, como Rich y Markdown.
El trabajo tambi�n evidenci� la relevancia de la documentaci�n y del README como medio de comunicaci�n t�cnica, garantizando la comprensi�n del proyecto incluso por parte de terceros.

