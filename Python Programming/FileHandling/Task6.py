import os

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
    filename = input("Enter file to read  ?  ")
    if os.path.exists(filename) == False:
        print("File not found Please check the file name")
        return
    readFileLines(filename)

UserInputHandler()