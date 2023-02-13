from fastapi import APIRouter, status, Request
from pymongo import DESCENDING
from fastapi.responses import HTMLResponse
from jinja2 import Template
import sys
sys.path.append("..")
from db.models.oferta import Offer
from db.schemas.oferta import offer_schema, offers_schema
from db.client import db_client
from config import DB_URL, DB_NAME, COLLECTION_NAME

router = APIRouter(prefix="/ofertasdb",
                   tags=["ofertasdb"],
                   responses={status.HTTP_404_NOT_FOUND: {"message": "No encontrado"}})

@router.get("/", response_model=list[Offer])
async def get_data():
    return offers_schema(db_client[COLLECTION_NAME].find())

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

