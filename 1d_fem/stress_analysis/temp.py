import numpy as np
import matplotlib.pyplot as plt
import sys

def create_mesh(n) :
    F = np.zeros(n+1, dtype= float)
    d = np.zeros(n+1, dtype= float)
    k = np.zeros((n+1, n+1), dtype= float)
    return F, d, k

def stiffness_value(k, c, k_x, a, b) :
    k[b, a] += c * k_x

    return k

def assemble_stiffness_matrix(k, i, k_x) :
    k = stiffness_value(k, 1, k_x, i, i)
    k = stiffness_value(k, -1, k_x, i, i+1)
    k = stiffness_value(k, -1, k_x, i+1, i)
    k = stiffness_value(k, 1, k_x, i+1, i+1)
    return k

def displacement_boundary_condition(d, n, deformation) :
    d[n] = deformation
    return d

def force_boundary_condition(F, n, value) :
    F[n] = value
    return F

def solve_displacement(k, F) :
    d = np.linalg.solve(k, F)
    return d

def solve_force(k, d) :
    F = np.dot(k, d)
    return F

def call_displacement_solver(n, x) :
    F, d, k = create_mesh(n)
    i = 0
    while i < n :
        k_x = float(input(f"Enter the stiffness value for element {i+1}: "))
        k = assemble_stiffness_matrix(k, i, k_x)
        i += 1
    count = 0
    while True :
        count += 1
        force = input(f"Enter the force value for node {count} (or 'done' to finish): ")
        if force.lower() == 'done' :
            break
        F = force_boundary_condition(F, count-1, float(force))

    d = solve_displacement(k, F)
    return d


def call_force_solver(n, x) :
    F, d, k = create_mesh(n)
    i = 0
    while i < n :
        k_x = float(input(f"Enter the stiffness value for element {i+1}: "))
        k = assemble_stiffness_matrix(k, i, k_x)
        i += 1
    count = 0
    while True :
        count += 1
        deformation = input(f"Enter the deformation value for node {count} (or 'done' to finish): ")
        if deformation.lower() == 'done' :
            break
        d = displacement_boundary_condition(d, count-1, float(deformation))

    F = solve_force(k, d)
    return F

def main() :
    n = input("Enter the number of elements: ")
    x = input("Enter the length of the rod: ")
    input_case = input("Enter the type of boundary condition (force/displacement): ").lower()
    if input_case == "force" :
        call_displacement_solver(n, x)
    elif input_case == "displacement" :
        call_force_solver(n, x)
    else :
        print("Invalid input for boundary condition type.")
        sys.exit(1)