x = int(input())
for i in range(x):
    line = input()
    a, b, c = line.split()
    a = int(a)
    b = int(b)
    c = int(c)
    if a < (b -c):
        print("advertise")
    elif a > (b -c):
        print("do not advertise")
    else:
        print("does not matter")
    