import math
from collections import Counter
with open("C:\\Users\\IPernev\\PycharmProjects\\advent\\advent2023\\advent07\\input.txt", "r") as file:
    contents = file.read()

data = contents.split("\n")

type_bet_list = []
strength = ['A', 'K', 'Q', "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
def is_stronger(a,b):
    count_a, count_b = Counter(a), Counter(b)
    if count_a.most_common(1)[0][1] > count_b.most_common(1)[0][1]:
        return True
    elif count_a.most_common(1)[0][1] < count_b.most_common(1)[0][1]:
        return False
    else:
        if len(set(a))<len(set(b)):
            return False
        elif len(set(a))>len(set(b)):
            return True
        elif len(set(a)) == len(set(b)):
            for i in range(len(a)):
                if strength.index(a[i])<strength.index(b[i]):
                    return True
                elif strength.index(a[i])>strength.index(b[i]):
                    return False
                else:
                    continue

for game in data:

    cards, bet = game.split(" ")[0], int(game.split(" ")[1])

    if len(type_bet_list) == 0:

        type_bet_list.append({cards:bet})
    else:
        for i in range(len(type_bet_list)):
            cards_i =list((type_bet_list[i]).keys())[0]
            cards, cards_i = list(cards), list(cards_i)
            if is_stronger(cards, cards_i):
                cards = "".join(cards)
                dictionary_to_append = {cards:bet}
                type_bet_list.insert(i, dictionary_to_append)
                break
            else:
                continue

sum = 0
for i in range(len(type_bet_list)):
    j = list(type_bet_list[i].values())[0]
    k = len(type_bet_list)-i
    sum += k*j

print(sum)