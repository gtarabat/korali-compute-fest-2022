#/bin/bash/python3

# Import packages
import numpy as np
import matplotlib.pyplot as plt

# Read the data file
data = np.loadtxt('data.txt')

# Reformat data
years = data[:,0]
predator = data[:,1]
prey = data[:,2]

# Plot the data file
fig = plt.figure()
plt.plot(years, prey, color='b', label='prey', marker='x')
plt.plot(years, predator, color='r', label='predator', marker='x')
plt.xlabel('years')
plt.ylabel('population size')
plt.legend()

# Save the figure to a file
plt.savefig('population.png')

#uncomment to display plot on screen
#plt.show() #uncomment to display plot on screen
