import pandas as pd

the_list = [1, 2, 3, 4, 5, 6, 7]
the_series = pd.Series(the_list, index =  ["a", "b", "c", "d", "e", "f", "g"])
print(the_series)