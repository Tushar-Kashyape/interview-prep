def set_zeroes(matrix):
    m = len(matrix)
    n = len(matrix[0])
    zero_col_track = []

    for i in range(m):
        flag = False

        for j in range(n):
            if matrix[i][j] == 0:
                zero_col_track.append(j)
                flag = True

        if flag: matrix[i] = [0] * n

    for i in range(m):
        for j in zero_col_track:
            matrix[i][j] = 0

    return matrix


# matrix = [[1,1,1],[1,0,1],[1,1,1]]
matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
print(set_zeroes(matrix))