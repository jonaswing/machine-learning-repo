# import scipy.constants with the alias const
import scipy.constants as const

# Demonstrate a few of the constants and functions in
# scipy.constants
print("20 pounds = {0} kg".format(20 * const.pound))
print("3 weeks = {0} seconds".format(3 * const.week))
print("27 nautical miles = {0} m".format(27 * const.nautical_mile))
print("5 atmospheres = {0} pascals".format(5 * const.atmosphere))
print("10 parsecs = {0} light-years".format((10 * const.parsec) / const.light_year))
print("55 degrees Fahrenheit = {0} degrees Celsius".format(const.convert_temperature(55,"Fahrenheit", "Celsius")))