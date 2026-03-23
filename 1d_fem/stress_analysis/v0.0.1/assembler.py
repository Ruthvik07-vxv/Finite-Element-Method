def stiffness_value(k, c, k_x, a, b) :
    k[b, a] += c * k_x

    return k

def assemble_stiffness_matrix(k, i, k_x) :
    k = stiffness_value(k, 1, k_x, i, i)
    k = stiffness_value(k, -1, k_x, i, i+1)
    k = stiffness_value(k, -1, k_x, i+1, i)
    k = stiffness_value(k, 1, k_x, i+1, i+1)
    return k

def assemble_displacement_boundary_condition(d, fixed_deformation, n, deformation) :
    d[n] = deformation
    fixed_deformation[n] = True
    return d

def assemble_force_boundary_condition(F, fixed_force, n, value) :
    F[n] = value
    fixed_force[n] = True
    return F