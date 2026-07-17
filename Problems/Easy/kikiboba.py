word = input()
k = 0
b = 0
for i in range(len(word)):
    if word[i] == "k":
        k += 1
    elif word[i] == "b":
        b += 1
if k < b:
    print("boba")
elif k > b:
    print("kiki")
elif k == b and k != 0:
    print("boki")
else:
    print("none")