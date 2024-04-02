for def symbolize(matrix, start_row, start_col, end_row, end_col):
    symbolized = False
    for i in (0,1):
        try:
            for row in range(start_row+i, end_row + i):
                for j in (0,1):
                    for col in range(start_col+j, end_col + j):
                        if matrix[row][col] in symbols:
                            symbolized = True
                        except:
                            continue
        except:
            return symbolized
return symbolized