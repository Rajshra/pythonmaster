from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:root@localhost/sample'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db = SQLAlchemy(app)



class Product(db.Model):
    prodId = db.Column('prod_id',db.Integer(),primary_key=True)
    prodName = db.Column('prod_name',db.String(100))
    prodVen = db.Column('prod_ven',db.String(100))
    prodPrice = db.Column('prod_price',db.Float())
    prodQty = db.Column('prod_qty',db.Integer())

    def __str__(self):
       return f'''\n
        ProductId : {self.prodId},
        ProductName: {self.prodName},
        ProductPrice : {self.prodPrice},
        ProductQty : {self.prodQty},
        ProductVendor : {self.prodVen}'''

    def __repr__(self):
        return str(self)

db.create_all()