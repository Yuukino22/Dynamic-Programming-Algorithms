import math

inf = math.inf

def optTree(p):
    n = len(p) - 1
    E = []
    W = []
    root = []
    for i in range(n+1+1):
        E.append([])
    for i in range(n+1+1):
        for j in range(n+1):
            E[i].append("N")
    for i in range(n+1+1):
        root.append([])
    for i in range(n+1+1):
        for j in range(n+1):
            root[i].append("N")
    for i in range(n+1+1):
        W.append([])
    for i in range(n+1+1):
        for j in range(n+1):
            W[i].append("N")

    for i in range(1, n+2):
        E[i][i-1] = 0
        W[i][i-1] = 0
        for j in range(i, n+1):
            W[i][j] = W[i][j-1] + p[j]

    for size in range(1,n+1):
        for i in range(1, n - size + 2):
            j = i + size - 1
            E[i][j] = inf
            for r in range(i, j+1):
                x = E[i][r-1] + E[r+1][j] + W[i][j]
                if x < E[i][j]:
                    E[i][j] = x
                    root[i][j] = r
    return E, root

if __name__ == '__main__':
    #p[0] is always 0, don't change!
    p = [0, 0.08,0.10,0.11,0.06,0.09,0.22,0.34]
    E, root = optTree(p)
    for i in E[1:]:
        for j in i:
            print(j, end = ", ")
        print()
    for i in root[1:]:
        for j in i:
            print(j, end = ", ")
        print()
    
