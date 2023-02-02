tree_list = []
with open("day8input.txt") as fh:
    for line in fh:
        if line != "\n":
            temp = []
            for each in line:
                each = each.strip("\n")
                if each !="":
                    temp.append(int(each))
            tree_list.append(temp)

for a in tree_list:
    print (a)

def checkLeft(tree_list,row,col):
    height = tree_list[row][col]
    sum = 0
    for a in range(col-1,-1,-1):
        if tree_list[row][a] < height:
            sum += 1
        else:
            return sum+1
    return sum

def checkRight(tree_list,row,col):
    height = tree_list[row][col]
    sum = 0
    for a in range(col+1,len(tree_list[0])):
        if tree_list[row][a] < height:
            sum += 1
        else:
            return sum + 1
    return sum

def checkDown(tree_list,row,col):
    height = tree_list[row][col]
    sum = 0
    for a in range(row+1,len(tree_list)):
        if tree_list[a][col] < height:
            sum += 1
        else:
            return sum + 1
    return sum

def checkUp(tree_list,row,col):
    height = tree_list[row][col]
    sum = 0
    for a in range(row-1,-1,-1):
        if tree_list[a][col] < height:
            sum += 1
        else:
            return sum + 1
    return sum


highest_scene_score = 0
for row in range(1,len(tree_list)-1):
    for col in range(1, len(tree_list[0])-1):
        scenic_score = checkUp(tree_list,row,col)*checkDown(tree_list,row,col)*checkLeft(tree_list,row,col)*checkRight(tree_list,row,col)
        if scenic_score > highest_scene_score:
            highest_scene_score = scenic_score

print (highest_scene_score)