def knap(v,w,W):
    n = len(v) - 1
    OPT = []
    keep = []
    for i in range(n+1):
        OPT.append([])
    for i in range(n+1):
        for j in range(W+1):
            OPT[i].append("N")
    for i in range(n+1):
        keep.append([])
    for i in range(n+1):
        for j in range(W+1):
            keep[i].append("N")
    for i in range(0, n+1):
        OPT[i][0] = 0
    for j in range(0, W+1):
        OPT[0][j] = 0
    for i in range(1, n+1):
        for j in range(1, W+1):
            if (w[i] > j) or ((v[i] + OPT[i-1][j-w[i]]) <= OPT[i-1][j]):
                OPT[i][j] = OPT[i-1][j]
                keep[i][j] = False
            else:
                OPT[i][j] = v[i] + OPT[i-1][j-w[i]]
                keep[i][j] = True
    return OPT, keep

def print_solution(OPT, keep, i, j):
    if i == 0:
        return
    if keep[i][j]:
        print_solution(OPT, keep, i-1, j-w[i])
        print(i)
    else:
        print_solution(OPT, keep, i-1, j)

if __name__ == '__main__':
    #v[0] and w[0] are always 0 don't change!
    v = [0,13,11,15,7,4,9]
    w = [0,9,2,4,3,7,8]
    W = 15
    
    OPT, keep = knap(v,w,W)
    for i in OPT:
        for j in i:
            print(j, end = ", ")
        print()
    for i in keep:
        for j in i:
            print(j, end = ", ")
        print()
    print_solution(OPT, keep, len(v) - 1, W)
    
