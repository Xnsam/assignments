"""Printing cows and bulls."""
import random

num = int(input('Enter the length of the number : \t'))

cpu_number = [random.randint(0, 9) for i in range(num)]


count = 0
while count < num:
    i = input('Guess number {} :\t'.format(count + 1))
    if not i:
        break
    if cpu_number[count] == i:
        cpu_number[count] = '<cows>'
    else:
        cpu_number[count] = '<bulls !>'
    count += 1

print(cpu_number)
if cpu_number.count('<bulls !>') < 3:
    print('Good work, but better luck next time')
else:
    print('Bullshit !')
