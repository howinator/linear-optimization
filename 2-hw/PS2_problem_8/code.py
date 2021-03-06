from gurobipy import *
import numpy as np
import scipy.io


def problem8():

    model = Model("mip1")
    A = read_mtx_matrix_file('A.mtx')
    c = read_mtx_array_file('c.mtx')
    b = read_mtx_array_file('b.mtx')
    lbd = read_mtx_array_file('lower_bd.mtx')
    ubd = read_mtx_array_file('upper_bd.mtx')

    n = A.shape[0]
    m = A.shape[1]

    dec_vars = model.addVars(m, vtype=GRB.BINARY, ub=ubd, lb=lbd, name="dev_vars")
    for i in range(n):
        # import pdb; pdb.set_trace()
        model.addConstr(quicksum(A[i][j] * dec_vars[j] for j in range(m)) == b[i], "c{}".format(str(i)))

    obj_expr = quicksum(c[i] * dec_vars[i] for i in range(m))
    model.setObjective(obj_expr, GRB.MINIMIZE)

    model.optimize()

    _print_results(model)


def read_mtx_array_file(filename):

    return [ele[0] for ele in scipy.io.mmread(filename)]


def read_mtx_matrix_file(filename):
    return scipy.io.mmread(filename).toarray()


def _print_results(m):
    for v in m.getVars():
        print(v.varName, v.x)

    print('Obj:', m.objVal)


print("-----------problem8 below--------------")
problem8()
