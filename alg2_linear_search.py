def linear_search(matrix, target):
    row_it = 0
    col_it = len(matrix[0])-1
    while matrix[row_it][col_it] != target and (row_it <= len(matrix)-1 and col_it >= 0):
        if matrix[row_it][col_it] < target:
            if row_it == len(matrix) - 1: break
            row_it += 1
        elif matrix[row_it][col_it] > target:
            if col_it == 0: break
            col_it -= 1
    if matrix[row_it][col_it] == target:
        return row_it, col_it
    else:
        return -1, -1

if __name__ == '__main__':
    pass