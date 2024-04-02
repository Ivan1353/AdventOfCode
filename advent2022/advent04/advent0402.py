with open("C:\\Users\\IPernev\\PycharmProjects\\advent\\advent2022\\advent04\\input.txt", "r") as file:
    contents = file.read()

data = contents.split("\n")
pairs = [x.split(",") for x in data]
ls = []
counter = 0
for sub in pairs:
    ls2 = []
    for subsub in sub:
        ls3 = list(map(int, subsub.split("-")))
        ls2.append(ls3)
#    if (ls2[0][0] <= ls2[][] and ls2[0][1] >= ls2[1][0]) or (ls2[][] <= ls2[][] and ls2[1][1]>=ls2[0][0]):
#counter += 1
    if (ls2[0][0] <= ls2[1][1] and ls2[0][1] >= ls2[1][0]) or (ls2[1][0] <= ls2[0][1] and ls2[1][1]>=ls2[0][0]):
        counter += 1

print(counter)