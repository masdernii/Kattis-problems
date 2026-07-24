N, M = input().split()
N = int(N)
M = int(M)
weights = [int(x) for x in input().split()]
values = [int(x) for x in input().split()]
parent = list(range(N))

def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x
def union(x, y):
    rx = find(x)
    ry = find(y)
    
    if rx == ry:
        return

for i in range(M):
    u, v = input().split()
    u = int(u)
    v = int(v)
    union(u, v)
