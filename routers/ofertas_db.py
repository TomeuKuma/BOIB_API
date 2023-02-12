from fastapi import APIRouter, status, Request
from pymongo import DESCENDING
from datetime import datetime, timedelta
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from jinja2 import Template
from typing import List
import requests
import json
import sys
sys.path.append("..")
from db.models.oferta import Offer
from db.schemas.oferta import offer_schema, offers_schema
from db.client import db_client
from bson import ObjectId
from BOIB_API.config import DB_URL, DB_NAME, COLLECTION_NAME

router = APIRouter(prefix="/ofertasdb",
                   tags=["ofertasdb"],
                   responses={status.HTTP_404_NOT_FOUND: {"message": "No encontrado"}})

@router.get("/", response_model=list[Offer])
async def get_data():
    return offers_schema(db_client[COLLECTION_NAME].find())

#templates = Jinja2Templates(directory="templates")
#datos = [{"Fecha":"10", "Entidad":"entidad", "Resolucion":"resolucion", "HTML":"html"}, {"Fecha":"10", "Entidad":"entidad", "Resolucion":"resolucion", "HTML":"html"}]
#datos = [{"id":"63e7cb8689797c409dbe529f","Fecha":"2014-08-09","Entidad":"ESCUELA BALEAR DE ADMINISTRACIÓN PÚBLICA (EBAP)","Resolucion":"Resolución de la Consejera de Administraciones Públicas de 30 de julio de 2014, por la cual se aprueba la lista de aspirantes seleccionados del concurso para formar parte de una bolsa extraordinaria para cubrir, con carácter de interinidad, plazas vacantes del cuerpo facultativo técnico, escala sanitaria, especialidad ayudante técnico sanitario (ATS)/ diplomado universitario en enfermería (DUE) de la Administración especial de la Comunidad Autónoma de las Illes Balears, en la isla de Mallorca, convocado por la Resolución de 24 de abril de 2014 ","HTML":"https://www.caib.eshttps://intranet.caib.es/eboibfront/es/2014/10140/547089/resolucion-de-la-consejera-de-administraciones-pub"},{"id":"63e7cb8689797c409dbe52a0","Fecha":"2014-08-09","Entidad":"AYUNTAMIENTO DE SANT LLORENÇ DES CARDASSAR","Resolucion":"Aprobación de la clasificación definitiva de las personas aspirantes y consiguiente constitución de la bolsa de interinos de auxiliares administrativos/vas del Ayuntamiento de Sant Llorenç des Cardassar ","HTML":"https://www.caib.eshttps://intranet.caib.es/eboibfront/es/2014/10140/547191/aprobacion-de-la-clasificacion-definitiva-de-las-p"},{"id":"63e7cb9f4a664cc59f88c955","Fecha":"2014-08-14","Entidad":"ESCUELA BALEAR DE ADMINISTRACIÓN PÚBLICA (EBAP)","Resolucion":"Diligencia de la consejera de Administraciones Públicas de 6 de agosto de 2014, por la que se da publicidad a las modificaciones en las adjudicaciones de los puestos de trabajo del personal funcionario de la Administración de la Comunidad Autónoma de las Illes Balears, objeto del procedimiento convocado para su provisión (BOIB núm. 88, de 22 de junio de 2013), a raíz de la estimación de diversos recursos administrativos ","HTML":"https://www.caib.eshttps://intranet.caib.es/eboibfront/es/2014/10141/547414/diligencia-de-la-consejera-de-administraciones-pub"}]


@router.get("/html")
async def render_items():
    datos = db_client[COLLECTION_NAME].find().sort("URL_id", DESCENDING).limit(100)
    template = Template('''
        <style>
            table {
                font-family: arial, sans-serif;
                border-collapse: collapse;
                width: 100%;
            }
            td, th {
                border: 1px solid #dddddd;
                text-align: left;
                padding: 8px;
            }
    
            tr:nth-child(even) {
                background-color: #dddddd;
            }
        </style>
        <input type="text" id="myInput" onkeyup="myFunction()" placeholder="Buscar por texto">
        <table id="myTable">
        <thead>
            <tr>
                <th>Fecha</th>
                <th>Entidad</th>
                <th>Resolución</th>
                <th>HTML</th>
            </tr>
        </thead>
        <tbody>
        {% for dato in datos %}
            <tr>
                <td>{{ dato.Fecha }}</td>
                <td>{{ dato.Entidad }}</td>
                <td>{{ dato.Resolucion }}</td>
                <td><a href={{dato.HTML}}><button>Ver Link</button></a></td>
            </tr>
        {% endfor %}
        </tbody>
        </table>
        <script>
            function myFunction() {
                var input, filter, table, tr, td, i, txtValue;
                input = document.getElementById("myInput");
                filter = input.value.toUpperCase();
                table = document.getElementById("myTable");
                tr = table.getElementsByTagName("tr");
                for (i = 0; i < tr.length; i++) {
                    td = tr[i].getElementsByTagName("td");
                    for (j = 0; j < td.length; j++) {
                        txtValue = td[j].textContent || td[j].innerText;
                        if (txtValue.toUpperCase().indexOf(filter) > -1) {
                            tr[i].style.display = "";
                            break;
                        } else {
                            tr[i].style.display = "none";
                        }
                    }
                }
            }
        </script>
    ''')
    html = template.render(datos=datos)
    return HTMLResponse(html)

