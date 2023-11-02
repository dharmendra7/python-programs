"""
Input : list1 = [“a”, “b”, “c”, “d”, “e”, “f”, “g”, “h”, “i”]
           list2 = [ 0,   1,   1,    0,   1,   2,   2,   0,   1]
Output : [‘a’, ‘d’, ‘h’, ‘b’, ‘c’, ‘e’, ‘i’, ‘f’, ‘g’]

Input : list1 = [“g”, “e”, “e”, “k”, “s”, “f”, “o”, “r”, “g”, “e”, “e”, “k”, “s”]
            list2 = [ 0,   1,   1,    0,   1,   2,   2,   0,   1]
Output : [‘g’, ‘k’, ‘r’, ‘e’, ‘e’, ‘g’, ‘s’, ‘f’, ‘o’]
"""

# Logic 1
list1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
list2 = [ 0,   1,   1,    0,   1,   2,   2,   0,   1]

newlist1 = []
newlist2 = []
zipped_pair = zip(list2, list1)
for i, _ in sorted(zipped_pair):
    newlist1.append(i)
    newlist2.append(_)

print(newlist1)
print(newlist2)


