import pandas as pd

marks = [78, 85, 90, 66, 72]
my_Series = pd.Series(marks)

#Maximum marks 
print("\n Maximum marks  ", my_Series.max())

#Minimum marks
print("\n Minimum marks ", my_Series.min())

#Sum of marks
print("\n Sum of marks ", my_Series.sum())

#Mean of marks
print("\n Mean of marks ", my_Series.mean())

print("Count of Students having marks > 70 ==> ", my_Series[my_Series.apply(lambda x : x > 70)].count())