# https://codeforces.com/problemset/problem/158/A

row1 = input().split()

row2 = input().split()

target_position = int(row1[1])
count = 0

for i in row2:
    if int(i) >= int(row2[target_position - 1]) and int(i) != 0:
        count += 1

print(count)
