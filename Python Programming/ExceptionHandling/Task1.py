#Safe Division Utiltity 

numerator = 0
denominator = 0

try:
    i1 = input("Numerator ? ")
    numerator =  int(i1)
except ValueError:
    print(f" {i1} is not a valid number")
else:
    try:
        i2 = input("Denominator ? ")
        denominator = int(i2)
    except ValueError:
        print(f" {i2} is not a valid number")
    else:
        try:
            result = numerator / denominator
            print(f"Result of {numerator}/{denominator} = {result}")
        except ZeroDivisionError:
            print("Denominator should not be Zero")
finally:
    print("Operation Complete")