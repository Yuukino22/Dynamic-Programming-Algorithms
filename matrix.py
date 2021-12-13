import math

inf = math.inf



def matrix(d):
    n = len(d)
    M = []
    S = []
    for i in range(n+1):
        M.append([])
    for i in range(n+1):
        for j in range(n+1):
            M[i].append("N")
    for i in range(n+1):
        S.append([])
    for i in range(n+1):
        for j in range(n+1):
            S[i].append("N")
    for i in range(1,n+1):
        M[i][i] = 0
    for l in range(2, n+1):
        for i in range(1, n - l + 1):
            j = i + l - 1
            M[i][j] = inf
            for k in range(i, j):
                x = M[i][k] + M[k+1][j] + d[i-1]*d[k]*d[j]
                if x < M[i][j]:
                    M[i][j] = x
                    S[i][j] = k
    return M,S

if __name__ == '__main__':
    d = [6,14,19,4,15,17,10]
    M, S = matrix(d)
    for i in M[1:len(d)]:
        for j in i[1:len(d)]:
            print(j, end = ", ")
        print()
    for i in S[1:len(d)]:
        for j in i[1:len(d)]:
            print(j, end = ", ")
        print()
    
