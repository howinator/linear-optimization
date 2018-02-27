from gurobipy import *
import numpy as np


def problem1():

    m = Model("mip1")

    cost_matrix = read_numpy_matrix()
    n = cost_matrix.shape[0]

    choice_tuple = m.addVars(n, n, vtype=GRB.BINARY, name="choice")

    linear_expression = LinExpr()
    for row_idx in range(n):
        for col_idx in range(n):
            linear_expression.addTerms(cost_matrix[row_idx, col_idx],
                                       choice_tuple[row_idx, col_idx])

    m.setObjective(linear_expression, GRB.MINIMIZE)
    m.addConstrs(sum(choice_tuple[worker, i] for i in range(n)) == 1 for worker in range(n))
    m.addConstrs(sum(choice_tuple[i, job] for i in range(n)) == 1 for job in range(n))

    m.optimize()

    _print_results(m)


def problem2():

    array = [4, 7, 2, 8, 1, 5]
    r = 3
    n = len(array)
    m = Model("mip1")

    choice_tuple = m.addVars(n, 1, vtype=GRB.BINARY, name="choice")

    linear_expression = LinExpr()
    for row in range(n):
        linear_expression.addTerms(array[row], choice_tuple[row, 0])

    m.setObjective(linear_expression, GRB.MAXIMIZE)
    m.addConstr(sum(choice_tuple[row, 0] for row in range(n)) == r)

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
print("-----------problem2 below--------------")
problem2()
