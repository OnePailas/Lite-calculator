print('Привет, этот калькулятор поможет вычесть ответ двух переменных')

oper = '  +   -   *   /'
print(f'Выбери действие: {oper}')
operation = input()


if operation in ['+', '-', '*', '/']:
    num1 = float(input('Введите первое число: '))
    num2 = float(input('Введите второе число: '))
    if operation == '+':
        print('Ответ: ', num1 + num2)
    elif operation == '-':
        print('Ответ: ', num1 - num2)
    elif operation == '*':
        print('Ответ: ', num1 * num2)
    elif operation == '/':
        if num2 == 0:
            print('На ноль делить нельзя')
            num2 = float(input('Введите еще раз второе число: '))
        if num2 > 0:
            print('Ответ: ', num1 / num2)
