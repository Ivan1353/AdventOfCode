with open("C:\\Users\\IPernev\\PycharmProjects\\advent\\advent2023\\advent03\\input.txt", "r") as file:
    contents = file.read()

data = contents.split("\n")
ls = []
symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "+", "-", "/", "="]

matrix = [list(x) for x in data]

def symbolize(matrix, start_row, start_col, end_row, end_col):
    symbolized = False
    for i in (0, 1):
        for row in range(start_row + i, end_row + 1 + i):
            if row >= len(matrix):  # Prevents index error for rows
                continue
            for j in (0, 1):
                for col in range(start_col + j, end_col + 1 + j):
                    if col >= len(matrix[row]):  # Prevents index error for columns
                        continue
                    if matrix[row][col] in symbols:
                        symbolized = True
    return symbolized

for r in range(len(matrix)):
    numberised = False
    symbolized = False

    for c in range(len(matrix[r])):

        curr = matrix[r][c]

        if curr.isdigit():

            if numberised==False:
                start_r, start_c = r, c
                number = curr
                numberised = True

            elif numberised == True:
                number += curr
                if c+1==len(matrix[r]):
                    symbolized = symbolize(matrix, start_r, start_c, end_r, end_c)
                    if symbolized:
                        ls.append(int(number))

        elif not curr.isdigit():
            if numberised == True:
                end_r, end_c = r, c

                numberised = False
                symbolized = symbolize(matrix, start_r, start_c, end_r, end_c)
                if symbolized:
                    ls.append(int(number))

print(ls)
print(sum(ls))