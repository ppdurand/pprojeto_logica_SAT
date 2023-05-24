from pysat import solvers, cnf

formula = cnf.CNF()
solver = solvers.Solver()
solver.append_formula(formula)
result = solver.solve()

if result:
    model = solver.get_model()
    print("Satisfatória. Modelo: ", model)
else:
    print("Insatisfatória.")
