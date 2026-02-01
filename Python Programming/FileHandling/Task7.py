import os

prices = {"Mouse" : 500, "keyBoard" : 800, "Monitor" : 7000, "Pendrive" : 400, "camera" : 5000}

def CreateReport(discoutPer : int):
    file = open("discount_report.txt", "w")
    avgDisc = 0
    for key, val in prices.items():
        discPrice = val - (val * discoutPer)/100
        avgDisc = discoutPer + avgDisc
        file.write( key + "|" + str(val) + "|" + str(discPrice) + '\n')

    file.write("Total Items " + str(len(prices))+ '\n')
    file.write("Average discounted price " + str(avgDisc) + '\n')

    file.close()


def readFileLines():
    file = open("discount_report.txt", "r")
    while True:
        line = file.readline()
        if not line:
            # Reached EOF
            break
        # Process the line (e.g., print it)
        element = line.strip('\n').split('|')
        if len(element) > 1:
            print(element[0] + "  " + element[1] + "   " + element[2])
        else:
            print(element[0])
    file.close()

def UserInputHandler():
    discPer = int(input("Enter Discount Percentage ?  "))
    CreateReport(discPer)
    readFileLines()

UserInputHandler()