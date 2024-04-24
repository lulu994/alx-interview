def rotate_2d_matrix(matrix):
    if type(matrix) != list:
        print("Input is not a list")
        return
    if len(matrix) <= 0:
        print("Matrix is empty")
        return
    if not all(map(lambda x: type(x) == list, matrix)):
        print("Matrix contains non-list elements")
        return
    rows = len(matrix)
    cols = len(matrix[0])
    if not all(map(lambda x: len(x) == cols, matrix)):
        print("Matrix rows have inconsistent lengths")
        return
    c, r = 0, rows - 1
    for i in range(cols * rows):
        if i % rows == 0:
            matrix.append([])
        if r == -1:
            r = rows - 1
            c += 1
        matrix[-1].append(matrix[r][c])
        if c == cols - 1 and r >= -1:
            matrix.pop(r)
        r -= 1
