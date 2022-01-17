#!/usr/bin/env python3

## In this example, we demonstrate how Korali finds values for the
## parameter of the [Lotka-Volterra](https://en.wikipedia.org/wiki/Lotka%E2%80%93Volterra_equations)
## equations that maximize the likelihood of the reference data.

# Importing computational model
import sys
import math
sys.path.append('./_model')
from model import *

# Time scale
T = 21

# Read the data file
data = np.loadtxt('data.txt')

# Initial population (Prey & Predator)
y0 = [30,4]

# Starting Korali's Engine
import korali
k = korali.Engine()

# Creating new experiment
e = korali.Experiment()

# Configuring Problem
e["Random Seed"] = 0xC0FEE
e["Problem"]["Type"] = "Optimization"
e["Problem"]["Objective Function"] = lambda sample: k_lotka_volterra_opt(y0, T, data, sample)

# Defining the problem's variables.
e["Variables"][0]["Name"] = "a"
e["Variables"][0]["Initial Value"] = 0.5
e["Variables"][0]["Initial Standard Deviation"] = 0.01

e["Variables"][1]["Name"] = "b"
e["Variables"][1]["Initial Value"] = 0.03
e["Variables"][1]["Initial Standard Deviation"] = 0.001

e["Variables"][2]["Name"] = "c"
e["Variables"][2]["Initial Value"] = 0.8
e["Variables"][2]["Initial Standard Deviation"] = 0.01

e["Variables"][3]["Name"] = "d"
e["Variables"][3]["Initial Value"] = 0.03
e["Variables"][3]["Initial Standard Deviation"] = 0.01

# Configuring CMA-ES parameters
e["Solver"]["Type"] = "Optimizer/CMAES"
e["Solver"]["Population Size"] = 8
e["Solver"]["Mu Value"] = 4
e["Solver"]["Termination Criteria"]["Min Value Difference Threshold"] = 1e-32
e["Solver"]["Termination Criteria"]["Max Generations"] = 500

# Configuring results path
e["File Output"]["Enabled"] = True
e["File Output"]["Path"] = '_korali_result_cmaes'
e["File Output"]["Frequency"] = 1

# Running Korali
k.run(e)
