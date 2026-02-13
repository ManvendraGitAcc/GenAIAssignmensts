import pandas as pd

students = {
    'Name' : ['Amit', 'Neha', 'Rahul', 'Sneha', 'Pooja'],
    'Marks' : [78, 85, 90, 66, 72],
    'Subject' : ['Math', 'Math', 'Science', 'Science', "Math"]
}

data = pd.DataFrame(students)
print("First 3 rows of dataframe --- \n ", data.head(3))
print("Last 2 rows of dataframe  --- \n ", data.tail(2))

print("Shape of dataframe  --- ", data.shape)
print("Columns of dataframe  --- ", data.columns)
