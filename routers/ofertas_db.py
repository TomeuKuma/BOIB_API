from fastapi import APIRouter, status
from datetime import datetime, timedelta
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
ten_days_ago = datetime.now() - timedelta(days=10)

@router.get("/", response_model=list[Offer])
async def users():
    return offers_schema(db_client[COLLECTION_NAME].find())

