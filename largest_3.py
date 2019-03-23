"""Find the largest amongst 3."""

a = 3
b = 4
c = 2

if a > b:
    if a > c:
        print(a, ' is largest')
    else:
        print(c, ' is largest')
else:
    if b > c:
        print(b, ' is largest')
    else:
        print(c, ' is largest')
