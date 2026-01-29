import sys

products = ["Monitor", "CPU", "Mouse", "HeadSet", "Docker", "Laptop"]
category = ["Display", "Machine", "Pointer", "Music", "Machine", "Display"]

price_dict = {"Monitor" : 15000, 
              "CPU" : 12000, 
              "Mouse" : 500, 
              "HeadSet" : 2000, 
              "Docker" : 9000, 
              "Laptop" : 50000}

def AddElement(product:str, price:int):
    price_dict[product] = price 

def ModifyElement(product:str, price:int):
    if price_dict.get(product) != None: 
        price_dict[product] = price 
        return {price_dict[product], price }
    else:
        return None 

def calculateAvg():
    sum = 0
    count = 0
    average = 0
    for _,price in price_dict.items():
        sum = sum + price
        count += 1
    if count > 0 :
        average = sum / count
    return average

def findMaxMin():
    max = 0
    min = sys.maxsize
    for price in price_dict.values():
        if max < price:
            max = price
        if min > price:
            min = price
    return max, min

def printDictionary():
    for product, price in price_dict.items():
        print(product, "--", price)

print("Original Dictionary ---- ")
printDictionary()
AddElement("phone", 40000)

print("Dictionary After update ----")
printDictionary()

ModifyElement("Monitor", 60000)
print("Dictionary after Modification ----")
printDictionary()


print("Average price --- ", calculateAvg())
print("Max and Min values are ", findMaxMin())


