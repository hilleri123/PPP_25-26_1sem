

if __name__ == "__main__":
    #словарь из римских в арабский и наоборот
roman_to_arabic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
arabic_to_roman = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
    (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
    (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]

#преобразую римские числа в арабские
def roman_to_int(roman):
    total = 0
    prev_value = 0 #хранит предыдущее значения что бы знать менять или нет
    for symbol in reversed(roman):
        value = roman_to_arabic.get(symbol, 0)
        if value < prev_value:
            total -= value
        else:
            total += value
        prev_value = value
    return total

#преобразования арабского в римские
def int_to_roman(num):
    result = ''
    for value, numeral in arabic_to_roman:
        while num >= value:
            result += numeral
            num -= value
    return result

#операции с римскими числами
def roman_caclulator(roman1,roman2,type_operation):
    try: #нужно что бы обработать случаи которые преведут к ошибке
        num1 = roman_to_int(roman1)
        num2 = roman_to_int(roman2)

        # выполнение операций
        if type_operation == '+':
            result = num1 + num2
        elif type_operation == '-':
            result = num1 - num2
        elif type_operation == '*':
            result = num1 * num2
        elif type_operation == '/':
            if num2 == 0:
                return "на ноль делить нельзя!"
            result = num1 // num2
        else:
            return 'некоректная операция'

        if result <= 0:
            return 'результат не может быть отрицательным'

        #обратное преобразование
        return int_to_roman(result)

    except ValueError:
        return 'не праильно введенныое римское число'


input_roman1 = input('введите первое римское число:, ')
input_roman2 = input('введите второе римское число:, ')
operation = input('введите тип операции:', )

output = roman_caclulator(input_roman1,input_roman2,operation)
print(f"результат: {output}")
