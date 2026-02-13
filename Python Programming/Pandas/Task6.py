import pandas as pd

students = {
    'Name' : ['Amit', 'Neha', 'Rahul', 'Sneha', 'Pooja'],
    'Marks' : [78, 85, 90, 66, 72],
    'Subject' : ['Math', 'Math', 'Science', 'Science', "Math"]
}

data = pd.DataFrame(students)

print('Students who scored more than 75 marks \n', data[data['Marks'] > 75] )

print('Students belonging to subject math \n', data[data['Subject'] == 'Math'] )

print('Students who scored more than avg marks \n', data[data['Marks'] > data['Marks'].mean()])

print('Students who failed \n', data[data['Marks'] < 70])