import numpy as np
from scipy.integrate import odeint

# Lotka-Volterra simulator
def lotka_volterra(y0, T, a, b, c, d):

  F = lambda y, t: [
            y[0] * (a - b * y[1]),     # Change in prey population.
            y[1] * (d * y[0] - c)]     # Change in predator population.

  t = range(0,T)
  y = odeint(F, y0, t)

  return y

# Lotka-Volterra wrapper for Korali
def k_lotka_volterra_opt(y0, T, data, sample):
  a = sample["Parameters"][0]
  b = sample["Parameters"][1]
  c = sample["Parameters"][2]
  d = sample["Parameters"][3]
  
  y = lotka_volterra(y0, T, a, b, c, d)
  y = np.concatenate((y[:,0], y[:,1]), axis=0)
  data = np.concatenate((data[:,2], data[:,1]), axis=0)

  sample["F(x)"] = -np.linalg.norm(y - data)
  

def k_lotka_volterra(y0, T, sample):
  a = sample["Parameters"][0]
  b = sample["Parameters"][1]
  c = sample["Parameters"][2]
  d = sample["Parameters"][3]
  sig = sample["Parameters"][4]
  
  y = lotka_volterra(y0, T, a, b, c, d)

  simData = list(y[:,0]) + list(y[:,1])
  sample["Reference Evaluations"] = simData
  sample["Standard Deviation"] = 2*T*[sig]

# Extract reference data from data.txt
def getReferenceData():

    # Read the data file
    data = np.loadtxt('data.txt')

    # Reformat data
    predator = data[:,1]
    prey = data[:,2]
    return list(prey) + list(predator) 
