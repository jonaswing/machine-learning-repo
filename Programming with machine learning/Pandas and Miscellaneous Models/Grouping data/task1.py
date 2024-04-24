import pandas as pd
import numpy as np

data = {
    "course_code": ["PR", "DP", "ML", "DP", "ML", "DP", "ET", "ML", "DP", "SW",
                    "PR", "DP", "PR", "OC", "PR", "DP", "ML", "PR", "DP", "DP"],
    "score": [80,70,60,50,40,30,90,70,59,67,56,98,67,54,56,24,17,22,44,66]
}

data = pd.DataFrame(data)

something = data.groupby(by='course_code').score.mean()

print("Score mean by groups: \n", something)

scores_mean = data['score'].mean()
print("Score mean: ", scores_mean)

scores_std = data['score'].std()
print("Score std: ", scores_std)
