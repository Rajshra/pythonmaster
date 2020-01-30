from demos.raw_sql.database_ops import DatabaseOpr
from demos.raw_sql.product_info import Product
import sys

if __name__ == '__main__':
    service = DatabaseOpr()
    service.create_table(False)

    p1 = Product(pid=113, pnm='Laptop', ppr=28382.34, pqty=3, pven='Flipkart')
    p2 = Product(pid=114, pnm='Mobile', ppr=22882.34, pqty=23, pven='Flipkart')


    service.add_product(p1)
    service.add_product(p2)

