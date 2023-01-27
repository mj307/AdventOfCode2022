input_list = []
with open("day7input.txt") as fh:
    for line in fh:
        if line != "\n":
            line = line.strip("$ ")
            input_list.append(line.strip("\n"))

#for a in input_list:
    #print (a)
####################################
print ("#################################################")

directory = {}
current_directory_list = []
current_directory = ""
size_dict = {}
for each in input_list:
    if each != "ls":
        each_list = each.split(" ")
        #print (each_list)
        if each_list[0] == "cd":
            if each_list[1] == "..":
                current_directory = current_directory_list[-1]
                current_directory_list.pop()
            else:
                if each_list[1] not in directory:
                    parent = ""
                    for a in current_directory_list:
                        parent += ":" + str(a)
                    child = parent + ":" + each_list[1]
                    directory[child] = []
                    current_directory = each_list[1]
                    current_directory_list.append(current_directory)
                else:
                    print ("should not come here")
                    current_directory = each_list[1]
                    current_directory_list.append(current_directory)
        #elif each
        elif each_list[0] == "dir":
            parent = ""
            for a in current_directory_list:
                parent += ":" + str(a)
            temp = directory[parent]
            child = parent + ":" + each_list[1]
            temp.append(child)
            directory[parent] = temp
            #directory.setdefault(current_directory,[]).append(temp)

        else: # this is file
            parent = ""
            for a in current_directory_list:
                parent += ":" + str(a)
            temp = directory[parent]
            temp.append({each_list[1]:int(each_list[0])})
            directory[parent] = temp
            #directory.setdefault(current_directory,[]).append(each_list[1])
            #size_dict[each_list[1]] = int(each_list[0])
        #print(directory)


sums_dir_dict = {}
for a in directory:
    print (a, directory[a])

#'''
# size value is now the second part of the file
def findDirSum(dir_name, directory_dictionary):
    sum = 0
    if dir_name in directory_dictionary:
        for each in directory_dictionary[dir_name]:
            if type(each) == dict: # this lets you know it's a file
                for a in each.values():
                    sum += a
            else:
                print ("This is each: "+ each)
                sum += findDirSum(each, directory_dictionary)
    return sum

#print (findDirSum("a", directory, size_dict))
sumList = []

for a in directory:
    print (a)
    sumList.append(findDirSum(a, directory))
    print("#####")

print (sumList)
total_sum = 0
for a in sumList:
    if a <= 100000:
        total_sum += a

print (total_sum)
