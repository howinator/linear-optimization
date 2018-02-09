from gurobipy import *
import numpy as np


def ex114a():

    m = Model("mip1")

    cost_matrix = read_numpy_matrix()
    n = cost_matrix.shape[0]

    choice_tuple = m.addVars(n, n, vtype=GRB.BINARY, name="choice")

    linear_expression = LinExpr()
    for row, outer_index in enumerate(choice_tuple):
        linear_expression.addTerms(cost_matrix[outer_index, :], row)

    # m.setObjective(sum(choice_var * cost_matrix[outer_index, inner_index]
    #                    for choice_var, inner_index in enumerate(row)
    #                    for row, outer_index in enumerate(choice_tuple)), GRB.MINIMIZE)

    m.setObjective(linear_expression, GRB.MINIMIZE)
    m.addConstrs(sum(x[i, :] for i in range(n)) == 1)
    m.addConstrs(sum(x[:, i] for i in range(n)) == 1)

    m.optimize()

    _print_results(m)


def read_numpy_matrix():
    with open('cost.npy') as f:
        matrix = np.load(f)
    return matrix


def _print_results(m):
    for v in m.getVars():
        print(v.varName, v.x)

    print('Obj:', m.objVal)


print("-----------problem1 below--------------")
problem1()
