from app import db

class Marca(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)

    def __str__(self) -> str:
        return self.nombre
    
class Tipo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)

    def __str__(self) -> str:
        return self.nombre
    
class Celular(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    modelo = db.Column(db.String(50), nullable=False)
    yearFabricacion = db.Column(db.Integer)
    precio = db.Column(db.Integer)

    #Pertenece a
    marcaID = db.Column(db.Integer, db.ForeignKey('marca.id'), nullable=False)
    tipoID = db.Column(db.Integer, db.ForeignKey('tipo.id'), nullable=False)

    #Relacion directa con el optro objeto
    marca = db.relationship('Marca', backref = db.backref('celulares', lazy=True))
    tipo = db.relationship('Tipo', backref = db.backref('celulares', lazy=True))