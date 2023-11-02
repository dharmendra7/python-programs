li = [1,2,3,1,3,4,2,5,6,7,8,9,1]

# Logic 1:
print(len(li))
duplicate = []
for i in range(len(li)):
    for j in range(i+1, len(li)):
        if li[i] == li[j]:
            if li[i] not in duplicate:
                duplicate.append(li[i])

print(duplicate)


# Logic 2

uniqueList = []
duplicateList = []

for value in li:
    if value not in uniqueList:
        uniqueList.append(value)
    elif value not in duplicateList:
        duplicateList.append(value)

print(uniqueList)
print(duplicateList)
