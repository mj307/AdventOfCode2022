calorie_list = []
sum = 0
with open("day1input.txt") as fh:
    for line in fh:
        if line != "\n":
            line = line.strip("\n")
            sum += int(line)
        else:
            calorie_list.append(sum)
            sum = 0

print (sorted(calorie_list)[-1])
