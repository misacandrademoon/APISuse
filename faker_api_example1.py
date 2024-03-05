import requests

# URL base de Faker API
BASE_URL = 'https://fakerapi.it/api/v1/'

# Ejemplo de endpoint para generar datos de personas
endpoint = 'persons'

# Parámetros opcionales para especificar cuántos datos generar y el idioma
params = {
    '_locale': 'es_ES',  # idioma español
    '_quantity': 5  # cantidad de datos a generar
}

# Hacer la solicitud HTTP
response = requests.get(BASE_URL + endpoint, params=params)

# Verificar si la solicitud fue exitosa
if response.status_code == 200:
    # Mostrar los datos generados
    data = response.json()
    for person in data['data']:
        print(person)
else:
    print('Error al hacer la solicitud:', response.status_code)
