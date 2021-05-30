# https://codeforces.com/contest/1531/problem/A

row = int(input())

color = 'blue'
unlock = True

for i in range(row):
    message = input()
    if message == 'lock':
        unlock = False
        continue
    if message == 'unlock':
        unlock = True
        continue
    if message != 'lock' and message != 'unlock' and unlock:
        color = message

print(color)
