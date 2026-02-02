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

    
p1 = Product("Mouse", 400, "Pointer")
p2 = Product("Monitor", 40000, "Display")

p1.getInfo()
p2.getInfo()

print("After discount" , p1.apply_discount(10))
print("After discount",  p2.apply_discount(20))