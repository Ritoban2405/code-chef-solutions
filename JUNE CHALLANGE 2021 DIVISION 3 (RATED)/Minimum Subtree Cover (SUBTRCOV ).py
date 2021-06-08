#PROBLEM STATEMENT - https: www.codechef.com/JUNE21C/problems/SUBTRCOV

import sys
sys.setrecursionlimit(10**9)
def getFar(node, gr, n):
    ## bfs and get the farthest node
    done = [False]*(n+1)
    fd = -1
    far = None
    qu = [(node, 0)]
    done[node] = True
    while qu:
        nod, dis = qu.pop(0)
        if fd < dis:
            fd = dis
            far = nod
        for cnod in gr[nod]:
            if done[cnod]:
                continue
            done[cnod] = True
            qu.append((cnod, dis+1))
    return far

def fixHeight(nod, par, gr, H):
    isleaf = True
    for cnod in gr[nod]:
        if cnod == par:
            continue
        isleaf = False
        fixHeight(cnod, nod, gr, H)
        H[nod] = max(H[nod], 1 + H[cnod])
    if isleaf:
        H[nod] = 1

def dfs(nod, par, gr, H, li, cur):
    isleaf = True
    mx = 0
    for cnod in gr[nod]:
        if cnod == par:
            continue
        isleaf = False
        mx = max(mx, H[cnod])
    if isleaf:
        li.append(cur)
        return

    c = 0
    for cnod in gr[nod]:
        if cnod == par:
            continue
        if H[cnod] == mx and c == 0:
            dfs(cnod, nod, gr, H, li, cur+1)
            c+=1
        else:
            dfs(cnod, nod, gr, H, li, 1)
def breakIntoLines(nod, par, gr, li, n, cur):
    H = [0]*(n+1)
    fixHeight(nod, par, gr, H)
    dfs(nod, par, gr, H, li, 1)
    
    
def GETSOL(gr, n, k):
    if k==1:
        return 1
    u = getFar(1, gr, n)
    li = []
    breakIntoLines(u, 0, gr, li, n, 1)
    li.sort(reverse = True)
    size = 1
    total = 0
    i = 0
    while total < k:
        size += 1
        total += li[i]
        i+=1
    return size

for case in range(int(input())):
    n, k = map(int, input().split())
    gr = [[] for i in range(n+1)]
    for i in range(n-1):
        u,v = map(int, input().split())
        gr[u].append(v)
        gr[v].append(u)

    chad = GETSOL(gr, n, k)
    print(chad)