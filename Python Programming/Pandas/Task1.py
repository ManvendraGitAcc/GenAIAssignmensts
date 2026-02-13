import pandas as pd

marks = [78, 85, 90, 66, 72]
my_Series = pd.Series(marks)

print(my_Series )
print('index    ', my_Series.index)
print('value    ',my_Series.values)
print('datatype  ',my_Series.dtype)

print(my_Series[0])
print(my_Series.tail(2))