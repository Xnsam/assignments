"""Function to calculate the operators."""

v1 = int(input('Enter number 1 \n'))
v2 = int(input('Enter number 2 \n'))


operations = ['Add', 'Subtraction', 'Multiply', 'Division', 'Modulo', 'Exponential', 'Root', 'Floor Divide']
for i, v in enumerate(operations):
    print('{}.{}'.format(i + 1, v))
op = int(input('Enter the operation \n'))

if op == 1:
    print('Addition {}'.format(v1 + v2))
elif op == 2:
    if v1 > v2:
        print('v2 greater than v1')
    else:
        print('Addition {}'.format(v1 - v2))
elif op == 3:
    print('Multiplication {}'.format(v1 * v2))
elif op == 4:
    try:
        print('Division {}'.format(v1 / v2))
    except ZeroDivisionError:
        print('Cannot Divide with zero.')
elif op == 5:
    print('Modulo {}'.format(v1 % v2))
elif op == 6:
    print('Exponential {}'.format(v1 ** v2))
elif op == 7:
    print('Root {}'.format(v1 ** (1. / float(v2))))
elif op == 8:
    try:
        print('Division {}'.format(v1 // v2))
    except ZeroDivisionError:
        print('Cannot Divide with zero.')
else:
    print('Incorrect choice.')
