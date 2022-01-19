#/bin/bash/python3

# Import packages
import numpy as np
import matplotlib.pyplot as plt
from models import *

# Read the data file
data = np.loadtxt('data.txt')

# Reformat data
years = data[:,0]
prey = data[:,1]
predator = data[:,2]

# Simulate data

# get initial condition
y0 = [prey[0], predator[0]]

# set LV model parameter
a = 0.5
b = 0.01
c = 0.5
d = 0.01

#a = +5.903e-02
#b = +4.731e-03
#c = +7.103e-01
#d = +2.406e-02

a = +5.475e-01
b = +2.812e-02
c = +8.432e-01
d = +2.656e-02

# simulation length
T = len(years)

simulation = lotka_volterra(y0, T, a, b, c, d)
simyears = np.linspace(years[0], years[0]+T, len(simulation))

# Plot the data file
fig = plt.figure()
plt.plot(years, prey, 'bx')
plt.plot(years, predator, 'rx')
plt.xlabel('years')
plt.ylabel('population size')

# Plot simulation
plt.plot(simyears, simulation[:,0], color='b', label='simulated prey')
plt.plot(simyears, simulation[:,1], color='r', label='simulated predator')
plt.legend()

# Save the figure to a file
plt.savefig('simulated_population.png')

#uncomment to display plot on screen
#plt.show() #uncomment to display plot on screen
