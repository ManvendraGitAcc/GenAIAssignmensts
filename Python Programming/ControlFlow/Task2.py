def calculate_discount(order_amount:int):
    Final_amount = 0
    discounted = False
    discount = 0
    
    if order_amount >= 2000: # 15% discount
        Final_amount = order_amount - ((order_amount * 15 )/100)
        discount = 15
        discounted = True
    elif order_amount >= 1500 and order_amount < 2000 : # 10% discount
        Final_amount = order_amount - ((order_amount * 10 )/100)
        discount = 10
        discounted = True
    elif order_amount >= 1000 and order_amount < 1500 : # 7% discount
        Final_amount = order_amount - ((order_amount * 7 )/100)
        discount = 7
        discounted = True
    else:
        Final_amount = order_amount
    
    print(order_amount, " -- ",discount, " -- ", Final_amount)
    return Final_amount, discounted



orders = [1200, 2500, 800, 1750, 3000]
print("order_amount -> discount% -> final_amount")
totalRevenue = 0
discountedOrder = 0
for i in range(len(orders)):
    Revenue, discounted = calculate_discount(orders[i])
    totalRevenue = totalRevenue + Revenue
    if discounted:
        discountedOrder += 1

print("Total Revenue -- ", totalRevenue)
print("Discounted orders --", discountedOrder)