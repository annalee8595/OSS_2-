def pius(a, b):
    return a + b

def minus(a, b):
    return a - b

def mul(a, b):
    return a * b

def divide(a, b):
    return a / b


if __name__ == '__main__':

    print('\n첫번째 숫자를 입력하세요.')
    input1 = inpput('입력: ')

    print('\n사칙연산 선택')
    act = input('기호: ')

    print('\n두번째 숫자를 입력하세요.')
    input2 = inpput('입력: ')

    if act == '+':
        result = plus(inptu1, input2)

    elif act == '-':
        result = minus(input1, input2)

    elif act == '*':
        result = mul(input1, input2)

    else:
        result = divide(input1, input2)
