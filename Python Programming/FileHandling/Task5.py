def writeFile(FileName:str, data:list, seperator:chr):
    file = open(FileName, "w")
    for i in range(len(data)):
        file.write(str(data[i]))
        file.write(seperator)
    file.close()

def appendInFile(FileName:str, productname : str, price : int, seperator:chr):
    file = open(FileName, "a")
    file.write(productname + " " + seperator + " " + str(price))
    file.write('\n')
    file.close()

def readFileLines(FileName:str):
    file = open(FileName, "r")
    data = file.readlines()
    element = []
    print("-------------------------------------------")
    print("----Prodcut--------------------Price-------")
    print("-------------------------------------------")
    for i in range(len(data)):
        element = data[i].split('|')
        print(element[0] + "             " + str(int(element[1])))
        
    file.close()

def UserInputHandler():
    prdCount = 0
    while(prdCount < 3):
        try:
            product = input("Product Name ?  ")
            price = int(input("Price  ?  "))
            appendInFile("products.txt",product, price, '|')
            prdCount += 1
        except:
            print("input valid price")


UserInputHandler()
readFileLines("products.txt")