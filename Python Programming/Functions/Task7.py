prices = []

def add_price(prices_list, price):
    prices_list.append(price)

def get_average_price(prices_list):
    counts = len(prices_list)
    avg = 0
    for i in prices_list:
        avg = avg + prices_list[i]
    avg = avg / counts
    return avg

def get_max_price(prices_list):
    max = 0
    for i in prices_list:
        if max < prices_list[i]:
            max = prices_list[i]
    return max


while(1):
    print("1. Add Price")
    print("2. Show Average Price")
    print("3. Show Highest Price")
    print("4. Quit")
    try:
        ch = (input("Enter your choice --"))
        print(ch)
        choice = int(ch)
        if choice == 1:
            amount = int(input("Enter order amount -- "))
            add_price(prices, amount)

        elif choice == 2:
            print("Average Price -- " , get_average_price(prices))

        elif choice == 3:
            print("Maximum element -- " , get_max_price(prices))

        else:
            break
    except:
        print("Enter a valid choice")