import random
import numpy as np
import seaborn as sns

rem = 100
data = [1, 2, 1, 4, 2]

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
print("50%: " + str(np.percentile(simulateddata,50)))
print("85%: " + str(np.percentile(simulateddata,85)))
print("90%: " + str(np.percentile(simulateddata,90)))
