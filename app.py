from flask import Flask, render_template, redirect, request

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate   


app = Flask(__name__)
#config Alchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/efi' #aca se establece la cadena de conexion a la DB
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models import Tipo, Marca

@app.route("/")
def home():
    return render_template('index.html')  

@app.route("/marca_list", methods=['POST', 'GET'])
def marcas():
    marcas = Marca.query.all()

    if request.method == 'POST':
        nombre = request.form['nombre']
        nuevaMarca = Marca(nombre=nombre)
        db.session.add(nuevaMarca)
        db.session.commit()
        return render_template('marca.html', marcas = marcas)

    return render_template('marca.html', marcas = marcas)  

@app.route("/tipo_list")
def tipos():
    tipos = Tipo.query.all()
    return render_template('tipo.html', tipos = tipos)  

@app.route("/celulares")
def vehiculos():
    return render_template('celulares.html')  
