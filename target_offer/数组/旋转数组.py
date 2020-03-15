# 4
# 1 2 3 4
# 5 6 7 8
# 9 10 11 12
# 13 14 15 16


def solution(matrix, n):
    if n <= 1:
        return matrix
    i, j = 0, n - 1
    while i < j:
        #  如果转多了，可能又转回去了
        for k in range(j - i):
            tmp = matrix[i][i + k]
            matrix[i][i + k] = matrix[j - k][i]
            matrix[j - k][i] = matrix[j][j - k]
            matrix[j][j - k] = matrix[i + k][j]
            matrix[i + k][j] = tmp
        i += 1
        j -= 1
    return matrix


if __name__ == '__main__':
    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

    ans = solution(matrix, 4)

    # print(ans)
