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
from templates.table import table_html, best_html

router = APIRouter(prefix="/ofertasdb",
                   tags=["ofertasdb"],
                   responses={status.HTTP_404_NOT_FOUND: {"message": "No encontrado"}})


@router.get("/", response_model=list[Offer])
async def get_data():
    return offers_schema(db_client[COLLECTION_NAME].find())


@router.get("/html")
async def render_items():
    datos = db_client[COLLECTION_NAME].find().sort("URL_id", DESCENDING).limit(100)
    template = Template(best_html)
    html = template.render(datos=datos)
    return HTMLResponse(html)

