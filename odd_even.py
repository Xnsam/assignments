"""Print add or even."""

a = int(input('Enter the range \n'))
odd = []
even = []
for i in range(0, a):
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

print(even)
print(odd)
