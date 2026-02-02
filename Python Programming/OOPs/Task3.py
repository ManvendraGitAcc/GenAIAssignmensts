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
    
class ElectronicProducts(Product):
    warranty_years : int

    def __init__(self, name, price, category, warranty):
        super().__init__(name, price, category)
        self.warranty_years = warranty

    def getInfo(self):
        super().getInfo()
        print(f"warranty_years -- {self.warranty_years}")


p1 = Product("Mouse", 400, "Pointer")
p2 = Product("Monitor", 40000, "Display")
p3 = ElectronicProducts("Phone", 35000, "Display", "4")

p1.getInfo()
p2.getInfo()
p3.getInfo()