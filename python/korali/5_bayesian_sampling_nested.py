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
e["Problem"]["Computational Model"] = lambda sample: k_lotka_volterra(y0, T, sample)

# Configuring the problem's prior distributions
e["Distributions"][0]["Name"] = "Prior LV Parameter"
e["Distributions"][0]["Type"] = "Univariate/Uniform"
e["Distributions"][0]["Minimum"] = 0.0
e["Distributions"][0]["Maximum"] = +1.0

e["Distributions"][1]["Name"] = "Prior Sigma"
e["Distributions"][1]["Type"] = "Univariate/Uniform"
e["Distributions"][1]["Minimum"] = 0.0
e["Distributions"][1]["Maximum"] = +25.0

# Defining the problem's variables.
e["Variables"][0]["Name"] = "a"
e["Variables"][0]["Prior Distribution"] = "Prior LV Parameter"

e["Variables"][1]["Name"] = "b"
e["Variables"][1]["Prior Distribution"] = "Prior LV Parameter"

e["Variables"][2]["Name"] = "c"
e["Variables"][2]["Prior Distribution"] = "Prior LV Parameter"

e["Variables"][3]["Name"] = "d"
e["Variables"][3]["Prior Distribution"] = "Prior LV Parameter"

e["Variables"][4]["Name"] = "Sigma"
e["Variables"][4]["Prior Distribution"] = "Prior Sigma"
e["Variables"][4]["Initial Value"] = 5

# Configuring Nested Sampling parameters
e["Solver"]["Type"] = "Sampler/Nested"
e["Solver"]["Resampling Method"] = "Multi Ellipse"
e["Solver"]["Number Live Points"] = 1500
e["Solver"]["Termination Criteria"]["Min Log Evidence Delta"] = 1e-1

# Configuring results path
e["File Output"]["Enabled"] = True
e["File Output"]["Path"] = '_korali_result_nested'
e["File Output"]["Frequency"] = 5000

e["Console Output"]["Frequency"] = 500
e["Console Output"]["Verbosity"] = 'Detailed'

# Running Korali
k.run(e)
