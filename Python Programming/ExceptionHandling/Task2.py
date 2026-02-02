#Bill calculator with Error Handling

prices = [120, 350, 'abc', 500, -200, 800]
total = 0
for i in range(len(prices)):
    try:
        if type(prices[i]) is not int:
            raise TypeError
        elif prices[i] < 0 :
            raise ValueError(f"{prices[i]}, Negative price not allowed")
        total = total + prices[i]
    except TypeError:
        print(f"{prices[i]} is not a valid number")
    except ValueError as e:
        print(e)

print("Running Total is ", total)