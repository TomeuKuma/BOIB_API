from fastapi import FastAPI
from routers import ofertas_db
from fastapi.responses import HTMLResponse
from templates.index import index_html

app = FastAPI()
app.include_router(ofertas_db.router)


@app.get("/")
async def main():
    return HTMLResponse(content=index_html)


# Inicia el server: uvicorn main:app --reload
# Detener el server: CTRL+C

# Documentación con Swagger: http://127.0.0.1:8000/docs
# Documentación con Redocly: http://127.0.0.1:8000/redoc
