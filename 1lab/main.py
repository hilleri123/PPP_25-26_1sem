from random import randint

try:
    m, n = map(int, input('hall size\n').split())
    a = int(input('seats in row\n'))
    hall = [[randint(0, 1) for _ in range(n)] for _ in range(m)]
    print(*hall, sep='\n')
    for i in range(m):
        for j in range(n - a + 1):
            if hall[i][j:j + 3] == [0] * 3:
                hall[i][j], hall[i][j + 1], hall[i][j + 2] = 1, 1, 1
    print(*hall, sep='\n')
except:
    print('wrong input')
