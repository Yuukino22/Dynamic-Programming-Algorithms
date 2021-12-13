def weight_interval(v,p):
    M = []
    n = len(v) - 1
    for i in range(n+1):
        M.append("N")
    keep = []
    for i in range(n+1):
        keep.append("N")
    M[0] = 0
    for j in range(1, n + 1):
        if v[j] + M[p[j]] > M[j-1]:
            M[j] = v[j]+M[p[j]]
            keep[j] = True
        else:
            M[j] = M[j - 1]
            keep[j] = False
    return M, keep

def print_sol(j, keep, p):
    if j == 0:
        return
    if keep[j]:
        print_sol(p[j], keep, p)
        print(j)
    else:
        print_sol(j-1, keep, p)

if __name__ == '__main__':
    # v[0] and p[0] are always 0!
    v = [0,5,4,7,2,3,5,7,4]
    p = [0,0,0,1,2,0,3,5,6]
    M, keep = weight_interval(v,p)
    print_sol(len(v) - 1, keep, p)
    for i in M:
        print(i, end = ", ")
    print()
    for i in keep:
        print(i, end = ", ")
