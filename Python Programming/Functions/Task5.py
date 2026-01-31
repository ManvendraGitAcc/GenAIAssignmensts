gt500 = lambda price : price > 500
lt500 = lambda price : price <= 500

prices = [100, 200, 400, 1200, 50, 2000, 850]

prices_gt500 = list(filter(gt500, prices))
prices_lt500 = list(filter(lt500,prices))

print(prices_gt500)
print(prices_lt500)