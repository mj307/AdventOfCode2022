stacks = [["R","N","F","V","L","J","S","M"],["P","N","D",'Z','F','J','W','H'], ["W",'R','C','D','G'],['N','B','S'],
          ['M','Z','W','P','C','B','F','N'],['P','R','M','W'],['R','T','N','G','L','S','W'],['Q','T','H','F','N','B','V'],['L','M','H','Z','N','F']]

allInstructions = []
with open("day5input.txt") as fh:
    for line in fh:
        if line != "\n":
            instructions = line.strip("\n").split(" ")
            instructions.remove("move")
            instructions.remove("from")
            instructions.remove("to")
            allInstructions.append(instructions)
# how much you want to remove -- what stack to remove from -- what stack to put it in
for a in allInstructions:
    print (a)
l = [9]
print (l[-1])
for eachInstruction in allInstructions:
    amount = int(eachInstruction[0])
    moveFrom = int(eachInstruction[1])
    moveTo = int(eachInstruction[2])
    moveList = stacks[moveFrom - 1][len(stacks[moveFrom - 1])-amount:]
    for a in moveList:
        stacks[moveTo - 1].append(a)
        stacks[moveFrom - 1].pop()
    print (stacks)
    print ("######")

message = ""
for a in stacks:
    message += a[-1]

print (message)