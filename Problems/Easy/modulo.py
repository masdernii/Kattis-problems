mod42 = [0] * 42
for i in range(10):
    mod42[int(input()) % 42] += 1
cnt = 0
for i in range(42):
    if mod42[i] > 0:
        cnt += 1
print(cnt)
