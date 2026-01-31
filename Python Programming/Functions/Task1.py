def apply_discount(price, disc_perc = 5):
    discounted_price = 0
    if disc_perc > 60 :
         print("Invalid discount, Plase enter value less than 60")
         return
    discounted_price = price - ((price * disc_perc)/100)
    return discounted_price

finalPrice = apply_discount(1000,10)
print("10% on price 1000 --", finalPrice)

finalprice = apply_discount(500)
print("default discount 5% on price 500 --", finalPrice)

print("Response on 61 % discount  --")
finalPrice = apply_discount(5000, 61)
if finalPrice != None:
     print("default discount 61% on price 500 --", finalPrice)