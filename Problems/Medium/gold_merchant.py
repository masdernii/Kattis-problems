N, M = input().split()
N = int(N)
M = int(M)
weights = [int(x) for x in input().split()]
values = [int(x) for x in input().split()]
graph = [[0] * N for i in range(N)]
for i in range(M):
    l , m = input().split()
    l = int(l) - 1
    m = int(m) - 1
    graph [l][m] = 1
    graph [m][l] = 1
    for j in range(N):
        if graph[l][j] == 1:
            graph[m][j] = 1
            graph[j][m] = 1   
        if graph[m][j] == 1:
            graph[l][j] = 1
            graph[j][l] = 1
weightsS = []
valuesS = []
moneys = 0
for i in range(N):
    if graph[i][i] == 0:
        moneys += values[i]*weights[i]
    elif graph[i][i] == 1:
        for j in range(i, N):
            if graph[i][j] == 1:
                weightsS.append(weights[j])
                valuesS.append(values[j])
                graph[j][j] = -1
        weightsS.sort()
        valuesS.sort()
        for j in range(len(weightsS)):
            moneys += valuesS[j]*weightsS[j]
        valuesS.clear()
        weightsS.clear()
print(moneys)

