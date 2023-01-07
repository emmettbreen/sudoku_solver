import cvxpy as cp


def solve(board):
    constraints = []
    X = [None for _ in range(27)]
    for k in range(27):
        X[k] = cp.Variable((9,9), boolean=True)
        constraints += [sum(X[k][i][j] for i in range(9)) == 1 for j in range(9)]
        constraints += [sum(X[k][i][j] for j in range(9)) == 1 for i in range(9)]



    Y = cp.Variable((9,9), integer=True)

    constraints += [Y[i][j] == sum(X[i][j][k] * (k+1) for k in range(9)) for i in range(9) for j in range(9)]
    constraints += [Y[i][j] == sum(X[j+9][i][k] * (k+1) for k in range(9)) for j in range(9) for i in range(9)]

    constraints += [Y[k][l] == sum(X[18][k+3*l][j] * (j+1) for j in range(9)) for k in [0,1,2] for l in [0,1,2]]
    constraints += [Y[k][l] == sum(X[19][k+3*(l-3)][j] * (j+1) for j in range(9)) for k in [0,1,2] for l in [3,4,5]]
    constraints += [Y[k][l] == sum(X[20][k+3*(l-6)][j] * (j+1) for j in range(9)) for k in [0,1,2] for l in [6,7,8]]
    constraints += [Y[k][l] == sum(X[21][(k-3)+3*l][j] * (j+1) for j in range(9)) for k in [3,4,5] for l in [0,1,2]]
    constraints += [Y[k][l] == sum(X[22][(k-3)+3*(l-3)][j] * (j+1) for j in range(9)) for k in [3,4,5] for l in [3,4,5]]
    constraints += [Y[k][l] == sum(X[23][(k-3)+3*(l-6)][j] * (j+1) for j in range(9)) for k in [3,4,5] for l in [6,7,8]]
    constraints += [Y[k][l] == sum(X[24][(k-6)+3*l][j] * (j+1) for j in range(9)) for k in [6,7,8] for l in [0,1,2]]
    constraints += [Y[k][l] == sum(X[25][(k-6)+3*(l-3)][j] * (j+1) for j in range(9)) for k in [6,7,8] for l in [3,4,5]]
    constraints += [Y[k][l] == sum(X[26][(k-6)+3*(l-6)][j] * (j+1) for j in range(9)) for k in [6,7,8] for l in [6,7,8]]

    for i in range(9):
        for j in range(9):
            if board[i][j] != '':
                constraints += [Y[i][j] == int(board[i][j])]


    problem = cp.Problem(cp.Maximize(0), constraints)
    problem.solve()

    for v in problem.variables():
        if 0 not in v.value[0]:
            return v.value




