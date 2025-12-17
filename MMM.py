import numpy as np

Mean = [2,5,3,6,9,8,1,7,10]
print("Mean of the list is:", sum(Mean)/len(Mean))
print("Median", np.median(Mean))
print(np.mean(Mean))

n = len(Mean)
for i in range(n):
    for j in range(0, n - i - 1):
        if Mean[j] > Mean[j + 1]:
            # swap
            Mean[j], Mean[j + 1] = Mean[j + 1], Mean[j]

print("Sorted list using Bubble Sort:", Mean)