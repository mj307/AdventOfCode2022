import math
all_monkey_data = {}
each_monkey_data = {}
with open("day11input.txt") as fh:
    for line in fh:
        if line != "\n":
            if "Monkey" not in line:
                each_monkey_list = line.lstrip(" ").strip("\n").split(":")
                if each_monkey_list[0] == "Starting items":
                    temp = each_monkey_list[1].lstrip(" ").split(",")
                    temp2 = []
                    for a in temp:
                        temp2.append(int(a.strip(" ")))
                    each_monkey_data[each_monkey_list[0]] = temp2
                else:
                    each_monkey_data[each_monkey_list[0]] = each_monkey_list[1].lstrip(" ")

            else:
                x = line.strip("\n")
        else:
            all_monkey_data[x.strip(":")] = each_monkey_data
            each_monkey_data = {}
    all_monkey_data[x.strip(":")] = each_monkey_data
    each_monkey_data = {}

print (all_monkey_data)

monkey_inspection_dict = {}
for a in all_monkey_data:
    monkey_inspection_dict[a] = 0

print (monkey_inspection_dict)

for round in range(0,10000):
    print (round)
    for monkey in all_monkey_data:
        for item in all_monkey_data[monkey]['Starting items'][:]:
            monkey_inspection_dict[monkey] += 1  # where the inspection amount increases
            operation = all_monkey_data[monkey]["Operation"]
            op_instruction = operation.lstrip("new = old ").split(" ")

            if op_instruction[1] == "old":
                new_worry_item = item * item
            else:
                if op_instruction[0] == "+":
                    new_worry_item = item + int(op_instruction[1])
                else:
                    new_worry_item = item * int(op_instruction[1])

            test = int(all_monkey_data[monkey]["Test"].strip("divisible by "))

            if new_worry_item % test == 0:

                next_monkey = all_monkey_data[monkey]["If true"].strip("throw to ").capitalize()

                all_monkey_data[next_monkey]["Starting items"].append(new_worry_item)

            else:
                next_monkey = all_monkey_data[monkey]["If false"].strip("throw to ").capitalize()

                all_monkey_data[next_monkey]["Starting items"].append(new_worry_item)
            all_monkey_data[monkey]['Starting items'].remove(item)

print (monkey_inspection_dict)
product = 1
count = 0
for w in sorted(monkey_inspection_dict, key=monkey_inspection_dict.get, reverse=True):
    if count > 1:
        break
    else:
        product *= monkey_inspection_dict[w]
    count += 1
print (product)