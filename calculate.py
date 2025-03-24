def pius(a, b):
    return float(a) + float(b)

def minus(a, b):
    return float(a) - float(b)

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

    elif act == '/':
        result = divide(input1, input2)

    print(f'사칙 연산 결과: {result}')
    print("modify1")
    #왜 안되는데
