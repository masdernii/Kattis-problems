a = 1
b = 0
c = 0
d = 0
str = input()
for i in range(len(str)):
    if str[i] == "A":
        d = a
        a = b
        b = d
    elif str[i] == "B":
        d = b
        b = c
        c = d
    elif str[i] == "C":
        d = a
        a = c
        c = d
if a == 1:
    print("1")
elif b == 1:
    print("2")
elif c == 1:
    print("3")
