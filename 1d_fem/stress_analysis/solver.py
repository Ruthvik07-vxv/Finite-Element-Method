import numpy as np

def displacement_boundary_condition(F, k, d, i) :
    k[i, :] = 0
    k[:, i] = 0
    k[i, i] = 1
    F[i] = d[i]   

    return F, k

def solve_displacement(k, F) :
    d = np.linalg.solve(k, F)
    return d

def solve_force(k, d) :
    F = np.dot(k, d)
    return F