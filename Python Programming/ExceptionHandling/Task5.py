#Bill calculator with Error Handling

cart = []

def printBill():
    total = 0
    for i in range(len(cart)):
        total = total + cart[i]
    print("Total items ===",len(cart))
    print("total Bill ====", total)

while(1):
    inp = input("Enter prices or 'q' to complete ? ")
    if inp == 'q':
        break
    try:
        value = float(inp)
        if value < 0:
            raise Exception("Price is negative")
        cart.append(value)
    except ValueError:
        print("Invalid Input")
    except Exception as e:
        print(e)


printBill()


