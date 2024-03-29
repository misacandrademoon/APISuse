import requests

# URL base de Faker API
BASE_URL = 'https://fakerapi.it/api/v1/'

# Endpoint para generar datos de productos
endpoint = 'products'

# Parámetros opcionales para especificar cuántos datos generar
params = {
    '_quantity': 4  # cantidad de productos a generar
}

# Hacer la solicitud HTTP
response = requests.get(BASE_URL + endpoint, params=params)

# Verificar si la solicitud fue exitosa
if response.status_code == 200:
   
       # Mostrar los datos generados dl primer producto
    data = response.json()
    for i, product in enumerate(data['data']):
        if i >= 1:
            break
        print(product)
       
else:
    print('Error al hacer la solicitud:', response.status_code)
