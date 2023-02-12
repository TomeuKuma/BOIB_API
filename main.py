from fastapi import FastAPI
from routers import ofertas_db
from fastapi.responses import HTMLResponse

app = FastAPI()
app.include_router(ofertas_db.router)


# Url local: http://127.0.0.1:8000
#@app.get("/")
#async def root():
#    return "Ir a http://127.0.0.1:8000/ofertasdb"

@app.get("/")
async def main():
    content = """
<!DOCTYPE html>
<html>
  <head>
    <style>
      .button {
        background-color: #4CAF50;
        border: none;
        color: white;
        padding: 15px 32px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
      }
    </style>
  </head>
  <body>
    <h2>Accedeix a la base de dades</h2>
    <button class="button" onclick="location.href='http://127.0.0.1:8000/ofertasdb'">Mostrar dades</button>
    <button class="button" onclick="location.href='http://127.0.0.1:8000/ofertasdb/html'">Accedeix a la Web</button>
  </body>
</html>
    """
    return HTMLResponse(content=content)


# Inicia el server: uvicorn main:app --reload
# Detener el server: CTRL+C

# Documentación con Swagger: http://127.0.0.1:8000/docs
# Documentación con Redocly: http://127.0.0.1:8000/redoc
