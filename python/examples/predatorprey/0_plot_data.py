#/bin/bash/python3

# Import packages
import numpy as np
import matplotlib.pyplot as plt

# Read the data file
data = np.loadtxt('data.txt')

# Reformat data
years = data[:,0]
prey = data[:,1]
predator = data[:,2]

# Plot the data file
fig = plt.figure()
plt.plot(years, prey, '--x', color='b', label='prey')
plt.plot(years, predator, '--x', color='r', label='predator')
plt.xlabel('years')
plt.ylabel('population size')
plt.legend()

# Save the figure to a file
plt.savefig('0_population.png')

#uncomment to display plot on screen
#plt.show() #uncomment to display plot on screen
