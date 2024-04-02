with open("C:\\Users\\IPernev\\PycharmProjects\\advent\\advent2023\\advent05\\input.txt", "r") as file:
    contents = file.read()

strings = contents.split("\n\n")
almanac = {}
dictionaries = []
locations = []

seeds = strings[0].split(": ")
seeds = list(map(int, seeds[1].split(" ")))


for string in strings[1:]:
    metadata, data = string.split(":")[0], string.split(":")[1]
    data = data.split("\n")
    while '' in data:
        data.remove('')
    data = [x.split(' ') for x in data]
    data = [[int(string) for string in inner_list] for inner_list in data]
    almanac[metadata] = data


for ratio in almanac.values():
    dictionary = {}
    for ratio_instance in ratio:
        print(ratio_instance)
        destination, source, range_ = ratio_instance[0], ratio_instance[1], ratio_instance[2]
        for x in range(range_):
            dictionary[source] = destination+x
            print(dictionary)
        dictionaries.append(dictionary)

for seed in seeds:
    for dictionary in dictionaries:
        if seed in dictionary:
            seed = dictionary[seed]
        else:
            continue
    locations.append(seed)

print(min(locations))