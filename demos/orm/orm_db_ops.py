
from demos.orm.orm_config import db,ProductInfo

class ProductPersist:

    def add_product(self,prod):
        dbprod = ProductInfo.query.filter_by(prodId=prod.prodId).first()
        if dbprod:
            print('Already Exist..!')
        else:
            db.session.add(prod)
            db.session.commit()
            print('Product Record inserted.')
    def delete_product(self,prodId):
        dbprod = ProductInfo.query.filter_by(prodId=prodId).first()
        if dbprod:
            db.session.delete(dbprod)
            db.session.commit()
            print('Record removed..!')
        else:
            print('No record avaiable so cannot remove..!')

    def get_product(self,prodId):
        return ProductInfo.query.filter_by(prodId=prodId).first()

    def get_all_product(self):
        return ProductInfo.query.all()

    def update_product(self,prod):
        dbprod = ProductInfo.query.filter_by(prodId=prod.prodId).first()
        if dbprod:
            dbprod.prodName = prod.prodName
            dbprod.prodQty = prod.prodQty
            dbprod.prodPrice = prod.prodPrice
            dbprod.prodVen = prod.prodVen
            db.session.commit()
            print('Product recored Updated..!')
        else:
            print('No product so cannot update..!')