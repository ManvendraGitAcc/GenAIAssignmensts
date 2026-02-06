import numpy as np
sales = np.array([1200, 1500, 900, 2000, 1800, 1700, 1600])

print("Total weekly sales ",np.sum(sales))
print("Average daily sales ", np.average(sales))
print("Highest sales day ", np.where(sales == np.max(sales)))
print("Highest sales day ", np.where(sales == np.min(sales)))
print("Standard Deviation of sales",np.std(sales))
print("Days where sales were above avg", np.where(sales > np.average(sales)))