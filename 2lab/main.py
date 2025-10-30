def entr(s):
    answ = {}
    for i in s:
        if i in answ: answ[i] += 1
        else: answ[i] = 1
    return answ

a, b = map(entr, input().split())
if len(a) != len(b):
    print('Количество элементов не равно. Установить все соотношеня невозможно')
for i in a:
    if not a[i] in list(b.values()):
        print(i, '- невозможно найти соответствие', end=' ')
    else:
        for itm, val in b.items():
            if val == a[i]:
                print(f'{i}={itm}', end=' ')
