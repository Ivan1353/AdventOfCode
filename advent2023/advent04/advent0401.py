with open("C:\\Users\\IPernev\\PycharmProjects\\advent\\advent2023\\advent04\\input.txt", "r") as file:
    contents = file.read()

data = contents.split("\n")
total_sum = 0
cards_dictionary = {}

for card in data:
    info_1, info_2 = card.split(":")[0], card.split(":")[1]

    winning_nums, actual_nums = info_2.split("|")[0], info_2.split("|")[1]

    winning_nums = [x for x in winning_nums.split(" ") if x != '']
    actual_nums = [x for x in actual_nums.split(" ") if x != '']

    intersection = len([x for x in actual_nums if x in winning_nums])

    if intersection == 0:
        total_sum += 0
    else:
        total_sum += 2**(intersection-1)

print(total_sum)
