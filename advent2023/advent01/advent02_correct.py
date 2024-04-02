
with open("C:\\Users\\IPernev\\PycharmProjects\\advent\\advent2023\\advent01\\input.txt", "r") as file:
    contents = file.read()

data = contents.split("\n")
list = []
digits = {"one": "1", "two":"2", "three": "3", "four":"4", "five":"5", "six":"6", "seven": "7", "eight": "8", "nine": "9"}

for element in data:

    number1, number2 = '', ''
    numstring1, numstring2 = "", ""
    index1, index2 = 0, 0

    for ch in element:
        index1 += 1
        if ch.isdigit():
            number1 = ch
            break

        else:
            numstring1 += ch
            for digit in digits:
                if digit in numstring1:
                    print(numstring1)
                    number1 = digits[digit]
                    break

    for ch in element[::-1]:

        if (len(element) - index2) == index1:
            break
        index2 += 1

        if ch.isdigit():
            number2 = ch
            break
        else:
            numstring2 += ch
            for digit in digits:
                if digit in numstring1[::-1]:
                    number2 = digits[digit]
                    break

    endnumber = int(number1+number2)
    list.append(endnumber)

print(list)
print(sum(list))

def find_num_in_string(string):
