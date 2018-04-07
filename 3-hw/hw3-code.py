from gurobipy import *
import numpy as np
import scipy.io
import matplotlib.pyplot as plt



def problem6():

    dir_base = "PS3 prob6"
    A = np.loadtxt(open("{}/A_small.csv".format(dir_base)), delimiter=",")
    b = np.loadtxt(open("{}/b_small.csv".format(dir_base)), delimiter=",")
    # import pdb; pdb.set_trace()
    A = np.matrix([[float(x) for x in y] for y in A])
    b = np.array([float(x) for x in b])

    m = A.shape[0]
    n = A.shape[1]

    # first subproblem
    run_variant = 1
    x, model = get_model(run_variant, n)
    v = quicksum(quicksum(A[i, j] * x[j] * A[i, j] * x[j] - 2 * A[i, j] * x[j] * b[i] + b[i] * b[i] for j in range(n)) for i in range(m))
    optimize_function(model, v, run_variant)
    show_results(model, A, b, m, n, "Euclidean")

    # second subproblem
    run_variant = 2
    x, model = get_model(run_variant, n)
    # v =


def get_model(run_variant, n):

    dir_base = "PS3 prob6"
    model = Model("model{}".format(str(run_variant)))

    x = model.addVars(n, vtype=GRB.CONTINUOUS, name="x")

    return x, model


def optimize_function(model, function, run_variant, min_or_max=GRB.MINIMIZE):

    model.setObjective(function, min_or_max)
    model.optimize()

    # _print_results(model)

def show_results(model, A, b, m, n, run_variant):

    x = [var.x for var in model.getVars()]
    positions = x
    plot_one_histogram(positions, "{} Positions".format(run_variant))
    connection_lengths = []
    for row in range(m):
        first_val = 0
        for col in range(n):
            first_val += A[row, col] * x[col]
        full_val = first_val - b[row]
        full_val = abs(full_val)
        connection_lengths.append(full_val)
    plot_one_histogram(connection_lengths, "{} Connection Lengths".format(run_variant))
    print('Total length for {}: {}'.format(run_variant, model.objVal))
    print('Max Length for {}: {}'.format(run_variant, max(connection_lengths)))

def plot_one_histogram(data, title):
    bins = np.linspace(-1, 1, 20)

    plt.hist(data, bins)
    plt.title("{} Histogram".format(title))
    plt.show()


def _print_results(m):
    for v in m.getVars():
        print(v.varName, v.x)

    print('Obj:', m.objVal)


print("-----------problem6 below--------------")
problem6()
