from flask import Flask, render_template,redirect,url_for,request
import pymysql #biblioteca myslq

conn = pymysql.connect('localhost','root','','bdelectricstore')

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('store.html')

@app.route('/agregar')
def agregar():
    return render_template('agregarProducto.html')

if __name__== '__main__':
    app.run(port=4100,debug=True)