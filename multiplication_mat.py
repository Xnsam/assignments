"""Matrix multiplication."""
import numpy as np


# a = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
# b = [[1, 1, 1], [0, 1, 1], [0, 0, 1]]

a = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
b = [[1, 1], [1, 1], [1, 1]]

if len(a[0]) == len(b):
    m = [[0 for j in range(len(b[0]))] for i in range(len(a))]
    for i in range(len(a)):
        for j in range(len(a[0])):
            for k in range(len(b[0])):
                m[i][k] += a[i][j] * b[j][k]
    print(m)
    print(np.dot(np.asarray(a), np.asarray(b)) == np.asarray(m))
else:
    print('Cannot multiply.')

# a = np.array([[1, 2], [1, 2]])
# b = np.array([[1, 1], [1, 1]])
