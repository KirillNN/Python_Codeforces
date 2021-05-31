# https://codeforces.com/problemset/problem/231/A

row = int(input())

count = 0
for i in range(row):
    data = input()
    if data.count('1') > 1:
        count += 1

print(count)
