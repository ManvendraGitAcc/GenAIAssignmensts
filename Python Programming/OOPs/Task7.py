class Product:
    __name :str
    __price:float
    __category:str

    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, price):
        self.__price = price

    @property
    def category(self):
        return self.__category
    
    @category.setter
    def category(self, category):
        self.__category = category

        
    def getInfo(self):
        print(f"Name -- {self.name} Price -- {self.price} Category -- {self.category}")
    

class Inventory:
    products : list[Product]

    def __init__(self):
        self.products = []

    def add_product(self, product : Product) :
        self.products.append(product)

    def remove_product(self, name :str) :
        index = 0
        for i in range(len(self.products)):
            index += 1
            if self.products[i].name == name :
                break
        self.products.pop(index)

    def show_summary(self):
        for i in range(len(self.products)):
            self.products[i].getInfo()


class Store:
    store_name : str
    inventory : Inventory

    def __init__(self, storeName):
        self.store_name = storeName
        self.inventory = Inventory()

    def add_new_product(self):
        self.inventory.add_product(Product("Monitor", 40000, "Display"))
        self.inventory.add_product(Product("Phone", 4000, "Display"))
        self.inventory.add_product(Product("Mouse", 40000, "Pointer"))
        self.inventory.add_product(Product("Book", 250, "Stationary"))

    def remove_product(self):
        self.inventory.remove_product("Mouse")

    def show_summary(self):
        self.inventory.show_summary()

MyStore = Store("STORE1")
MyStore.add_new_product()
#MyStore.remove_product()
MyStore.show_summary()



    

