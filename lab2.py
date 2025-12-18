from collections import deque


def check_brackets(s):

    bracket_pairs = {')': '(', '}': '{', ']': '['}

    stack = deque()

    for i, char in enumerate(s):
        if char in bracket_pairs.values():
            stack.append((char, i))

        elif char in bracket_pairs.keys():
            if not stack or stack[-1][0] != bracket_pairs[char]:
                return f'Ошибка в позиции {i + 1}'

            stack.pop()

    if stack:
        # Остались лишние открывающие скобки
        return f'Ошибка в позиции {stack[0][1] + 1}'

    return 'ok'


s = str(input())
print(check_brackets(s))

