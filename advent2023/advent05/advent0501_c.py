with open("C:\\Users\\IPernev\\PycharmProjects\\advent\\advent2023\\advent05\\input.txt", "r") as file:
    contents = file.read()

strings = contents.split("\n\n")
almanac = []
seeds = strings[0].split(": ")
seeds = list(map(int, seeds[1].split(" ")))

for string in strings[1:]:
    metadata, data = string.split(":")[0], string.split(":")[1]
    data = data.split("\n")
    while '' in data:
        data.remove('')
    data = [x.split(' ') for x in data]
    data = [[int(string) for string in inner_list] for inner_list in data]
    almanac.append(data)


for seed in seeds:
    +