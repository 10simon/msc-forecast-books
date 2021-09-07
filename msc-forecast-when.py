import random
import numpy as np
import seaborn as sns

rem = 25041
data = [2002, 3911, 758, 269, 0, 729, 1041, 1739, 585, 2494, 1200, 468, 3606]

num_simulations = 100000
simulateddata = [0]*num_simulations

for i in range(num_simulations):
    j = 0
    num_days = 0
    while j < rem:
        j = j+random.choice(data)
        num_days+=1
    simulateddata[i] = num_days

sns_plot = sns.histplot(simulateddata)
sns_plot.figure.savefig("output.png")

#print(simulateddata)
print(np.percentile(simulateddata,50))
print(np.percentile(simulateddata,85))
print(np.percentile(simulateddata,90))
print(np.percentile(simulateddata,30))

