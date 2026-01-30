products = ["Monitor", "CPU", "Mouse", "HeadSet", "Docker", "Laptop", "earphone"]
category = ["Display", "Machine", "Pointer", "Music", "Machine", "Display", "Music"]

price_dict = {"Monitor" : 15000, 
              "CPU" : 12000, 
              "Mouse" : 500, 
              "HeadSet" : 2000, 
              "Docker" : 9000, 
              "Laptop" : 50000,
              "earphone" : 4000}

catalog = []
category_to_product = {"" : [] }

def populate_catalog():
    for item,price in price_dict.items():
        index = products.index(item)
        catalog.append((item, price, category[index]))

def categorytoProduct():
    for item in catalog: #item is a tuple of (productName, price, category)
        if category_to_product.get(item[2]) == None:
            category_to_product[item[2]] = [item[0]]
        else:
            category_to_product[item[2]].append(item[0])


def printMaxProdcutsCategory():
    maxProductsCount = 0
    category = ""
    for item,value in category_to_product.items():
        if maxProductsCount < len(value):
            maxProductsCount = len(value)
            category = item
    print(category_to_product[category])
        
populate_catalog()
print(catalog)

categorytoProduct()
print(category_to_product)

printMaxProdcutsCategory()



