m = int(input())
n = int(input())
sum = 0
for i in range(n):
    x = input()
    for j in range(len(x)):
        if x[j] == '.':
            sum += 1
print(sum /(m*n))