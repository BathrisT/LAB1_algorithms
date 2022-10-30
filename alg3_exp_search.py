import time


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
    #if matrix[min(start+border, len(matrix)-1)][col] < target: return min(start+border, len(matrix)-1)  # TODO: проверить верность
    return bin_search_in_col(matrix, target, col, left=start+border//2-1, right=min(start+border, len(matrix)-1))

def bin_search_in_row(matrix, target, row, left, right):
    while left + 1 < right:
        mid = (right + left) // 2
        if matrix[row][mid] <= target:
            left = mid
        else:
            right = mid
    return left

def exp_search_in_row(matrix, target, row, start):
    border = 1
    while (start - border) > 0 and matrix[row][start-border] > target:
        border = border * 2
    #if matrix[row][max(0, start-border-1)] > target: return min(start + border, max(0, start-border-1))
    t = bin_search_in_row(matrix, target, row, left=max(0, start-border-1), right=start-border//2)
    #print(max(0, start-border-1), start-border//2, t)
    return t


def exp_search(matrix, target):
    row_it = 0
    col_it = len(matrix[0])-1
    while matrix[row_it][col_it] != target and (row_it <= len(matrix)-1 and col_it >= 0):
        if matrix[row_it][col_it] > target:
            if col_it == 0: break
            #print(f"CHANGING COL ({row_it}, {col_it})")
            col_it = exp_search_in_row(matrix, target, row_it, start=col_it)
            #print("COL CHANGED:", col_it, row_it)
        else:
            if row_it == len(matrix) - 1: break
            #print(f"CHANGING ROW ({row_it}, {col_it})")
            row_it += 1
            #print("ROW CHANGED:", col_it, row_it)
    if matrix[row_it][col_it] == target:
        return row_it, col_it
    else:
        return -1, -1

if __name__ == '__main__':
    target = 5
    a = [[0,1,2,3,4],
         [4,7,8,9,10],
         [5,7,8,11,12]]
    print(exp_search(a, target))