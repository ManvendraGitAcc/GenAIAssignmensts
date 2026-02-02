def check_age(age):
    if age <= 0 or age > 120:
        raise Exception("Age must be between 1 and 120")
    print("Valid age")
    
try:
    age = int(input("Age ?? "))
    check_age(age)
except Exception as e:
    print(e)
    

