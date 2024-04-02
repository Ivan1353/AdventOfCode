import math
with open("C:\\Users\\IPernev\\PycharmProjects\\advent\\advent2023\\advent06\\input.txt", "r") as file:
    contents = file.read()

all_ways_to_win = []

strings = contents.split("\n")
lists = []
for string in strings:
    ls = []
    elements = string.split(" ")
    for element in elements:
        if element.isdigit():
            ls.append(int(element))
    lists.append(ls)

races = dict(zip(lists[0], lists[1]))

for record_time in races:

    ways_to_win = 0
    speed = 0
    for push_time in range(1, record_time+1):
        speed += 1
        my_race_time = races[record_time]//speed
        if my_race_time+push_time < record_time:
            ways_to_win +=1
    all_ways_to_win.append(ways_to_win)


product = math.prod(all_ways_to_win)
print(product)


#########

time, distance = lists[0], lists[1]
time = int(''.join([str(x) for x in time]))
distance = int(''.join([str(x) for x in distance]))

ways_to_win = 0
speed = 0
for push_time in range(1, time+1):
    speed += 1
    my_race_time = distance//speed
    if my_race_time+push_time < time:
        ways_to_win +=1
print(ways_to_win)