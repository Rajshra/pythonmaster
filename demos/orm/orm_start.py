from demos.orm.orm_config import db,ProductInfo
from demos.orm.orm_db_ops import ProductPersist

db.create_all()

service = ProductPersist()

if __name__ == '__main__':

    prod =service.get_product(105)
    print(prod)
    #products =service.get_all_product()
    #print(products)
    '''
    p1 = ProductInfo(prodId=102,prodName='lappy',prodVen='Amazon',prodPrice=2883.34,prodQty=2)
    service.add_product(p1)
    p1 = ProductInfo(prodId=1022, prodName='lappy', prodVen='Amazon', prodPrice=2883.34, prodQty=2)
    service.add_product(p1)
    p1 = ProductInfo(prodId=102, prodName='lappy', prodVen='Amazon', prodPrice=2883.34, prodQty=2)
    service.add_product(p1)
    '''
