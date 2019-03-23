"""Add matrix addition."""

# a = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
# b = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]

a = [[1, 2], [1, 2]]
b = [[1, 2], [1, 1]]

if len(a) == len(b) and len(a[0]) == len(b[0]):
    m = [[0 for j in range(len(a[0]))] for i in range(len(a))]
    for i in range(len(a)):
        for j in range(len(a[0])):
            m[i][j] = a[i][j] + b[i][j]
    print(a)
    print(b)
    print(m)
else:
    print('Non symmetric matrix')
