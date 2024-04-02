import pandas as pd

with open("C:\\Users\\IPernev\\PycharmProjects\\advent\\advent2022\\advent08\\input.txt", "r") as file:
    contents = file.read()

data = [list(x) for x in contents.split("\n")]
#data = pd.DataFrame(data)
curr = 0

for rownum in range(len(data)):
    for colnum in range(len(rownum)):
        curr =         