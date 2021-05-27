# https://codeforces.com/problemset/problem/1/A
import math

data = input().split()
print(math.ceil(int(data[0]) / int(data[2])) * math.ceil(int(data[1]) / int(data[2])))
