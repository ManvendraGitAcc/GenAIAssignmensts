def factorial(num : int):
    if num < 0 :
        return 0
    if num == 1 or num == 0:
        return 1
    else:
        return num * factorial(num - 1)
    

print("factorial of 5 is " , factorial(5))
print("factorial of 0 is ",factorial(0))
print("factorial of -3 is ", factorial(-3))
