character_list = []
with open("day6input.txt") as fh:
    for line in fh:
        if line!="\n":
            for a in line:
                if a != "\n":
                    character_list.append(a)

#print (character_list)
mini_list = character_list[0:14]
#print (mini_list)
for character in range(13, len(character_list)):
    #print (mini_list)
    temp_list = []
    temp_var = 0

    for a in mini_list:
        if a in temp_list:
            temp_var = 1
        temp_list.append(a)
    if temp_var == 1:
        mini_list.remove(mini_list[0])
        mini_list.append(character_list[character])
    else:
        print(character)
        break