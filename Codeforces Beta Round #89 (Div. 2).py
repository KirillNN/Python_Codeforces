# https://codeforces.com/problemset/problem/118/A

row = input().lower()

result = ''

for letter in row:
    if letter not in 'aoyeui':
        result += '.' + letter

print(result)
