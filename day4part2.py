input_list = []
with open("day4input.txt") as fh:
    for line in fh:
        if line != "\n":
            temp_list = line.strip("\n").split(",")
            temp_elf1 = temp_list[0].split("-")
            elf1 = []
            for a in temp_elf1:
                elf1.append(int(a))
            temp_elf2 = temp_list[1].split("-")
            elf2 = []
            for a in temp_elf2:
                elf2.append(int(a))
            input_list.append([elf1,elf2])

for a in input_list:
    print (a)
print ("#####")

total = 0

def overlap(elfMore, elfLess):
    for each in range(elfMore[0], elfMore[1] + 1):
        for items in range(elfLess[0], elfLess[1] + 1):
            if each == items:
                return True
    return False

for task in input_list:
    elf1 = task[0]
    elf2 = task[1]
    count = 0
    if elf1[1]-elf1[0] > elf2[1] - elf2[0]: # then elf2 length is smaller and shld be completely in elf1
        if overlap(elf1,elf2) == True:
            total += 1
    else:
        if overlap(elf2,elf1) == True:
            total += 1


print (total)