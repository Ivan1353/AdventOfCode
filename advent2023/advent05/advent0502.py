with open("C:\\Users\\IPernev\\PycharmProjects\\advent\\advent2023\\advent05\\input.txt", "r") as file:
    contents = file.read()

#Parse the data and create variables
strings = contents.split("\n\n")
almanac = []
locations = []
seeds = strings[0].split(": ")
seeds = list(map(int, seeds[1].split(" ")))
paired_seeds = [seeds[i:i + 2] for i in range(0, len(seeds), 2)]
real_seeds = [0]
for pair in paired_seeds:
    for real_seed in range(pair[0], pair[0]+pair[1]):
        real_seeds.append(real_seed)

#create an almanac out of all the data apart from the seed. In every dictionary the key is the source and the
#value is a list with the destination and the range

for string in strings[1:]:
    metadata, data = string.split(":")[0], string.split(":")[1]
    data = data.split("\n")
    while '' in data:
        data.remove('')
    data = [x.split(' ') for x in data]
    data = [[int(string) for string in inner_list] for inner_list in data]
    data_1 = {}
    for ratio_instance in data:
        destination_1, source, range_1 = ratio_instance[0], ratio_instance[1], ratio_instance[2]
        data_1[source] = [destination_1, range_1]
    almanac.append(data_1)

#iterate through each seed and find it's corresponding value in each map
for real_seed in real_seeds:

    implant = real_seed
#for each seed iterate through each map
    for ratio in almanac:
        source_ranges = []
        for ri in ratio:
            destination_2 = ratio[ri][0]
            range_2 = ratio[ri][1]
            source_range = range(ri, ri+range_2)
            if implant in source_range:
                implant = implant+destination_2-ri
                break
            else:
                continue

    locations.append(implant)
print(locations)
print(min(locations))