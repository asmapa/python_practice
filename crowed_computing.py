from statistics import mean
from scipy import stats
import matplotlib.pyplot as plt
import statistics

estimates = [100, 200, 234, 345, 300, 200, 350, 567, 876, 234, 890, 123, 145, 765, 987]
estimates.sort()
tv = int(0.1 * len(estimates))

# Trimming 10% from both ends
estimates = estimates[tv:]  # Removes the smallest 10%
estimates = estimates[:len(estimates) - tv]  # Removes the largest 10%

print(estimates)  # Print the trimmed list
print(mean(estimates))  # Print the mean of the trimmed list


#Sorting: The data is first sorted in ascending order.
#Trimming: A certain percentage of the smallest and largest values are removed (trimmed) from the sorted data.
#Calculating Mean: The mean of the remaining values (after trimming) is calculated.


# Calculate the trimmed mean using scipy.stats
m = stats.trim_mean(estimates, 0.1)  # Corrected module name to 'stats'
print(m)  # Print the trimmed mean

y=[]
for i in range(len(estimates)):
    y.append(5)
plt.plot(estimates,y,'r--')
plt.plot([statistics.mean(estimates)],[5],'ro')
plt.plot([375],[5],'g^')