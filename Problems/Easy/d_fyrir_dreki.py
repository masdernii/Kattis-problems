a = int(input())
b = int(input())
c = int(input())
theta = b*b - 4*a*c
if theta > 0:
    print("2")
elif theta == 0:
    print("1")
else:
    print("0")