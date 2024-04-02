with open("C:\\Users\\IPernev\\PycharmProjects\\advent\\advent2022\\advent05\\input2.txt", "r") as file:
    contents = file.read()

data = contents.split("\n\n")
crates, instructions = data[0], data[1]

rows = crates.strip().split('\n')
num_columns = 9
columns = [[] for _ in range(num_columns)]

for row in rows:
    elements = [elem.strip('[]') for elem in row.split() if elem.strip('[]')]
    for i, elem in enumerate(elements):
        columns[i].append(elem)

for col in columns:
    col.reverse()

instructions = instructions.split("\n")
for instr in instructions:
    instr = instr.split(" ")
    move_count = int(instr[1])
    from_ = int(instr[3])
    to_ = int(instr[5])

    for i in range(move_count):
        try:
            columns[to_-1].append(columns[from_-1].pop())
        except IndexError:
            break

endstring = ""
for ls in columns:
    endstring += ls[-1]

print(endstring)