# https://codeforces.com/contest/1476
count = int(input())

for i in range(count):
    str = input()
    x = list(map(int, str.split()))
    if x[1] % x[0] == 0:
        print(int(x[1] / x[0]))
        continue
    if x[1] / x[0] > 1:
        print(int(x[1] / x[0]) + 1)
        continue
    if x[0] % x[1] == 0:
        print(1)
        continue
    if x[1] / x[0] < 1:
        y = int(x[0] / x[1]) + 1
        x[1] = x[1] * y
        print(int(x[1] / x[0]) + 1)
        continue
