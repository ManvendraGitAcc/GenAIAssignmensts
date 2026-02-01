sales = [1200, 450, 980, 1500, 3000]

def writeFile(FileName:str, data:list, seperator:chr):
    file = open(FileName, "w")
    for i in range(len(data)):
        file.write(str(data[i]))
        file.write(seperator)
    file.close()

def readFile(FileName:str):
    file = open(FileName, "r")
    print(file.read())
    file.close()

writeFile("sales_data.txt",sales, '\n')
readFile("sales_data.txt")
writeFile("sales_data.txt",sales, ',')
readFile("sales_data.txt")
