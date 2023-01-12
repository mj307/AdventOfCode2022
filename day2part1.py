# a = rock, b = paper, c = scissors
# x ,y,z
moves_list = []
with open("day2input.txt") as fh:
    for line in fh:
        if line != "\n":
            line = line.strip("\n")
            moves_list.append(line.split(" "))

#print (moves_list)
score = 0
for play in moves_list:
    if play[0] == "A":
        if play[1] == "X":
            score += 3+1
        elif play[1] == "Y":
            score += 6+2
        else:
            score += 0+3
    elif play[0] == "B": #paper
        if play[1] == "X": #rock
            score += 0+1
        elif play[1] == "Y": #paper
            score += 3+2
        else:
            score += 6+3

    elif play[0] == "C": #scissors
        if play[1] == "X": #rock
            score += 6+1
        elif play[1] == "Y": #paper
            score += 0+2
        else:
            score += 3+3

print (score)