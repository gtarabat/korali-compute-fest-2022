#!/usr/bin/env python3

## In this example, we demonstrate how Korali finds values for the
## parameter of the [Lotka-Volterra](https://en.wikipedia.org/wiki/Lotka%E2%80%93Volterra_equations)
## equations that maximize the likelihood of the reference data.

# Importing computational model
import sys
import math
sys.path.append('./_model')
from models import *

# Time scale
T = 21

# Initial population (Prey & Predator)
y0 = [30,4]

# Starting Korali's Engine
import korali
k = korali.Engine()

# Creating new experiment
e = korali.Experiment()

# Configuring Problem
e["Random Seed"] = 0xC0FEE
e["Problem"]["Type"] = "Bayesian/Reference"
e["Problem"]["Likelihood Model"] = "Normal"
e["Problem"]["Reference Data"] = getReferenceData()
e["Problem"]["Computational Model"] = lambda sample: lotka_volterra_llk(y0, T, sample)

# Configuring the problem's prior distributions
e["Distributions"][0]["Name"] = "Prior LV Parameter"
e["Distributions"][0]["Type"] = "Univariate/Uniform"
e["Distributions"][0]["Minimum"] = 0.0
e["Distributions"][0]["Maximum"] = +1.0

e["Distributions"][1]["Name"] = "Prior Sigma"
e["Distributions"][1]["Type"] = "Univariate/Uniform"
e["Distributions"][1]["Minimum"] = 0.0
e["Distributions"][1]["Maximum"] = +100.0

# Defining the problem's variables.
e["Variables"][0]["Name"] = "a"
e["Variables"][0]["Prior Distribution"] = "Prior LV Parameter"
e["Variables"][0]["Initial Value"] = 0.5
e["Variables"][0]["Initial Standard Deviation"] = 0.1

e["Variables"][1]["Name"] = "b"
e["Variables"][1]["Prior Distribution"] = "Prior LV Parameter"
e["Variables"][1]["Initial Value"] = 0.03
e["Variables"][1]["Initial Standard Deviation"] = 0.01

e["Variables"][2]["Name"] = "c"
e["Variables"][2]["Prior Distribution"] = "Prior LV Parameter"
e["Variables"][2]["Initial Value"] = 0.8
e["Variables"][2]["Initial Standard Deviation"] = 0.1

e["Variables"][3]["Name"] = "d"
e["Variables"][3]["Prior Distribution"] = "Prior LV Parameter"
e["Variables"][3]["Initial Value"] = 0.03
e["Variables"][3]["Initial Standard Deviation"] = 0.01

e["Variables"][4]["Name"] = "Sigma"
e["Variables"][4]["Prior Distribution"] = "Prior Sigma"
e["Variables"][4]["Initial Value"] = 5
e["Variables"][4]["Initial Standard Deviation"] = 1

# Configuring CMA-ES parameters
e["Solver"]["Type"] = "Optimizer/CMAES"
e["Solver"]["Population Size"] = 8
e["Solver"]["Mu Value"] = 4
e["Solver"]["Termination Criteria"]["Max Generations"] = 500

# Configuring results path
e["File Output"]["Enabled"] = True
e["File Output"]["Path"] = '_korali_result_cmaes_bayesian'
e["File Output"]["Frequency"] = 1

# Running Korali
k.run(e)
