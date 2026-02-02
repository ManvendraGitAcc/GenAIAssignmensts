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

    def __str__(self):
        return "Product(%s, %s, %s)" % (self.name, self.price, self.category)

    def __add__(self, other):
        return self.price + other.price
    
p1 = Product("Mobile", 140000, "Display")
p2 = Product("Book", 800, "Stationary")

print(str(p1))
print(str(p2))
print(p1 + p2)
print(p1.__add__(p2))
    

