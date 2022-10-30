def bin_search(matrix, target):
    def search_in_row(row, left=-1, right=len(matrix[0])-1):
        while left + 1 < right:
            mid = (right + left)//2
            if matrix[row][mid] < target:
                left = mid
            else:
                right = mid
        return right
    found_index = -1
    for row_it in range(len(matrix)):
        if matrix[row_it][0] > target:
            #print(f"BIN SEARCH: ROW {row_it} breaked, element not found")
            break
        if matrix[row_it][-1] < target:
            #print(f"BIN SEARCH: ROW {row_it} skipped")
            continue
        a = search_in_row(row_it)
        if matrix[row_it][a] == target:
            found_index = a
            #print(f"BIN SEARCH: ROW {row_it} breaked, element found")
            break
    if found_index == -1:
        #print("BIN SEARCH: ELEMENT NOT FOUND")
        return -1, -1
    return row_it, found_index

