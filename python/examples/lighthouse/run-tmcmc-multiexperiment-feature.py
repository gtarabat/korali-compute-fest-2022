#!/usr/bin/env python3

# In this example, we demonstrate how Korali samples the posterior
# distribution of the coastline distance 'alpha' and distance from shore 'beta'
# of the lighthouse.


# Importing computational model
import sys
sys.path.append('./models')
from models import *

# Creating Synthetic Data
data = getReferenceData(N=512)

# Starting Korali's Engine
import korali
k = korali.Engine()


# Initialize experiment list
experiments = []

# Defnition experiment 1
e1 = korali.Experiment()

# Configuring problem
e1["Problem"]["Type"] = "Bayesian/Custom"
e1["Problem"]["Likelihood Model"] = lambda x: model1(x, data)

e1["Distributions"][0]["Name"] = "Uniform 0"
e1["Distributions"][0]["Type"] = "Univariate/Uniform"
e1["Distributions"][0]["Minimum"] = -100.0
e1["Distributions"][0]["Maximum"] = +100.0

# Defining problem's variables and prior distribution
e1["Variables"][0]["Name"] = "Alpha"
e1["Variables"][0]["Prior Distribution"] = "Uniform 0"

# Configuring the TMCMC sampler parameters
e1["Solver"]["Type"] = "Sampler/TMCMC"
e1["Solver"]["Population Size"] = 5000
e1["Solver"]["Target Coefficient Of Variation"] = 0.2

# Gener settings 
e1["File Output"]["Path"] = "_korali_result_example1_tmcmc"


# Defnition experiment 2
e2 = korali.Experiment()

# Configuring problem
e2["Problem"]["Type"] = "Bayesian/Custom"
e2["Problem"]["Likelihood Model"] = lambda x: model2(x, data)

e2["Distributions"][0]["Name"] = "Uniform 0"
e2["Distributions"][0]["Type"] = "Univariate/Uniform"
e2["Distributions"][0]["Minimum"] = -100.0
e2["Distributions"][0]["Maximum"] = +100.0

e2["Distributions"][1]["Name"] = "Uniform 1"
e2["Distributions"][1]["Type"] = "Univariate/Uniform"
e2["Distributions"][1]["Minimum"] = 0.0
e2["Distributions"][1]["Maximum"] = +100.0

# Defining problem's variables and prior distribution
e2["Variables"][0]["Name"] = "Alpha"
e2["Variables"][0]["Prior Distribution"] = "Uniform 0"

e2["Variables"][1]["Name"] = "Beta"
e2["Variables"][1]["Prior Distribution"] = "Uniform 1"

# Configuring the TMCMC sampler parameters
e2["Solver"]["Type"] = "Sampler/TMCMC"
e2["Solver"]["Population Size"] = 2000
e2["Solver"]["Target Coefficient Of Variation"] = 0.2

# General settings
e2["File Output"]["Path"] = "_korali_result_example2_tmcmc" 

# Running Korali
k.run([e1, e2])
