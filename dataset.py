"""where the dataset will be generated"""
import pandas as pd 
import numpy as np 

from utils.black_scholes import black_scholes_put

#Domain boundaries
S_bound = (0.0, 200.0)
K_bound = (50.0, 150.0)
T_bound = (0.0, 5.0)
r_bound = (0.001, 0.05)
sigma_bound = (0.05, 1.5)

def generate_data(n):
    return np.random.rand(n,5)

