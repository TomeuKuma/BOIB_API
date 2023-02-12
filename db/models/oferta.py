from pydantic import BaseModel
from typing import Optional


class Offer(BaseModel):
    id: Optional[str]
    Fecha: str
    Entidad: str
    Resolucion: str
    HTML: str
