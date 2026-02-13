import pandas as pd

students = {
    'Name' : ['Amit', 'Neha', 'Rahul', 'Sneha', 'Pooja'],
    'Marks' : [78, 85, 90, 66, 72],
    'Subject' : ['Math', 'Math', 'Science', 'Science', "Math"]
}

data = pd.DataFrame(students)

print('Average marks per subject \n', data.groupby('Subject')['Marks'].mean())
print('Number of students per subject \n', data.groupby('Subject').count())
print('Maximum marks per subject \n', data.groupby('Subject').max())