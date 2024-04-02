with open("C:\\Users\\IPernev\\PycharmProjects\\advent\\advent2023\\advent04\\input.txt", "r") as file:
    contents = file.read()

data = contents.split("\n")
cards_dictionary = dictionary = {i: 0 for i in range(1, 214)}

for card in data:
    info_1, info_2 = card.split(":")[0], card.split(":")[1]
    card_id = int([x for x in info_1.split(" ") if x != ''][1])

    winning_nums, actual_nums = info_2.split("|")[0], info_2.split("|")[1]

    winning_nums = [x for x in winning_nums.split(" ") if x != '']
    actual_nums = [x for x in actual_nums.split(" ") if x != '']

    intersection = len([x for x in actual_nums if x in winning_nums])


    for x in range(intersection):
        cards_dictionary[card_id + x] += 1



print(sum(cards_dictionary.values()))