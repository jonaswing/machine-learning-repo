import pandas as pd
import numpy as np

distance_covered = np.random.randint(5000, size=1001)
age = np.random.randint(18,65, size=1001)
prediction = np.random.rand(1001)


data = pd.DataFrame({'Distance Covered': distance_covered, 'Age': age, 'Prediction': prediction})

print(data)

data.to_csv('task_data.csv')
