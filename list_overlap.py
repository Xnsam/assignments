"""Print list with no duplicates."""


len_l1 = int(input('Enter the size of list 1 \n'))
len_l2 = int(input('Enter the size of list 2 \n'))

l1 = []
l2 = []

for i in range(0, len_l1):
    l1.append(int(input('Enter element {} \n'.format(i))))

for i in range(0, len_l2):
    l2.append(int(input('Enter element {} \n'.format(i))))
l1.extend(l2)

print(list(set(l1)))
