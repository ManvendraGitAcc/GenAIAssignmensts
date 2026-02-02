sales = [1200, 450, 980, 1500, 3000]

def writeFile(FileName:str, data:list, seperator:chr):
    file = open(FileName, "w")
    for i in range(len(data)):
        file.write(str(data[i]))
        file.write(seperator)
    file.close()

def readFile(FileName:str):
    try:
        with open(FileName, 'r') as file:
            print(file.read())
    except FileNotFoundError:
        print("File not found")
    except PermissionError:
        print("Permission not found")
    finally:
        print("File operation attempted ")
    
writeFile("sales_data.txt",sales, '\n')
#readFile("product_data.txt")
readFile("sales_data.txt")