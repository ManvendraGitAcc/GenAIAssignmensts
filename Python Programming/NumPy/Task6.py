import numpy as np
marks = np.array([78, 85, 90, 66, 72, 88, 95, 60])

print("Sorted array",marks.sort())
print("Percentile 25 ", np.percentile(marks, 25))
print("Percentile 50 ", np.percentile(marks, 50))
print("Percentile 75 ", np.percentile(marks, 75))
print("OR Percentile [25, 50, 75] ", np.percentile(marks, [25, 50, 75]))

print(f"Average mark = {np.average(marks)} and Count of students above avg marks = {marks[marks > np.average(marks)].size}")