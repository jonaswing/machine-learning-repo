import pandas as pd
import numpy as np

student_data1 = pd.read_csv("student_results_2021.csv")
student_data2 = pd.read_csv("student_results_2022.csv")
student_data = student_data2.append(student_data1)

personal_data = pd.read_csv("student_personal.csv")
data_set = student_data.merge(personal_data, on="stud_id", how="left")

highest_mark_average = data_set["highest_mark"].mean()
data_set = data_set["highest_mark"].fillna(highest_mark_average)
data_set = data_set["name"].fillna("Not provided")
data_set = data_set.dropna()
data_set["birth_date"] = pd.to_datetime(data_set["birth_date"])
data_set.sort_values(by=["birth_date", "highest_mark"], inplace=True)

print("Average by class code:")
print(data_set.groupby(data_set="class_code").highest_mark.mean())
