# import scipy.stats with the alias stats
import scipy.stats as stats
# import numpy with the alias np
import numpy as np

under_eighteens = np.random.randint(180,size=(10,1))
eighteens_and_up = np.random.randint(120, size=(10,1))

t_stat, p = stats.ttest_ind(under_eighteens,eighteens_and_up)
# For two-tailed test to determine if the means of the two sets are not equal
print("t-stat: {0}\np-value: {1}".format(t_stat, p))
# For a left-tailed test to determine if the number of minutes for the under_eighteens is higher
print("t-stat: {0}\np-value: {1}".format(t_stat, p / 2))