n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
arr = arr[::-1]
for i in range(n):
    print(arr[i])
    