gt300 = lambda price : price > 300
lt500 = lambda price : price <= 500
discPrice = lambda price : price - (price * 10)/100

def process_prices(prices):
    discounted_prices = list(map(discPrice, prices))
    filtered_prices = list(filter(gt300, prices))
    print(prices)
    print(discounted_prices)
    print(filtered_prices)

process_prices([100, 500, 900, 50, 750])
