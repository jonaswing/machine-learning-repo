import cv2
import pandas as pd

student_data_1 = {'numbers': [1, 2, 3, 4, 5]}
student_data_2 = {'numbers': [6, 7, 8, 9, 10]}

# Create DataFrames
df1 = pd.DataFrame(student_data_1)
df2 = pd.DataFrame(student_data_2)

# Append and reset index
student_data = df2.append(df1, ignore_index=True)

print(student_data)