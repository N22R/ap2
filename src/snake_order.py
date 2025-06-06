def snake_order(matrix):
    result = []
    for row_index, row in enumerate(matrix):
        if row_index % 2 == 0:
            result.extend(row)
        else:
            result.extend(row[::-1])
    return result