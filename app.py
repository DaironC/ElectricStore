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

@app.route('/update/<id>')
def update(id):
    cur = conn.cursor()
    cur.execute("SELECT * from productos where id={0}".format(id))
    producto = cur.fetchall()
    return render_template('update_producto.html', producto=producto[0])

@app.route('/update_producto/<id>', methods=['POST'])
def update_producto(id):
    if request.method == 'POST':
        nombre = request.form['nombre']
        precio = request.form['precio']
        descripcion = request.form['descripcion']
        imagen = request.form['imagen']
        cur = conn.cursor()
        cur.execute("""
        UPDATE productos
        set nombre = '{0}',
            precio = '{1}',
            descripcion = '{2}',
            imagen = '{3}'
        where id = {4}
        """.format(nombre, precio, descripcion, imagen, id))
        cur.close()
    return redirect(url_for('store'))

@app.route('/delete/<id>')
def delete(id):
    cur = conn.cursor()
    cur.execute("DELETE from productos where id={0}".format(id))
    conn.commit()
    cur.close()
    return redirect(url_for('store'))



if __name__== '__main__':
    app.run(port=4100,debug=True)