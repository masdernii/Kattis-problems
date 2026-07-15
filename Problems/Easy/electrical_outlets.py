n = int(input())
for i in range(n):
    O = [int(x) for x in input().split()]
    sum = 1
    for j in range (1, len(O)):
        sum += O[j]-1
    print(sum)
