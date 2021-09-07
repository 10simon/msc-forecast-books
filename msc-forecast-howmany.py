import random
import numpy as np
import seaborn as sns

data = [551, 153, 0, 0, 194]

num_simulations = 500000
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
print(np.percentile(simulateddata,50))
print(np.percentile(simulateddata,15))
print(np.percentile(simulateddata,10))

