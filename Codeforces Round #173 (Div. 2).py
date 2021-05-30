# https://codeforces.com/problemset/problem/282/A

row = int(input())

x = 0

for i in range(row):
    if '+' in input():
        x += 1
    else:
        x -= 1

print(x)
