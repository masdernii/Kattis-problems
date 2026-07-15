n = int(input())
ice = [int(x) for x in input().split()]
ice.sort()
print(ice[n-2])
    