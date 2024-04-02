with open("C:\\Users\\IPernev\\PycharmProjects\\advent\\advent2022\\advent03\\input.txt", "r") as file:
    contents = file.read()
import string

data = contents.split("\n")
tuple_list = [(str[:len(str)//2], str[len(str)//2:]) for str in data]
intersection_list = [set(t[0]).intersection(set(t[1])) for t in tuple_list]
list_strings = [list(x)[0] for x in intersection_list]

alphabet = [letter for letter in string.ascii_lowercase + string.ascii_uppercase]
value_dict = {x: y for x, y in zip(alphabet, range(1,53))}

list_values = [value_dict[key] for key in list_strings]
sum(list_values)