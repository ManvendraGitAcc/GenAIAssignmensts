import pandas as pd

marks = [78, 85, 90, 66, 72]
my_Series = pd.Series(marks)

#Adding 5 grace marks 
my_Series = my_Series + 5
print("After adding 5 \n", my_Series)

#Substracting 2 grace marks 
my_Series = my_Series - 2
print("After Susbtracting 2 \n", my_Series)

#multiply all marks by 1.05
my_Series = my_Series * 1.05
print("Multiply all marks by 1.05\n", my_Series)

#Divide all marks by 2
my_Series = my_Series/2
print("Divide by 2 \n", my_Series)