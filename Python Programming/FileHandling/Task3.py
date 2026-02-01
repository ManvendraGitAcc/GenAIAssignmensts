input_sales = [1200, 450, 980, 1500, 3000]
output_sales = []

def writeFile(FileName:str, data:list, seperator:chr):
    file = open(FileName, "w")
    for i in range(len(data)):
        file.write(str(data[i]))
        file.write(seperator)
    file.close()

def appendInFile(FileName:str, data:list, seperator:chr):
    file = open(FileName, "a")
    for i in range(len(data)):
        file.write(str(data[i]))
        file.write(seperator)
    file.close()

#readlines()
def readFileLines(FileName:str):
    file = open(FileName, "r")
    data = file.readlines()
    for i in range(len(data)):
        output_sales.append(int(data[i]))
    print(output_sales)
    file.close()

writeFile("sales_data.txt", input_sales, '\n')
appendInFile("sales_data.txt", [5000, 2500, 1700], '\n')
readFileLines("sales_data.txt")
