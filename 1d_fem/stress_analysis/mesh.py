import numpy as np

def create_mesh(n) :
    F = np.zeros(n+1, dtype= float)
    d = np.zeros(n+1, dtype= float)
    k = np.zeros((n+1, n+1), dtype= float)
    fixed_force = np.zeros(n+1, dtype= bool)
    fixed_deformation = np.zeros(n+1, dtype= bool)
    return F, d, k, fixed_force, fixed_deformation