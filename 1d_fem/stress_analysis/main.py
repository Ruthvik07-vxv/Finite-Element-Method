import numpy as np
import sys
import mesh as msh
import assembler as asm
import solver as slv

def Save_mesh(parameter, filename = "displacement_grid.txt") :
    with open(filename, "w") as f :
        for row in (parameter) :
            for val in row :
                f.write(f"{val:10.4f} ")
            f.write("\n")
    
    print(f"Displacement Grid saved to {filename}")

def save_force_grid(parameter, filename = "force_grid.txt") :
    with open(filename, "w") as f :
        for row in (parameter) :
            for val in row :
                f.write(f"{val:10.4f} ")
            f.write("\n")
    
    print(f"Force Grid saved to {filename}")

def save_stiffness_matrix(parameter, filename = "stiffness_matrix.txt") :
    with open(filename, "w") as f :
        for row in (parameter) :
            for val in row :
                f.write(f"{val:10.4f} ")
            f.write("\n")
    
    print(f"Stiffness Matrix saved to {filename}")

n = (int(input("Enter the number of elements: ")) + 1)
x = float(input("Enter the length of the rod: "))
F, d, k, fixed_force, fixed_deformation = msh.create_mesh(n)


for i in range(n-1):
    k_x = float(input(f"Enter the stiffness value for element {i+1}: "))
    k = asm.assemble_stiffness_matrix(k, i, k_x)

count = 0
while True and count < n :
    count += 1
    force = input(f"Enter the force value for node {count} (or 'done' to finish): ")
    if force.lower() == 'done' :
        break
    F = asm.assemble_force_boundary_condition(F, fixed_force, count-1, float(force))
    

count = 0
while True :
    count += 1
    deformation = input(f"Enter the deformation value for node {count} (or 'done' to finish): ")
    if deformation.lower() == 'done' :
        break
    d = asm.assemble_displacement_boundary_condition(d, fixed_deformation, count-1, float(deformation))



k_original = k.copy()

count = 0
for i in range(n) :
    if fixed_deformation[i] :
        F, k = slv.displacement_boundary_condition(F, k, d, i) 
    else :
        count += 1

if count >= n :
    print("No fixed node found. Please ensure at least one node has a fixed deformation boundary condition.")
    sys.exit(1)

type_of_solver = input("Enter the type of solver (force/displacement): ").lower()
if type_of_solver == "displacement" :
    d = slv.solve_displacement(k, F)
    F_real = slv.solve_force(k_original, d)
    Save_mesh(d)
    save_force_grid(F_real)
    save_stiffness_matrix(k_original)
else :
    F = slv.solve_force(k_original, d)
    Save_mesh(d)
    save_force_grid(F)
    save_stiffness_matrix(k_original)
