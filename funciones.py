# Importamos la librería a utilizar 
import requests

#FUNCION OBTENER PAIS
# Definimos la función para obtener los datos del país
def getPais(pais):
    # Definimos la url
    api_url = 'https://restcountries.com/v3.1/name/' + pais 

    try:
        # Hacemos un petición de tipo GET a la api de países 
        response = requests.get(api_url)

        # Parseamos la respuesta JSON a un diccionario de python
        data = response.json()

        # Buscamos los datos a imprimir
        nombre_oficial = data[0].get('name', {}).get('official')
        area = data[0].get('area')
        poblacion = data[0].get('population')
        continente = data[0].get('continents')[0]

        # Imprimimos algunos datos
        print("Este país es: " + nombre_oficial)
        print("Su área es: ", area)
        print("Su continente es: " + continente)
        print("Su población es de: ", poblacion)

    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error: {e}")
    except requests.exceptions.ConnectionError as e:
        print(f"Connection Error: {e}")
    except requests.exceptions.Timeout as e:
        print(f"Timeout Error: {e}")
    except requests.exceptions.RequestException as e:
        print(f"An unexpected error occurred: {e}")

# Llamamos a la función
getPais("Chi")

# #FUNCION CARGAR PAISES
# def cargarPaises():
#     paises = []
#     for nombre in lista_nombres:
#         try:
#             response = requests.get(f'https://restcountries.com/v3.1/name/{nombre}')
#             data = response.json()[0]
#             pais = {
#                 "nombre": data['name']['common'],
#                 "poblacion": data['population'],
#                 "superficie": data['area'],
#                 "continente": data['continents'][0]
#             }
#             paises.append(pais)
#         except Exception as e:
#             print(f"Error al cargar {nombre}: {e}")
#     return paises
