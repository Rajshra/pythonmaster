


class Product:

    def __init__(self,pid,pnm,ppr,pqty,pven):
        self.prodId = pid
        self.prodName = pnm
        self.prodPrice = ppr
        self.prodQty = pqty
        self.prodVen = pven

    def __str__(self):
        return ''.join(['\n'+items[0]+" : "+str(items[1]) for items in self.__dict__.items()])
        #return ''.join(productinfo)

    '''
        productrepr = '\n'
        for key,val in self.__dict__.items():
            productrepr += "\n"+key +":"+str(val)+","
        return productrepr
    '''

    def __repr__(self):
        return str(self)


