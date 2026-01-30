order_amount = 0
try:
    order_amount = int(input("Please input order amount? -- "))
except:
    print("Not a valid input")


Final_amount = 0
if order_amount >= 2000: # 15% discount
    Final_amount = order_amount - ((order_amount * 15 )/100)
elif order_amount >= 1500 and order_amount < 2000 : # 10% discount
    Final_amount = order_amount - ((order_amount * 10 )/100)
elif order_amount >= 1000 and order_amount < 1500 : # 7% discount
    Final_amount = order_amount - ((order_amount * 7 )/100)
else:
    Final_amount = order_amount

tax = (Final_amount * 5) / 100

print("Sub Total -- ", Final_amount)
print("Tax -- ", tax)
print("Final Total --", Final_amount + tax)

