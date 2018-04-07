from gurobipy import *


def ex114a():

    m = Model("mip1")

    p1 = m.addVar(vtype=GRB.INTEGER, name="p1")
    p2 = m.addVar(vtype=GRB.INTEGER, name="p2")

    m.setObjective(6 * p1 + 5.4 * p2, GRB.MAXIMIZE)

    m.addConstr(0.3 * p1 + 0.38 * p2 <= 4000, "capital")
    m.addConstr(3 * p1 + 4 * p2 <= 20000, "machinetime")

    m.optimize()

    _print_results(m)


def ex114b():

    m = Model("mip1")

    p1 = m.addVar(vtype=GRB.INTEGER, name="p1")
    p2 = m.addVar(vtype=GRB.INTEGER, name="p2")

    m.setObjective(6 * p1 + 5.4 * p2, GRB.MAXIMIZE)

    m.addConstr(0.3 * p1 + 0.38 * p2 <= 3600, "capital")
    m.addConstr(3 * p1 + 4 * p2 <= 22000, "machinetime")

    m.optimize()

    _print_results(m)


def ex115():

    m = Model("mip1")

    p1 = m.addVar(vtype=GRB.INTEGER, name="p1")
    p2 = m.addVar(vtype=GRB.INTEGER, name="p2")

    m.setObjective(8.8 * p1 + 7.1 * p2, GRB.MAXIMIZE)

    m.addConstr(0.25 * p1 + 1 / 3 * p2 <= 90, "labor")
    m.addConstr(.125 * p1 + 1 / 3 * p2 <= 80, "testing")

    m.optimize()

    _print_results(m)


def ex116():

    m = Model("mip1")

    p1 = m.addVar(vtype=GRB.CONTINUOUS, name="p1")
    p2 = m.addVar(vtype=GRB.CONTINUOUS, name="p2")
    p3 = m.addVar(vtype=GRB.CONTINUOUS, name="p3")

    m.setObjective(200 * p1 + 60 * p2 + 216 * p3, GRB.MAXIMIZE)

    m.addConstr(3 * p1 + p2 + 5 * p3 <= 8000000, "ca")
    m.addConstr(5 * p1 + p2 + 3 * p3 <= 5000000, "cb")

    m.optimize()

    _print_results(m)


def _print_results(m):
    for v in m.getVars():
        print(v.varName, v.x)

    print('Obj:', m.objVal)


print("-----------114a below--------------")
ex114a()
print("-----------114b below--------------")
ex114b()
print("-----------115 below---------------")
ex115()
print("-----------116 below---------------")
ex116()
