idef gaussianElimination(mat):

    singular_flag = forwardElim(mat)

    if (singular_flag != -1):
        if (mat[singular_flag][N]):
            print("Tidak punya solusi.")
        else:
            print("memiliki solusi tak hingga")

        return

    backSub(mat)


def swap_row(mat, i, j):

    for k in range(N + 1):

        temp = mat[i][k]
        mat[i][k] = mat[j][k]
        mat[j][k] = temp


def forwardElim(mat):
    for k in range(N):

        i_max = k
        v_max = mat[i_max][k]

        for i in range(k + 1, N):
            if (abs(mat[i][k]) > v_max):
                v_max = mat[i][k]
                i_max = i

        if not mat[k][i_max]:
            return k

        if (i_max != k):
            swap_row(mat, k, i_max)

        for i in range(k + 1, N):

            f = mat[i][k]/mat[k][k]

            for j in range(k + 1, N + 1):
                mat[i][j] -= mat[k][j]*f

            mat[i][k] = 0

    return -1


def backSub(mat):

    x = [None for _ in range(N)]

    for i in range(N-1, -1, -1):
        x[i] = mat[i][N]

        for j in range(i + 1, N):

            x[i] -= mat[i][j]*x[j]

        x[i] = (x[i]/mat[i][i])

    print("\nSolusi akhirnya:")
    print("{", end=" ")
    for i in range(N):
        if(i+1 !=N):
            print("x", end="")
            print(i+1 , end=" = ")
            print("{:.8f}".format(x[i]), end=", ")
        else:
            print("x", end="")
            print(i+1 , end=" = ")
            print("{:.8f}".format(x[i]), end=" ")
    print("}")
