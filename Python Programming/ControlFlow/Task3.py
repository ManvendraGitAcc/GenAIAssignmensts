def calculate_discount(order_amount:int):
    Final_amount = 0
    discount = 0
    
    if order_amount >= 2000: # 15% discount
        Final_amount = order_amount - ((order_amount * 15 )/100)
        discount = 15
    elif order_amount >= 1500 and order_amount < 2000 : # 10% discount
        Final_amount = order_amount - ((order_amount * 10 )/100)
        discount = 10
    elif order_amount >= 1000 and order_amount < 1500 : # 7% discount
        Final_amount = order_amount - ((order_amount * 7 )/100)
        discount = 7
    else:
        Final_amount = order_amount
    
    print(order_amount, " -- ",discount, " -- ", Final_amount)
    return Final_amount

orders = []
while(1):
    print("1. Add order amount to a running list")
    print("2. Show all orders and total after applying discounts")
    print("3. Quit")
    try:
        choice = int(input("Enter your choice --"))
        if choice == 1:
            amount = int(input("Enter order amount -- "))
            orders.append(amount)

        elif choice == 2:
            print("order_amount -> discount% -> final_amount")
            totalRevenue = 0

            for i in range(len(orders)):
                Revenue = calculate_discount(orders[i])
                totalRevenue = totalRevenue + Revenue
            print("Total Revenue -- ", totalRevenue)

        else:
            break
    except:
        print("Enter a valid choice")