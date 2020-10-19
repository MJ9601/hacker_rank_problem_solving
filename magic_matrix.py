
import math
import os
import random
import re
import sys

# Complete the formingMagicSquare function below.
def formingMagicSquare(s):
    magic_matrixs = [
        [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
        [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
        [[8, 3, 1], [1, 5, 9], [6, 7, 2]],
        [[4, 3, 8], [9, 5, 1], [2, 7, 6]],
        [[6, 7, 2], [1, 5, 9], [8, 3, 4]],
        [[2, 7, 6], [9, 5, 1], [4, 3, 8]],
        [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
        [[2, 9, 4], [7, 5, 3], [6, 1, 8]]
    ]
    holder = []
    for matrix in magic_matrixs:
        zero_point = 0
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                zero_point += abs(matrix[i][j]-s[i][j])
        
        holder.append(zero_point)

    return (holder)


s = [[2, 5, 4], [4, 6 , 9], [4, 5, 2]]

print(formingMagicSquare(s))