gst = lambda price : (price + (0.18 * price))
discPrice = lambda price, disc : price - (price * disc)/100

def genrate_bill(price):
    print("---- Bill ---")
    print("Price   ", price)
    print("After 5% Disc   ", discPrice(price,5))
    print("After GSt ", gst(discPrice(price,5)))

print(gst(100))
genrate_bill(100)