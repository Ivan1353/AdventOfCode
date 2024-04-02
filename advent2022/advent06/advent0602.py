from collections import deque

with open("C:\\Users\\IPernev\\PycharmProjects\\advent\\advent2022\\advent06\\input.txt", "r") as file:
    contents = file.read()

signal = deque([])
counter = 0

for ch in contents:
    signal.append(ch)
    counter += 1
    if len(signal) == 14:
        if len(signal) == len(set(signal)):
            break
        else:
            signal.popleft()

print(counter)