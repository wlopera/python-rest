# python-rest
Api Rest en Python

### Codigo a generar para API REST PYTHON:
```
------------------------------------------------------------------------------------
Aplicacion API REST - PYTHON
------------------------------------------------------------------------------------
------------------------------------------------------------------------------------

------------------------------------------------------------------------------------
Frameworks - Librerias:
------------------------------------------------------------------------------------
    - Framework FlasK: más ligero
      [https://flask.palletsprojects.com/en/2.3.x/installation/]
        - $ pip install Flask (pip administrador de instalaciones de Python)
------------------------------------------------------------------------------------
------------------------------------------------------------------------------------

------------------------------------------------------------------------------------
Instalaciones:
------------------------------------------------------------------------------------
    > $ python --version
        --> Python 3.11.0

    > $ pip --version
        --> pip 22.3 from C:\Python311\Lib\site-packages\pip (python 3.11)

    - pip install Flask --> Instalar Flask
        --> Collecting Flask
            ...
------------------------------------------------------------------------------------

------------------------------------------------------------------------------------
Crear data products.py (Arreglo JSON - data Dummy)
------------------------------------------------------------------------------------
products=[
    {"name":"laptop", "price":800, "quantity": 4},
    {"name":"mouse", "price":12, "quantity": 10},
    {"name":"monitor", "price":300, "quantity": 8},
    {"name":"keyboard", "price":25, "quantity": 15},
]
------------------------------------------------------------------------------------

------------------------------------------------------------------------------------
Crear Routes para peticiones API REST
------------------------------------------------------------------------------------
from flask import Flask
app=Flask(__name__)
@app.route('/ping')
def ping():
    return "Pong!"
------------------------------------------------------------------------------------

------------------------------------------------------------------------------------
Levantra servidor WEB
------------------------------------------------------------------------------------
''' Levanto servicios con debug para refrescar cambios automaticamente. puerto 4000 '''
if __name__=='__main__':
    app.run(debug=True, port=4000)
------------------------------------------------------------------------------------

------------------------------------------------------------------------------------
Correr App:
------------------------------------------------------------------------------------
willi@DESKTOP-M3MBPD8 MINGW64 /d/WorkSpace/WS_PYTHON/tutorial/Aplications/website
    ../src> python app.py
        * Serving Flask app 'app'
        * Debug mode: on
        WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
        * Running on http://127.0.0.1:4000
        Press CTRL+C to quit
        * Restarting with stat
        * Debugger is active!
        * Debugger PIN: 124-432-451

Probar en navegadar: http://127.0.0.1:4000/ping
------------------------------------------------------------------------------------

------------------------------------------------------------------------------------
JSON:
------------------------------------------------------------------------------------
from flask import Flask, jsonify (importarjsonify: uso de JSON)

 - Para prueba cambiar route de consulta:
    @app.route('/ping')
    def ping():
    return jsonify({"message": "Pong"})

    -> LLamada web: http://localhost:4000/ping
    // 20230510174037
    // http://localhost:4000/ping

    {
    "message": "Pong"
    }
------------------------------------------------------------------------------------
- API REST - Productos
------------------------------------------------------------------------------------
app.py:
------
...
@app.route('/products', methods=['GET'])
def getProducts():
    return jsonify(products)

------------------------------------------------------------------------------------

------------------------------------------------------------------------------------
- API REST - Producto por Nombre 
------------------------------------------------------------------------------------
app.py:
------
...
@app.route('/product/<string:product_name>')
def getProductByName(product_name):
    #data=list(filter(lambda product:product['name']==product_name, products))   # forma de cfiltrar data - lambda
    data= [product for product in products if product['name']==product_name]     # uso de for -
    if len(data)> 0:
        return jsonify({"product": data[0], "message":"Producto requerido", "status": "OK", "code": 200})
    else:
        return jsonify({"product": None, "message":"Producto no encontrado", "status": "Warning", "code": 300})
------------------------------------------------------------------------------------

------------------------------------------------------------------------------------
- API REST - Agregar Producto
------------------------------------------------------------------------------------
app.py:
------
...
@app.route('/products', methods=['POST'])
def addProduct():
    new_product= {"name": request.json['name'], "price": request.json['price'], "quantity": request.json['quantity']},
    products.append(new_product)
    return jsonify({"product": products, "message":"Producto agregado satisfactoriamente", "status": "OK", "code": 200})

------------------------------------------------------------------------------------


------------------------------------------------------------------------------------
- API REST - Modificar Producto
------------------------------------------------------------------------------------
app.py:
------
...
""" Rest PUT: Modificar producto  """ 
@app.route('/products/<string:product_name>', methods=['PUT'])
def editProduct(product_name):
    data= [product for product in products if product['name']==product_name]
    if len(data)>0:
        data[0]['name']=request.json['name']
        data[0]['price']=request.json['price']
        data[0]['quantity']=request.json['quantity']
        return jsonify({"product": products, "message":"Producto actualizado satisfactoriamente", "status": "OK", "code": 200})
    else:
        return jsonify({"product": None, "message":"Producto no actualizado", "status": "Warning", "code": 300})
------------------------------------------------------------------------------------

------------------------------------------------------------------------------------
- API REST - Borrar Producto
------------------------------------------------------------------------------------
app.py:
------
...
""" Rest DELETE: Borrar producto  """ 
@app.route('/products/<string:product_name>', methods=['DELETE'])
def deleteProduct(product_name):
    data= [product for product in products if product['name']==product_name]
    if len(data)>0:
        products.remove(data[0])
        return jsonify({"product": products, "message":"Producto eliminado satisfactoriamente", "status": "OK", "code": 200})
    else:
        return jsonify({"product": None, "message":"Producto no eliminado", "status": "Warning", "code": 300})
------------------------------------------------------------------------------------

------------------------------------------------------------------------------------
Uso de Pluggin Rest Client de VSCODE para probar consultar HTTP
------------------------------------------------------------------------------------
 - Creo archivo $__name__$.http
    > test.http

 - Agrego la petición URL - payload
        # Consultar productos
        GET http://localhost:4000/products HTTP/1.1

        # Agregar Producto
        # POST http://localhost:4000/products HTTP/1.1
        # Authorization: token xxx
        # content-type: application/json

        # {
        #     "name": "Printer",
        #     "price": 250,
        #     "quantity": 14
        # }


        # Modificar producto
        # PUT http://localhost:4000/products/laptop HTTP/1.1
        # Authorization: token xxx
        # content-type: application/json

        # {
        #     "name": "Laptop",
        #     "price": 225.67,
        #     "quantity": 140
        # }

        # Borrar producto
        #DELETE http://localhost:4000/products/monitor HTTP/1.1


 - send request (boton derecho del mouse sobre el archivo)
------------------------------------------------------------------------------------
```

