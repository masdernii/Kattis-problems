x = int(input())
sum = 0
for i in range(x):
    y = int(input())
    sum += pow((y//10),(y%10))
print(sum)