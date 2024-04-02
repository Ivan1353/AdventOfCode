with open('/advent/advent01/text.txt', 'r') as file:
    content = file.read()

data = content.split("\n")

dict_wins = {"A": "Y", "B": "Z", "C": "X"}
dict_draws = {"A": "X", "B":"Y", "C":"Z"}
dict_scores = {"X": 1, "Y": 2, "Z": 3}
score = 0
for game in data:
    if dict_wins[game[0]] == game[2]:
        score += 6
    elif dict_draws[game[0]] == game[2]:
        score += 3

    score += dict_scores[game[2]]

print(score)