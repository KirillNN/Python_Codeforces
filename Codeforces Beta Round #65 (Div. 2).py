# https://codeforces.com/problemset/problem/71/A

count = int(input())

for i in range(count):
    w = input()
    if len(w) > 10:
        print(w[0] + str(len(w) - 2) + w[-1])
    else:
        print(w)
