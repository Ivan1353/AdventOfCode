with open("C:\\Users\\IPernev\\PycharmProjects\\advent\\advent2023\\advent08\\input.txt", "r") as file:
    contents = file.read()

strings = contents.split("\n\n")
steps_counter = 0
curr_string = 'AAA'

instructions = list(strings[0])

lists_ = strings[1].split('\n')
lists_ = [x.split(" = ") for x in lists_]
dicts_ = {}
for x in lists_:
    key_ = x[0]
    s = x[1]
    s = s.strip("()")
    elements = s.split(",")
    values_ = tuple(element.strip() for element in elements)
    dicts_[key_] = values_

while True:

    for instruction in instructions:
        steps_counter += 1
        if instruction == "L":
            curr_string = dicts_[curr_string][0]
        elif instruction == "R":
            curr_string = dicts_[curr_string][1]

        if curr_string == "ZZZ":
            break
    if curr_string == "ZZZ":
        break

print(steps_counter)