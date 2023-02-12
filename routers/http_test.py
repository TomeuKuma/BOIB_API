import requests

url = "http://127.0.0.1:8000/ofertasdb/"

response = requests.get(url)

if response.status_code == 200:
    datos = response.json()
    for dato in datos:
        print(dato["Fecha"], dato["Entidad"], dato["Resolucion"], dato["HTML"])
else:
    print("Ha ocurrido un error al realizar la petición")
