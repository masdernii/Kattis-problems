x = float(input())
y = int(input())
sum = 0
for i in range(y):
    line = input()
    a, b = line.split()
    a = float(a)
    b = float(b)
    sum += a * b
print(sum*x)
