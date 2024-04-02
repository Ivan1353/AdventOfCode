with open('/advent/advent01/text.txt', 'r') as file:
    content = file.read()

data = content.split("\n")

dict_wins = {"A": "Y", "B": "Z", "C": "X"}
dict_draws = {"A": "X", "B":"Y", "C":"Z"}
dict_loss = {"A": "Z", "B": "X", "C":"Y"}

dict_scores = {"X": 1, "Y": 2, "Z": 3}

dict_conditions = {"X":0, "Y":3, "Z": 6}
def reverse_dict(d):
    return {v: k for k, v in d.items()}

score = 0
for game in data:
    score += dict_conditions[game[2]]
    if game[2] == "X":
        score += dict_scores[dict_loss[game[0]]]
    elif game[2] == "Y":
        score += dict_scores[dict_draws[game[0]]]
    elif game[2] == "Z":
        score += dict_scores[dict_wins[game[0]]]

print(score)