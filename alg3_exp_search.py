def bin_search_in_col(matrix, target, col, left, right):
    while left + 1 < right:
        mid = (right + left) // 2
        if matrix[mid][col] < target:
            left = mid
        else:
            right = mid
    return right

def exp_search_in_col(matrix, target, col, start):
    border = 1
    while start + border < len(matrix) and matrix[start+border][col] < target:
        border = border * 2
    return bin_search_in_col(matrix, target, col, left=start+border//2-1, right=min(start+border, len(matrix)-1))

def bin_search_in_row(matrix, target, row, left, right):
    if target < matrix[row][left]: return left
    elif target > matrix[row][right]: return right
    while left + 1 < right:
        mid = (right + left) // 2
        if matrix[row][mid] <= target:
            left = mid
        else:
            right = mid
    return left

def exp_search_in_row(matrix, target, row, start):
    if matrix[row][0] >= target:
        return 0
    border = 1
    while (start - border) > 0 and matrix[row][start-border] > target:
        border *= 2
    t = bin_search_in_row(matrix, target, row, left=max(0, start-border), right=start-border//2)
    return t


def exp_search(matrix, target):
    row_it = 0
    col_it = len(matrix[0])-1
    matrix_length = len(matrix)
    while matrix[row_it][col_it] != target and (row_it <= matrix_length-1 and col_it >= 0):
        if matrix[row_it][col_it] > target:
            if col_it == 0: break
            col_it = exp_search_in_row(matrix, target, row_it, start=col_it)
        else:
            if row_it == matrix_length - 1: break
            row_it += 1
    if matrix[row_it][col_it] == target:
        return row_it, col_it
    else:
        return -1, -1
