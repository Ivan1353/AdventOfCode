with open("C:\\Users\\IPernev\\PycharmProjects\\advent\\advent2023\\advent01\\input.txt", "r") as file:
    contents = file.read()

import string

data = contents.split("\n")
list = []
for item in data:
    item = item.strip(string.ascii_lowercase)
    number = int(item[0]+item[-1])
    list.append(number)

print(sum(list))