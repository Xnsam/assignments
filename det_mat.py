"""Determinant of a matrix."""

import numpy as np


def cross_multiply(x):
    """Function to cross multiply."""
    return (x[0][0] * x[1][1]) - (x[0][1] * x[1][0])


def determinant(x):
    """Function to calculate the determinant of x."""
    if len(x) == len(x[0]):
        if len(x) == 2:
            return cross_multiply(x)
        else:
            val = 0
            alt = False
            for i in range(len(x)):
                tmp = x[1:]
                t1, t2 = tmp[0][:], tmp[1][:]
                _ = t1.pop(i), t2.pop(i)
                new_t = [t1, t2]
                print(new_t)
                x_multiply = cross_multiply(new_t)
                if val == 0:
                    val = x[0][i] * x_multiply
                else:
                    if alt:
                        val = val + (x[0][i] * x_multiply)
                        alt = False
                    else:
                        val = val - (x[0][i] * x_multiply)
                        alt = True
            return val
    else:
        return 'matrix is not a square matrix.'


x = [[6, 1, 1], [4, -2, 5], [2, 8, 7]]
determinant(x) == int(np.linalg.det(np.array(x)))
