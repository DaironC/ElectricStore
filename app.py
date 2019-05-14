from flask import Flask, render_template,redirect,url_for, request

import pymysql #biblioteca myslq

conn = pymysql.connect('localhost','root','','bdelectricstore')

app = Flask(__name__)

@app.route('/')
def store():
    cur = conn.cursor()
    cur.execute("SELECT * FROM productos")
    producto = cur.fetchall()
    print(producto)
    return render_template('store.html', producto=producto)

@app.route('/agregar')
def agregar():
    return render_template('agregarProducto.html')

@app.route('/agregarProducto' ,methods=['POST'])
def agregarProducto():
    if request.method == "POST":
        nombre = request.form['nombre']
        precio = request.form['precio']
        descripcion = request.form['descripcion']
        imagen = request.form['imagen']

        #pintar en consola los productos de la bd
        print ("Nombre:" ,nombre)
        print ("Precio:" ,precio)
        print ("Descripcion:" ,descripcion)
        print ("Imagen:" ,imagen)

        #conexion a bd
        cur = conn.cursor()
        cur.execute("INSERT INTO productos(nombre,precio,descripcion,imagen)VALUES(%s,%s,%s,%s)",(nombre,precio,descripcion,imagen))
        conn.commit()
        cur.close()
    #Despues de Guardar redirige a la pagina store    
    return redirect(url_for('store'))


if __name__== '__main__':
    app.run(port=4100,debug=True)