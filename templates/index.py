index_html = """
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