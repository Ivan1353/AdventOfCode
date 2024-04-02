def read_file(filepath):
    with open(filepath, "r") as file:
        contents = file.read()
    return contents.split("\n\n")

def parse_data(data):
    instructions = list(data[0])
    pairs = [line.split(" = ") for line in data[1].split('\n')]
    return instructions, {key: tuple(val.strip("()").split(", ")) for key, val in pairs}

def main():
    strings = read_file("C:\\Users\\IPernev\\PycharmProjects\\advent\\advent2023\\advent08\\input.txt")
    instructions, mappings = parse_data(strings)

    curr_strings = [key for key in mappings if key.endswith("A")]
    steps_counter = 0

    for instruction in instructions:
        steps_counter += 1

        curr_strings = [mappings[element][0] if instruction == "L" else mappings[element][1] for element in curr_strings]

        if all(element.endswith("Z") for element in curr_strings):
            break

    print(steps_counter)

if __name__ == "__main__":
    main()
