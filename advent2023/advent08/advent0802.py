with open("C:\\Users\\IPernev\\PycharmProjects\\advent\\advent2023\\advent08\\input.txt", "r") as file:
    contents = file.read()

strings = contents.split("\n\n")
steps_counter = 0
curr_strings = []

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

curr_strings = [x for x in dicts_ if x.endswith("A")]

to_break = False
while True:

    for instruction in instructions:
        steps_counter += 1

        if instruction == "L":
            for i in range(len(curr_strings)):
                curr_strings[i] = dicts_[curr_strings[i]][0]
        if instruction == "R":
            for i in range(len(curr_strings)):
                curr_strings[i] = dicts_[curr_strings[i]][1]


        to_break = all(element.endswith("Z") for element in curr_strings)

        if to_break == True:
            break
    if to_break == True:
        break


print(steps_counter)