## Salida
![Captura](https://github.com/wlopera/python-rest/assets/7141537/4785fc10-b646-4539-adc7-f330f7f05035)

* Consultar productos

![Captura1](https://github.com/wlopera/python-rest/assets/7141537/45b0662f-5e3f-441b-b467-42f73bab31ef)
![Captura2](https://github.com/wlopera/python-rest/assets/7141537/8a426e4d-6969-479f-b7a3-bd380fbf9ba5)

* Consultar producto por nombre

![Captura3](https://github.com/wlopera/python-rest/assets/7141537/baeced0c-a009-4825-b3d3-5889db518006)

* Agregar producto

![Captura4](https://github.com/wlopera/python-rest/assets/7141537/783dac63-b01d-4f00-8e6a-f1fcc8e43514)

![Captura5](https://github.com/wlopera/python-rest/assets/7141537/c3fa7b7d-18f0-4416-a648-bce36637ac6e)

* Borrar producto

![Captura6](https://github.com/wlopera/python-rest/assets/7141537/2dda0fa2-7ddb-4b61-bf6c-1720189de9c2)

## Agregar Templates y Servicio WEB
```
------------------------------------------------------------------------------------
Agregar Servicio Web:
------------------------------------------------------------------------------------
 Crear servidor web con routes a las paginas a mostrar
------------------------------------------------------------------------------------
from flask import Flask, render_template
import requests

web=Flask(__name__)

#---------------------- Routes
@web.route('/table')
def getProducts():
    response = requests.get("http://127.0.0.1:4000/products")
    headers=['Nombre', 'Precio', 'Cantidad']
    tableData=response.json()['products']

    return render_template(
        'table.html',
        headers=headers,
        tableData=tableData
    )
 
@web.route('/about')
def about():
    return render_template('about.html')

@web.route('/pythonweb')
def pythonWeb():
    return render_template('pythonWEB.html')

#---------------------- Levantar servidor web
if __name__=='__main__':
    web.run(debug=True, port=5000)
------------------------------------------------------------------------------------
Crear templates
------------------------------------------------------------------------------------
- layout.html
    > Cabecera de navegacion y sitio para inscustar html dinamicos
    ...
    <div class="container p-4 ">
        {% block content %} 
        {% endblock %}
    </div>

- table.html
{% extends "layout.html" %} {% block content %}
<div class="px-5 mx-5 mt-5 div-table">
  <h1>Productos</h1>
  <hr />

  <table class="table table-bordered table-striped table-hover">
    <thead>
      <tr>
        {% for header in headers %}
        <th>{{header}}</th>
        {% endfor %}
      </tr>
    </thead>

    <tbody>
      {% for row in tableData %}
      <tr>
        <td>{{row['name']}}</td>
        <td>{{row['price']}}</td>
        <td>{{row['quantity']}}</td>
      </tr>
      {% endfor %}
    </tbody>
  </table>
</div>
{% endblock %}

- pythonweb.html
{% extends "layout.html" %} 

{% block content %}    
    <div class="card text-center">
        <div class="card-header">
          APP Python
        </div>
        <div class="card-body">
          <h5 class="card-title">Servicio API Rest - WEB</h5>
          <p class="card-text">Aplicación para estudiar Python .</p>
          <img src="..\static\image\python.png" width="300" height="300" alt="python" loading="lazy">
        </div>
        <div class="card-footer text-muted">
          @wlopera - 2023
        </div>
      </div>
{% endblock %}
------------------------------------------------------------------------------------

- Agregar estilos porpios CSS  y  Bootstrap 4
- Agregar libreria para consulta de API (Client API)
    - pip install requests 

------------------------------------------------------------------------------------
------------------------------------------------------------------------------------
------------------------------------------------------------------------------------
```

### Salida
![Captura1](https://github.com/wlopera/python-rest/assets/7141537/cf1dfa4a-6bc9-4afb-b309-03a9dc57ce7d)
![Captura](https://github.com/wlopera/python-rest/assets/7141537/0fea425d-c7a1-4129-af9e-541333cc9a55)
![Captura2](https://github.com/wlopera/python-rest/assets/7141537/67f6f02d-1349-426a-bb19-e6cbe7c079f4)


