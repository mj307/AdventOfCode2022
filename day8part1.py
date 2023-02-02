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

edge_count = len(tree_list[0])*2 + (len(tree_list)-2)*2
print (edge_count)

def checkLeft(tree_list,row,col):
    height = tree_list[row][col]
    for a in range(col-1,-1,-1):
        if tree_list[row][a] >= height:
            return False
    return True

def checkRight(tree_list,row,col):
    height = tree_list[row][col]
    for a in range(col+1,len(tree_list[0])):
        if tree_list[row][a] >= height:
            return False
    return True

def checkDown(tree_list,row,col):
    height = tree_list[row][col]
    for a in range(row+1,len(tree_list)):
        if tree_list[a][col] >= height:
            return False
    return True

def checkUp(tree_list,row,col):
    height = tree_list[row][col]
    for a in range(row-1,-1,-1):
        if tree_list[a][col] >= height:
            return False
    return True

tree_vis_count = 0
for row in range(1,len(tree_list)-1):
    for col in range(1, len(tree_list[0])-1):
        #print ()
        if checkUp(tree_list,row,col) == True:
            tree_vis_count += 1
        else:
            if checkDown(tree_list, row, col) == True:
                tree_vis_count += 1
            else:
                if checkLeft(tree_list, row, col) == True:
                    tree_vis_count += 1
                else:
                    if checkRight(tree_list, row, col) == True:
                        tree_vis_count += 1

print (tree_vis_count)

print (tree_vis_count+edge_count)
