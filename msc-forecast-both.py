import random
import numpy as np
import seaborn as sns

rem = 46648
data = [970, 0, 0, 0, 0, 253, 348, 0, 329, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 225, 710, 602, 279, 341, 0, 275, 251, 183]
days = 128 - 28
num_simulations = 100000

# When
simulateddata = [0]*num_simulations

for i in range(num_simulations):
    j = 0
    num_days = 0
    while j < rem:
        j = j+random.choice(data)
        num_days+=1
    simulateddata[i] = num_days

print(np.percentile(simulateddata,50))
print(np.percentile(simulateddata,80))
print(np.percentile(simulateddata,95))

# How many
for i in range(num_simulations):
    sample = [0]*days
    for j in range(days):
        sample[j] = random.choice(data)
        total_pages_read = sum(sample)
    simulateddata[i] = total_pages_read

print(np.percentile(simulateddata,50))
print(np.percentile(simulateddata,20))
print(np.percentile(simulateddata,5))