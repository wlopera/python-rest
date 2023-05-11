from flask import Flask, jsonify, request
from products import products

app=Flask(__name__)

""" Rest GET: Las routes por defecto son GET """ 
@app.route('/ping')
def ping():
    return jsonify({"message": "Pong"})

""" Rest GET: Las routes por defecto son GET """ 
@app.route('/products', methods=['GET'])
def getProducts():
    return jsonify({"products": products, "message":"Lista de productos"})

""" Rest GET:  Consulta por nombre de producto""" 
@app.route('/products/<string:product_name>')
def getProductByName(product_name):
    #data=list(filter(lambda product:product['name']==product_name, products))
    data= [product for product in products if product['name']==product_name]
    if len(data)> 0:
        return jsonify({"product": data[0], "message":"Producto requerido", "status": "OK", "code": 200})
    else:
        return jsonify({"product": None, "message":"Producto no encontrado", "status": "Warning", "code": 300})

""" Rest POST: Agregar producto  """ 
@app.route('/products', methods=['POST'])
def addProduct():
    new_product= {"name": request.json['name'], "price": request.json['price'], "quantity": request.json['quantity']},
    products.append(new_product)
    return jsonify({"product": products, "message":"Producto agregado satisfactoriamente", "status": "OK", "code": 200})

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

""" Rest DELETE: Borrar producto  """ 
@app.route('/products/<string:product_name>', methods=['DELETE'])
def deleteProduct(product_name):
    data= [product for product in products if product['name']==product_name]
    if len(data)>0:
        products.remove(data[0])
        return jsonify({"product": products, "message":"Producto eliminado satisfactoriamente", "status": "OK", "code": 200})
    else:
        return jsonify({"product": None, "message":"Producto no eliminado", "status": "Warning", "code": 300})

''' Levanto servicios con debug para refrescar cambios automaticamente. puerto 4000 '''
if __name__=='__main__':
    app.run(debug=True, port=4000)