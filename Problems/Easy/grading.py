a, b, c, d, e = input().split()
a = int(a)
b = int(b)
c = int(c)
d = int(d)
e = int(e)
grade = int(input())

if grade >= a:
    print("A")
elif grade >= b:
    print("B")
elif grade >= c:
    print("C")
elif grade >= d:
    print("D")
elif grade >= e:
    print("E")
else:
    print("F")