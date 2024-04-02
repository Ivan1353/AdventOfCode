with open("C:\\Users\\IPernev\\PycharmProjects\\advent\\advent2022\\advent03\\input.txt", "r") as file:
    contents = file.read()

data = contents.split("\n")
data_sets = list(map(set, data))
groups = [data_sets[i:i+3] for i in range(0, len(data_sets), 3)]
intersections = []
for group in groups:
    intersction = group[0].intersection(group[1], group[2])
    intersections.append(list(intersction)[0])

alphabet = [letter for letter in string.ascii_lowercase + string.ascii_uppercase]
value_dict = {x: y for x, y in zip(alphabet, range(1,53))}

list_values = [value_dict[key] for key in intersections]

print(sum(list_values))