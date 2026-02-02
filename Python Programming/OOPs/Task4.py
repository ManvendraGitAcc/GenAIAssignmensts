class Product:
    name :str
    price:float
    category:str

    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category
        
    def getInfo(self):
        print(f"Name -- {self.name} Price -- {self.price} Category -- {self.category}")

    def apply_discount(self, percentage):
        return self.price - (self.price * percentage)/100
    
class Laptop(Product):
    def getInfo(self):
        print("This is laptop class --")
        super().getInfo()

class Mobile(Product):
    def getInfo(self):
        print("This is Mobile class --")
        super().getInfo()

products = list()

def AddProducts(obj:Product):
    products.append(obj)

def printProductsInfo():
    for i in range(len(products)):
        products[i].getInfo()

AddProducts(Product("Mouse",400,"Pointer"))
AddProducts(Mobile("iPhone","140000","Mobile"))
AddProducts(Laptop("hp",150000,"Laptop"))
AddProducts(Mobile("Samsung","140000","Mobile"))
AddProducts(Laptop("Dell",150000,"Laptop"))

printProductsInfo()
