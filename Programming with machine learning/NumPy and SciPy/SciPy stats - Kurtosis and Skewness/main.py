# import scipy.stats with the alias stats
import scipy.stats as stats
# import numpy with the alias np
import numpy as np

# Generate a random data set of 100 values in the range 0 to 100
data = np.random.randint(100,size=(100,1))

# Output the skewness and kurtosis of the data set
print("Skewness:  ", stats.skew(data))
print("Kurtosis:  ", stats.kurtosis(data))