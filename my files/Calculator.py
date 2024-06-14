def calculator(num0, num1, op):
    if op == 'plus':
        result = num0 + num1
    elif op == 'minus':
        result = num0 - num1
    elif op == 'multiply':
        result = num0 * num1
    elif op == 'divide':
        result = num0 / num1
    return result

num0 = int(input('pick a number: '))
num1 = int(input('pick a number: '))
op = input('pick an operation (plus, minus, divide, multiply): ')

print(calculator(num0, num1, op))