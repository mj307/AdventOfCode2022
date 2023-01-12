moves_list = []
with open("day2input.txt") as fh:
    for line in fh:
        if line != "\n":
            line = line.strip("\n")
            moves_list.append(line.split(" "))


score = 0
#print (moves_list)
# rock = 1, paper = 2, scissors = 3
for play in moves_list:
    if play[0] == "A": # rock
        if play[1] == "X": #lose
            score += 0 + 3
        elif play[1] == "Y": # draw
            score += 3 + 1 # rock gives one point
        else:               # win
            score += 6 + 2
    elif play[0] == "B": #paper
        if play[1] == "X":
            score += 0+1
        elif play[1] == "Y":
            score += 3+2
        else:
            score += 6+3

    elif play[0] == "C":
        if play[1] == "X":
            score += 0+2
        elif play[1] == "Y":
            score += 3+3
        else:
            score += 6 + 1

print (score)