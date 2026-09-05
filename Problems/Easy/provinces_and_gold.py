g, s, c = input().split()
g = int(g)
s = int(s)
c = int(c)
total = g*3+s*2+c
if total >= 8:
    print("Province or Gold")
elif total >= 5:
    if total >= 6:
        print("Duchy or Gold")
    else:
        print("Duchy or silver")
elif total >= 2:
    if total >= 3:
        print("Estate or Silver")
    else:
        print("Estate or Copper")
else:
    print("Copper")