import random
import numpy as np
import seaborn as sns

data = [1, 2, 1, 4, 2]

num_simulations = 100000
days = 31
simulateddata = [0]*num_simulations

for i in range(num_simulations):
    sample = [0]*days
    for j in range(days):
        sample[j] = random.choice(data)
        total_pages_read = sum(sample)
    simulateddata[i] = total_pages_read

sns_plot = sns.histplot(simulateddata)
sns_plot.figure.savefig("output.png")

#print(simulateddata)
print("50%: " + str(np.percentile(simulateddata,50)))
print("85%: " + str(np.percentile(simulateddata,15)))
print("90%: " + str(np.percentile(simulateddata,10)))

