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