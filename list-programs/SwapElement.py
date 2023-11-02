"""
Input : List = [23, 65, 19, 90], pos1 = 1, pos2 = 3
Output : [19, 65, 23, 90]

Input : List = [1, 2, 3, 4, 5], pos1 = 2, pos2 = 5
Output : [1, 5, 3, 4, 2]

Swap Two Elements in a List
"""
l1 = [23, 65, 19, 90]
pos1 = 1
pos2 = 3

# Logic 1

l1[pos1], l1[pos2] = l1[pos2], l1[pos1]

print(l1)



# Logic with built-in function
l1 = [23, 65, 19, 90]
pos1 = 1
pos2 = 3

ele1 = l1.pop(pos1)
ele2 = l1.pop(pos2-1)

l1.insert(pos1, ele2)
l1.insert(pos2, ele1)

print(l1)

