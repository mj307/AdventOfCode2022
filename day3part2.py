import string
input_list = []
counter = 0
temp_list = []
with open("day3input.txt") as fh:
    for line in fh:
        if line != "\n":
            temp_list.append(line.strip("\n"))
            if len(temp_list) == 3:
                input_list.append(temp_list)
                temp_list = []


#print (input_list)

sum = 0
priority_list = []
for rucksacks in input_list:
    for item in rucksacks[0]:
        if item in rucksacks[1] and item in rucksacks[2]:
            priority_list.append(item)
            break


sum = 0
lowerAlphabet = list(string.ascii_lowercase)
upperAlphabet = list(string.ascii_uppercase)
for item in priority_list:
    if item.islower() == True:
        sum += 1+ lowerAlphabet.index(item)
    else:
        sum += 27+ upperAlphabet.index(item)

print (sum)