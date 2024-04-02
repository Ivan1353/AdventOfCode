from word2number import w2n

with open("C:\\Users\\IPernev\\PycharmProjects\\advent\\advent2023\\advent01\\input.txt", "r") as file:
    contents = file.read()

data = contents.split("\n")
list = []
digits = {"one": 1, "two":2, "three": 3, "four":4, "five":5, "six":6, "seven": 7, "eight": 8, "nine": 9}
for element in data:
    number1, number2 = "", ""
    strink1, strink2 = "", ""
    index1, index2 = 0,0

    for ch in element:
        index1 += 1
        if ch.isdigit():
            number1 = ch
            break

        else:
            strink1 += ch
            try:
                number1 = w2n.word_to_num(strink1)
                break
            except ValueError:
                continue

    for ch in element[::-1]:
        print("element")
        if (len(element) - index2) == index1:
            break
        index2 += 1
        if ch.isdigit():
            number2 = ch
            break
        else:
            strink2 += ch
            try:
                number2 = w2n.word_to_num(strink2[::-1])
                break
            except ValueError:
                continue

    number_end = int(str(number1)+str(number2))
    list.append(number_end)

print(sum(list))