gst = lambda price : (price + (0.18 * price))
#discPrice = lambda price, disc : price - (price * disc)/100

prices = [100, 250, 400, 1200, 50]
prices_with_gst = list(map(gst, prices))


print("lsit of prices",prices)
print("After gst prices", prices_with_gst)