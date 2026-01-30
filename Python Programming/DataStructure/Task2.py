#List and Touples
#List containing 6 products
products = ["Monitor", "CPU", "Mouse", "HeadSet", "Docker", "Laptop"]
category = ["Display", "Machine", "Pointer", "Music", "Machine", "Display"]

categories_set = set(category) #this is the way to find unique element of a list 

print("Items in list are -- ")
for item in category:
    print(item)

print("Items in categories set are -- ")
for item in categories_set:
    print(item)

#adding duplicate items in set 
categories_set.add("Pointer")

print("Items in categories set are -- ")
for item in categories_set:
    print(item)

#checking for an item in set 
if "Display" in categories_set:
    print("Item Display is present in the set")

if "Tool" in categories_set:
    print("Item Tool is present in set")
else:
    print("Item is not present in the set")

