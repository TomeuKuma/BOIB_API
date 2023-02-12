
def offer_schema(offer) -> dict:
    return {"id": str(offer["_id"]),
            "Fecha": offer["Fecha"],
            "Entidad": offer["Entidad"],
            "Resolucion": offer["Resolucion"],
            "HTML": offer["HTML"]}


def offers_schema(offers) -> list:
    return [offer_schema(offer) for offer in offers]