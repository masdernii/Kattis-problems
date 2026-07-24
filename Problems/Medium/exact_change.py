a = input()
b = input()
count = 0
if len(b) > len(a):
    print(len(b))
else:
    for i in range(len(b)):
        if a[i] == '1' and b[i] == '1':
            count += 1
        if a[i] == '0' and b[i] == '1':
            count += len(b)-i
            break
    print(count)