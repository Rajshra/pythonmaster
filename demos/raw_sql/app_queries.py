
    #db.create_all()
CREATE_TABLE = '''
        CREATE TABLE PROD_INFO(
            PROD_ID INT,
            PROD_NAME VARCHAR(50),
            PROD_VEN VARCHAR(50),
            PROD_PRICE FLOAT,
            PROD_QTY INT,
            PRIMARY KEY(PROD_ID)
        )
'''
    #db.session.add(model)
    #db.session.commit()
INSERT_PRODUCT_INFO = '''
    INSERT INTO PROD_INFO VALUES({},'{}','{}',{},{})
'''

    #dbprod = Product.query.filter_by(prodId=val).first()
    #if dbprod:
            #db.session.delete(dbprod)
            #db.session.commit()

DELETE_PRODUCT_INFO = '''
    DELETE FROM PROD_INFO WHERE PROD_ID={}
'''

#Product.query.all()

FETCH_ALL = '''
    SELECT * FROM PROD_INFO
'''

#dbprod = Product.query.filter_by(prodId=id).first()
FETCH_SINGLE_PRODUCT='''
    SELECT * FROM PROD_INFO WHERE PROD_ID={}
'''

    # dbprod = Product.query.filter_by(prodId=val).first()
    # if dbprod:
            # dbprod.field=newval
            # db.session.commit()

UPDATE_PRODUCT_INFO = '''
    UPDATE PROD_INFO SET PROD_NAME='{}', PROD_VEN='{}',PROD_QTY={},PROD_PRICE={}
    WHERE PROD_ID={}
'''

