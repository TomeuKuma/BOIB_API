import requests
import json

url = "http://127.0.0.1:8000/ofertasdb/"
response = requests.get(url)
if response.status_code == 200:
    data = response.text
    json_data = json.loads(data)
    print(type(json_data))
    print(json_data[0:5])
    #for item in json_data:
    #    print("id:", item["id"])
    #    print("Fecha:", item["Fecha"])
    #    print("Entidad:", item["Entidad"])
    #    print("Resolucion:", item["Resolucion"])
    #    print("HTML:", item["HTML"])
else:
    print("Ha ocurrido un error al realizar la petición")
