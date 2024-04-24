# import scipy.stats with the alias stats
import scipy.stats as stats

temps = [30,10,20,-6,32,12,27,28,13,15]
ice_creams = [40,4,12,0,47,5,21,25,7,12]

# Calculate Pearson's correlation coefficient
r, p = stats.pearsonr(temps, ice_creams)
print("Pearson's correlation coefficient: {0}\np-value:  {1}".format(r, p))