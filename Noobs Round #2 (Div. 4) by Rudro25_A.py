count = int(input())

for i in range(count):
    str_len = input()
    # str_in = input()[0:int(str_len)]
    str_in = input()
    c0 = str_in.count('0')
    c1 = str_in.count('1')
    x = abs(c1 - c0) % 4
    if c0 == c1 or x == 0:
        print('E')
        continue
    if x == 2:
        if x == 2:
            print('W')
            continue
    if c1 > c0:
        if x == 1:
            print('N')
            continue
        if x == 3:
            print('S')
            continue
    else:
        if x == 1:
            print('S')
            continue
        if x == 3:
            print('N')
            continue
