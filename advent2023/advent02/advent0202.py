with open("C:\\Users\\IPernev\\PycharmProjects\\advent\\advent2023\\advent02\\input.txt", "r") as file:
    contents = file.read()

games = contents.split("\n")
game_products = []
for game in games:

    metadata, data = game.split(":")[0], game.split(":")[1]
    game_id = int(metadata.split(" ")[1])
    subgame = data.split(";")
    maxcubes = {"red":1, "green":1, "blue":1}

    for cubes_info in subgame:
        for cube_instance in cubes_info.split(","):
            cube_instance.strip(" ")
            cube_number, cube_color = int(cube_instance.split(" ")[1]), cube_instance.split(" ")[2]
            if maxcubes[cube_color] <= cube_number:
                maxcubes[cube_color] = cube_number


    product = 1
    for num in  maxcubes.values():
        product *= num
    game_products.append(product)

sum(game_products)