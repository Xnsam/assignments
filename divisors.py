"""Print the divisors."""

l = int(input('Enter the number \n'))
tmp = [i for i in range(1, l + 1) if l % i == 0]
print(tmp)
