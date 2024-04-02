with open("C:\\Users\\IPernev\\PycharmProjects\\advent\\advent2023\\advent02\\input.txt", "r") as file:
    contents = file.read()

info = contents.split("\n")

maxcolors = {"red":12, "green":13, "blue":14}
impossible_counter = 0

for element in info:
    impossible = False
    metadata, data = element.split(":")[0], element.split(":")[1]
    game_id = int(metadata.split(" ")[1])
    games = data.split(";")

    for game in games:
        cubes = game.split(",")
        for cube in cubes:
            cube = cube.strip(" ")
            number, color = int(cube.split(" ")[0]), cube.split(" ")[1]
            if maxcolors[color] < number:
                impossible_counter += game_id
                impossible = True
                break
        if impossible == True:
            break

print(sum(range(100)) - impossible_counter)