import pandas as pd

students = {
    'Name' : ['Amit', 'Neha', 'Rahul', 'Sneha', 'Pooja'],
    'Marks' : [78, 85, 90, 66, 72],
    'Subject' : ['Math', 'Math', 'Science', 'Science', "Math"]
}

data = pd.DataFrame(students)

print("Info on dataframe  --- \n ", data.info())
print("Descibe on dataframe  --- \n ", data.describe())
print("head on dataframe  --- ", data.head())
print("tail on dataframe  --- ", data.tail())

data = data.sort_values(by='Marks')
print(data)

data = data.reset_index()
print(data)

#data.drop(columns=['index'])
#print(data)