# Import numpy with the alias np
import numpy as np

# Generate a two-dimensional array
# filled with random floating point values in the rang 0 to 1,
# spread across 1000 rows and 10 columns
data = np.random.rand(1000,10)

# Write the contents of the array to a file with a custom header
np.savetxt("output.csv", data, header="val1,val2,val3,val4,val5,val6,val7,val8,val9,val10")