def gen_per(elements, prefix=""):
    if len(elements) == 0:
        print(prefix)  #вывод каждой найденной перестановки
    else:
        for i in range(len(elements)):
            cur_elem = elements[i]
            ost_elem = elements[:i] + elements[i + 1:] #оставшиеся элементы после текущего

            gen_per(ost_elem, prefix + str(cur_elem)) #pекурсивно генерируем оставшиеся перестановки

elements = '1234'
print("Все перестановки:", elements)
gen_per(list(elements))
