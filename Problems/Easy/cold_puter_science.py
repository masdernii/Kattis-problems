n = int(input())
items = [int(x) for x in input().split()]
cnts = 0
for i in range(n):
    if items[i] < 0:
        cnts += 1
print(cnts)