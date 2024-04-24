from matplotlib import pyplot as plt

fig, ax = plt.subplots()
# Change the font size to 22 and set the figure to 19.20 by 10.80 inches
plt.rcParams.update({"font.size": 22, "figure.figsize": [19.20, 10.80]})
# Change the font weight to bold.
plt.rcParams["font.weight"] = "bold"
# Remove the Figure's frame.
fig.frameon = False


plt.show()

