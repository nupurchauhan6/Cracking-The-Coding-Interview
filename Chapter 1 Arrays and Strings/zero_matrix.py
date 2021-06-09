def set_zero(matrix, index):
    for i, m in enumerate(matrix):
        for j, n in enumerate(m):
            if j == index:
                matrix[i][index] = 0
    return matrix


def zero_matrix(matrix):
    first = matrix[0]
    for i, n in enumerate(first):
        if(n == 0):
            matrix[0] = [0]*len(first)
            set_zero(matrix, i)
    return matrix


matrix = [[1, 9, 0, 0, 8], [3, 6, 7, 8, 1], [6, 7, 5, 9, 5]]

print(zero_matrix(matrix))
