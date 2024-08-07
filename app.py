from flask import Flask, render_template, redirect, request, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate   

#Instancia de Flask
app = Flask(__name__)

#config Alchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/efi' #aca se establece la cadena de conexion a la DB(en caso de tener, luego de los ":" va una contraseña)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app) 
migrate = Migrate(app, db)

from models import Tipo, Marca, Celular, Fabricante, Caracteristica, Stock, Proveedor, Accesorio

@app.route("/")
def home():
    return render_template('index.html')  

@app.route("/marca_list", methods=['POST', 'GET'])
def marcas():
    marcas = Marca.query.all() #Trae todas las marcas de la BD para pasar al front

    if request.method == 'POST':
        nombre = request.form['nombre']
        nuevaMarca = Marca(nombre=nombre)
        db.session.add(nuevaMarca)
        db.session.commit()
        return redirect(url_for('marcas'))

    return render_template('marca.html', marcasFront = marcas)  

@app.route("/marca/<id>/celulares")
def celularesPorMarca(id):
    marca = Marca.query.get_or_404(id)
    celulares = Celular.query.filter_by(marcaID=id)
    return render_template("celularesPorMarca.html", celulares=celulares, marca = marca)

@app.route("/marca/<id>/editar", methods=['POST', 'GET'])
def marcaEditar(id):
    marca = Marca.query.get_or_404(id)

    if request.method == 'POST':
        marca.nombre = request.form['nombre']
        db.session.commit()
        return redirect(url_for('marcas'))
    return render_template("marcaEdit.html", marca = marca)

@app.route("/tipo_list", methods=['POST', 'GET'])
def tipos():
    tipos = Tipo.query.all()

    if request.method == 'POST':
        nombre = request.form['nombre']
        nuevoTipo = Tipo(nombre=nombre)
        db.session.add(nuevoTipo)
        db.session.commit()
        return redirect(url_for('tipos'))
    
    return render_template('tipo.html', tipos = tipos)  

@app.route("/celulares", methods = ['POST', 'GET'])
def celulares():
    celulares = Celular.query.all()
    marcas = Marca.query.all()
    tipos = Tipo.query.all()
    print("---------")
    
    if request.method == 'POST':
        modelo = request.form['modelo']
        yearFabricacion = request.form['yearFabricacion']
        precio = request.form['precio']
        marca = request.form['marca']
        tipo = request.form['tipo']
        celularNuevo = Celular(
            modelo = modelo,
            yearFabricacion = yearFabricacion,
            precio = precio,
            marcaID = marca,
            tipoID = tipo,
        )
        db.session.add(celularNuevo)
        db.session.commit()
        return redirect(url_for('celulares'))

    return render_template(
        'celulares.html',
        celulares = celulares,
        marcas = marcas,
        tipos = tipos,
    )  
