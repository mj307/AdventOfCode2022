input_list = []
with open("day10input.txt") as fh:
    for line in fh:
        if line != "\n":
            line = line.strip("\n")
            if "noop" in line:
                input_list.append(line)
            else:
                lineList = line.split(" ")
                input_list.append([lineList[0], int(lineList[1])])


cycle = 0
register_value = 1
sum_signal = 0
cycle_list = [20,60,100,140,180,220]
for each in input_list:
    cycle += 1
    if each != "noop":
        if cycle in cycle_list:
            sum_signal += (register_value*cycle)
        cycle += 1
        if cycle in cycle_list:
            sum_signal += (register_value*cycle)
        amount = each[1]
        register_value += amount

    else:
        if cycle in cycle_list:
            sum_signal += (register_value * cycle)

print (sum_signal)