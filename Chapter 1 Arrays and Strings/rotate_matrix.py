def rotate_matrix(matrix):
    s = len(matrix)
    ans = []
    for i, m in enumerate(matrix):
        row = []
        l = s - 1
        for j, n in enumerate(m):
            row.append(matrix[l][i])
            l = l - 1
        ans.append(row)
    return ans


matrix = [[1, 9, 6],
          [3, 6, 7],
          [6, 7, 5]]


print(rotate_matrix(matrix))
