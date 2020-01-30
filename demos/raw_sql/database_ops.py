from demos.raw_sql.app_queries import *
import pymysql
from demos.raw_sql.product_info import Product

def get_database_connection():
    return pymysql.connect('localhost','root','root','sample')

class DatabaseOpr:

    def create_table(self,use_old=True):

        if not use_old:
            try:
                conn = get_database_connection()
                channel = conn.cursor()
                channel.execute('DROP TABLE PROD_INFO')
                conn.commit()
                channel.close()
                print("EXISTING TABLE AND DATA REMOVED")
            except:
                pass

        try:
            conn = get_database_connection()
            channel = conn.cursor()
            channel.execute(CREATE_TABLE)
            conn.commit()
            channel.close()
            print("Product Table Created")
        except :
            print('Table already exist..')

    def add_product(self,prod):
        if type(prod)==Product:
            conn = get_database_connection()
            channel = conn.cursor()
            sql = INSERT_PRODUCT_INFO.format(prod.prodId,prod.prodName,prod.prodVen,prod.prodPrice,prod.prodQty)
            print(sql)
            channel.execute(sql)
            conn.commit()
            channel.close()
            print("Product Record Added..!")
        else:
            print("Invalid product..!")

    def update_product(self,prod):
        pass

    def delete_product(self,prodId):
        pass

    def get_product(self,prodId):
        pass

    def get_all_product(self):
        pass
