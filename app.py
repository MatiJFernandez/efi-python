from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate   



app = Flask(__name__)
#config Alchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/efi' #aca se establece la cadena de conexion a la DB
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

@app.route("/")
def home():
    return render_template('index.html')  

@app.route("/vehiculos")
def vehiculos():
    return render_template('vehiculos.html')  
