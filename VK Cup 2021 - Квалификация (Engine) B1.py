# https://codeforces.com/contest/1531/problem/B1

row = int(input())

data = []
count = 0

for i in range(row):
    tmp = input().split()
    data.append([int(tmp[0]), int(tmp[1])])

for index, first in enumerate(data):
    for second in data[index + 1:]:
        if any(i in first for i in second):
            count += 1

print(count)
