for i in range(1, 10):
    for j in range(i):
        print('*', end='')
    print()

# 실습1
for i in range(10, 0, -1):
    for j in range(i):
        print('*', end='')
    print()

# 실습2
for i in range(1, 10):
    for j in range(2, 10):
        result = j * i
        print('{} * {} = {}\t'.format(j, i, result), end='')
    print()