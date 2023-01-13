import string
input_list = []
with open("day3input.txt") as fh:
    for line in fh:
        if line != "\n":
            input_list.append(line.strip("\n"))

#print (input_list)
rucksack_list = []
for eachValue in input_list:
    compartment1 = eachValue[0:int(len(eachValue)/2)]
    compartment2 = eachValue[int(len(eachValue) / 2):]
    rucksack_list.append([compartment1,compartment2])

#for each in rucksack_list:
    #print (each)

priority_list = []
for compartments in rucksack_list:
    for item in compartments[0]:
        if item in compartments[1]:
            priority_list.append(item)
            break

#print (priority_list)
sum = 0
lowerAlphabet = list(string.ascii_lowercase)
upperAlphabet = list(string.ascii_uppercase)
for item in priority_list:
    if item.islower() == True:
        sum += 1+ lowerAlphabet.index(item)
    else:
        sum += 27+ upperAlphabet.index(item)

print (sum)