class Product:
    __price:float
    category:str
    name :str

    def __init__(self, name, price, category):
        self.name = name
        self.__price = price
        self.category = category

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if price > 0:
            self.__price = price
        
    def getInfo(self):
        print(f"Name -- {self.name} Price -- {self.__price} Category -- {self.category}")

    def apply_discount(self, percentage):
        return self.__price - (self.__price * percentage)/100

    
p1 = Product("Mouse", 400, "Pointer")
p2 = Product("Monitor", 40000, "Display")

p1.getInfo()
p2.getInfo()

p1.getInfo()
p1.price = 0
p1.getInfo()
p1.price = 500
p1.getInfo()
print(p1.price)


print("After discount" , p1.apply_discount(10))
print("After discount" , p2.apply_discount(20))