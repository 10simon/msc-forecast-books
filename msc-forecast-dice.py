import random
import numpy as np
import seaborn as sns

data = [2, 3, 3, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 11, 11, 12]

num_simulations = 1000000
days = 31
simulateddata = [0]*num_simulations

for i in range(num_simulations):
    simulateddata[i] = random.choice(data)

sns_plot = sns.histplot(simulateddata)
sns_plot.figure.savefig("output.png")

