from app import db

class Marca(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)

    #Este metodo logra que al acceder a un objeto de Marca nos muestre el nombre
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
    #Relacion directa con el otro objeto
    marca = db.relationship('Marca', backref = db.backref('celulares', lazy=True))
    tipo = db.relationship('Tipo', backref = db.backref('celulares', lazy=True))

    def __str__(self) -> str: 
        return self.nombreModelo

class Fabricante(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    paisOrigen = db.Column(db.String(50))
    descripcion = db.Column(db.Text)

    def __str__(self) -> str: 
        return self.nombre

class Caracteristica(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.Text, nullable=False)
    
    celularID = db.Column(db.Integer, db.ForeignKey('celular.id'), nullable=False)

    def __str__(self) -> str: 
        return self.nombre

class Stock(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    celularID = db.Column(db.Integer, db.ForeignKey('celular.id'), nullable=False)
    cantidad = db.Column(db.Integer)
    fechaModificacion = db.Column(db.DateTime)
    
    proveedorID = db.Column(db.Integer, db.ForeignKey('proveedor.id'), nullable=False)

    def __str__(self) -> str: 
        return self.cantidad

class Proveedor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    mail = db.Column(db.String(50))
    
    descripcionmarcasID = db.Column(db.Text)

    def __str__(self) -> str: 
        return self.nombre

class Accesorio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)

    #modeloID = 

    def __str__(self) -> str: 
        return self.nombre