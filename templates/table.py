table_html = '''
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
        <input type="text" id="myInput" onkeyup="myFunction()" placeholder="Filtra el contenido de la tabla según el texto introducido">
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
    '''

best_html = """
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        /* Estilos para la tabla */
        table {
            font-family: Arial, sans-serif;
            border-collapse: collapse;
            width: 100%;
            margin-bottom: 1em;
        }

        th, td {
            border: 1px solid #ddd;
            text-align: left;
            padding: 8px;
        }

        th {
            background-color: #4CAF50;
            color: white;
        }

        tr:nth-child(even) {
            background-color: #f2f2f2;
        }

        /* Estilos para el formulario */
        .search-form {
            margin-bottom: 1em;
        }

        .search-form input[type="text"] {
            width: 100%;
            padding: 12px 20px;
            margin: 8px 0;
            box-sizing: border-box;
            border: 2px solid #ccc;
            border-radius: 4px;
        }

        .search-form button {
            background-color: #4CAF50;
            color: white;
            padding: 12px 20px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }

        .search-form button:hover {
            background-color: #45a049;
        }

        /* Estilos generales */
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
        }

        .container {
            padding: 2em;
        }
    </style>
</head>
<body>
<div class="container">
    <form class="search-form">
        <input type="text" id="myInput" onkeyup="myFunction()" placeholder="Filtra el contenido de la tabla según el texto introducido">
        <button type="submit">Filtrar</button>
    </form>

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
            <td><a href={{dato.HTML}}>Ver Link</a></td>
        </tr>
        {% endfor %}
        </tbody>
    </table>
</div>

<script>
    function myFunction() {
        var input, filter, table, tr, td, i, j, txtValue;
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
</body>
</html>
"""