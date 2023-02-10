directions_list = []
with open("day9input.txt") as fh:
    for line in fh:
        if line != "\n":
            line = line.strip("\n")
            lineList = line.split(" ")
            directions_list.append([lineList[0],int(lineList[1])])

for a in directions_list:
    print (a)


# t only moves if h and t are not next to or diagonal from each other

#this function checks if t is close enough to h
def checkT(h_coordinates,t_coordinates):
    hx = h_coordinates[0]
    hy = h_coordinates[1]
    tx = t_coordinates[0]
    ty = t_coordinates[1]
    if hx == tx and hy == ty:
        return True
    if hx == tx or hy == ty: # check vertical or horizontal
        if abs(ty-hy) == 1 or abs(tx-hx) == 1:
            return True
        else:
            return False
    else: # checks diagonal
        if abs(ty-hy) == 1 and abs(tx-hx) == 1:
            return True
        else:
            return False

#print (checkT([2,3],[0,3]))

# rows = y
# col = x
# this function moves t so that it will be close to h
# if checkT() ==False then apply this function
# returns a list, each element is the h coord and then t coord
# this only moves T and the coordinates of H are already updated before coming into this function
def moveT(h_coordinates,t_coordinates,eachDirection,t_postions_list):
    hx = h_coordinates[0]
    hy = h_coordinates[1]
    tx = t_coordinates[0]
    ty = t_coordinates[1]
    direction = eachDirection[0]
    distance = eachDirection[1]
    if direction == "R":
        for a in range(0,distance):
            hx += 1
            if checkT([hx,hy],[tx,ty]) == False: # h and t aren't touching anymore
                if ty != hy: # h and t in diff rows, need to move T diagonally
                    if hy > ty:
                        ty += 1
                    else:
                        ty -= 1
                    tx += 1
                else: # in same row
                    tx += 1
                if [tx,ty] not in t_postions_list:
                    t_postions_list.append([tx, ty])


    elif direction == "L":
        for a in range(0, distance):
            hx -= 1
            if checkT([hx, hy], [tx, ty]) == False:  # h and t aren't touching anymore
                if ty != hy:  # h and t in diff rows, need to move T diagonally
                    if hy > ty:
                        ty += 1
                    else:
                        ty -= 1
                    tx -= 1
                else:  # in same row
                    tx -= 1

                if [tx, ty] not in t_postions_list:
                    t_postions_list.append([tx, ty])
    elif direction == "U":
        for a in range(0,distance):
            hy += 1
            if checkT([hx,hy],[tx,ty]) == False: # h and t aren't touching anymore
                if tx != hx: # h and t in diff rows, need to move T diagonally
                    if hx > tx:
                        tx += 1
                    else:
                        tx -= 1
                    ty += 1
                else: # in same row
                    ty += 1

                if [tx,ty] not in t_postions_list:
                    t_postions_list.append([tx, ty])
    elif direction == "D":
        for a in range(0, distance):
            hy -= 1
            if checkT([hx, hy], [tx, ty]) == False:  # h and t aren't touching anymore
                if tx != hx:  # h and t in diff rows, need to move T diagonally
                    if hx > tx:
                        tx += 1
                    else:
                        tx -= 1
                    ty -= 1
                else:  # in same row
                    ty -= 1

                if [tx, ty] not in t_postions_list:
                    t_postions_list.append([tx, ty])

    return t_postions_list,[hx,hy],[tx,ty]

h_coordinates = [0,0]
t_coordinates = [0,0]
t_positions_list = [[0,0]]
#print (moveT([0,0],[0,0],["R",4],[])[0])
#print ("###################")
for direction in directions_list:
    all_list = moveT(h_coordinates,t_coordinates,direction,t_positions_list)
    t_positions_list = all_list[0]
    h_coordinates = all_list[1]
    t_coordinates = all_list[2]
    #print (direction)
    #print(t_positions_list)


#print (checkT([2,4],[4,3]))
#print ("##################")
print (len(t_positions_list))
#print (t_positions_list)

