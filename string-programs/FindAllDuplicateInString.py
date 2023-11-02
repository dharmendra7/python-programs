"""
Input : hello
Output : l

Input : geeksforgeeeks
Output : e g k s
"""

u_input = "geeksforgeeeks"

uniqueList = []
duplicateList = {}
for i in u_input:
    if i not in uniqueList:
        uniqueList.append(i)
    elif i in duplicateList:
        duplicateList[i] +=1
    else:
        duplicateList[i] = 1

# print(uniqueList)
print(duplicateList)