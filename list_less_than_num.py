"""Print list number less than given number."""


l = int(input('Enter the length of list \n'))
ls = []
for i in range(l):
    ls.append(int(input("Enter number {} \n".format(i + 1))))

thresh = int(input('Enter threshold number \n'))

print([i for i in ls if i > thresh])
