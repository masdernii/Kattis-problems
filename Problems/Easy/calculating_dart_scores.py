n = int(input())

throws = []
for i in range(1, 21):
    throws.append(("single", i, i))
    throws.append(("double", i, 2 * i))
    throws.append(("triple", i, 3 * i))

# One dart
for a in throws:
    if a[2] == n:
        print(a[0], a[1])
        exit()

# Two darts
for a in throws:
    for b in throws:
        if a[2] + b[2] == n:
            print(a[0], a[1])
            print(b[0], b[1])
            exit()

# Three darts
for a in throws:
    for b in throws:
        for c in throws:
            if a[2] + b[2] + c[2] == n:
                print(a[0], a[1])
                print(b[0], b[1])
                print(c[0], c[1])
                exit()

print("impossible")   