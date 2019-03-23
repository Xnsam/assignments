"""Function to print the day person turns hundred."""

import datetime

name = input('Enter your name \n')
age = int(input('Enter your age \n'))

d = datetime.datetime.now()
left_age = 100 - age
year_100 = d.year + left_age

print('Hi {} you will celebrate 100 years on {} th year'.format(name, year_100))
