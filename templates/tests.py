import requests
import json

#data = '''[{"id":"63e7cb8689797c409dbe529f","Fecha":"2014-08-09","Entidad":"ESCUELA BALEAR DE ADMINISTRACIÓN PÚBLICA (EBAP)","Resolucion":"Resolución de la Consejera de Administraciones Públicas de 30 de julio de 2014, por la cual se aprueba la lista de aspirantes seleccionados del concurso para formar parte de una bolsa extraordinaria para cubrir, con carácter de interinidad, plazas vacantes del cuerpo facultativo técnico, escala sanitaria, especialidad ayudante técnico sanitario (ATS)/ diplomado universitario en enfermería (DUE) de la Administración especial de la Comunidad Autónoma de las Illes Balears, en la isla de Mallorca, convocado por la Resolución de 24 de abril de 2014 ","HTML":"https://www.caib.eshttps://intranet.caib.es/eboibfront/es/2014/10140/547089/resolucion-de-la-consejera-de-administraciones-pub"},{"id":"63e7cb8689797c409dbe52a0","Fecha":"2014-08-09","Entidad":"AYUNTAMIENTO DE SANT LLORENÇ DES CARDASSAR","Resolucion":"Aprobación de la clasificación definitiva de las personas aspirantes y consiguiente constitución de la bolsa de interinos de auxiliares administrativos/vas del Ayuntamiento de Sant Llorenç des Cardassar ","HTML":"https://www.caib.eshttps://intranet.caib.es/eboibfront/es/2014/10140/547191/aprobacion-de-la-clasificacion-definitiva-de-las-p"},{"id":"63e7cb9f4a664cc59f88c955","Fecha":"2014-08-14","Entidad":"ESCUELA BALEAR DE ADMINISTRACIÓN PÚBLICA (EBAP)","Resolucion":"Diligencia de la consejera de Administraciones Públicas de 6 de agosto de 2014, por la que se da publicidad a las modificaciones en las adjudicaciones de los puestos de trabajo del personal funcionario de la Administración de la Comunidad Autónoma de las Illes Balears, objeto del procedimiento convocado para su provisión (BOIB núm. 88, de 22 de junio de 2013), a raíz de la estimación de diversos recursos administrativos ","HTML":"https://www.caib.eshttps://intranet.caib.es/eboibfront/es/2014/10141/547414/diligencia-de-la-consejera-de-administraciones-pub"}]'''
#json_data = json.loads(data)
#for item in json_data:
#    print("id:", item["id"])
#    print("Fecha:", item["Fecha"])
#    print("Entidad:", item["Entidad"])
#    print("Resolucion:", item["Resolucion"])
#    print("HTML:", item["HTML"])

url = "http://127.0.0.1:8000/ofertasdb/"
response = requests.get(url)
print(1)
datos = json.loads(response.text)[0:2]
print(type(datos))
print(datos)
