#List and Touples
#List containing 6 products
products = ["Monitor", "CPU", "Mouse", "HeadSet", "Docker", "Laptop"]

#tuple sample product 
sample_product = ("Monitor", 12000, "Small") #product name , price , category

#printing second and last element of the products list
print("Second Product of the list is " + products[1])
print("Last Product of the list is " + products[-1])

#append 2 new productes in list
products.append("ear-phone")
products.append("phone")

#print all elements all elements of the list 
for i in range(len(products)):
    print("product [",i,"]", products[i])

#convert list into tuple and convert back to list 
sampleList = list(sample_product)
sampleList[1] = 15000
sample_product = tuple(sampleList)

print(sample_product)