daily = [200, 150, 0, 400, 50, -1 , 300]

Running_total = 0
total_sales = 0

for i in range(len(daily)):
    if daily[i] == -1:
        break
    if daily[i] == 0:
        continue
    else:
        Running_total = Running_total + daily[i]
        print("Running Total is", Running_total)
        total_sales = total_sales + daily[i]

print("Total Sales -- ", total_sales)