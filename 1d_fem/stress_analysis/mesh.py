import numpy as np

def create_mesh(n) :
    F = np.zeros(n+1, dtype= float)
    d = np.zeros(n+1, dtype= float)
    k = np.zeros((n+1, n+1), dtype= float)
    return F, d, k