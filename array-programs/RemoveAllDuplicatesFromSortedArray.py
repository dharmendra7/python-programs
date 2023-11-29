nums = [1,1,2]

duplicates = []
uniques = []

for item in nums:
    if item not in uniques:
        print(item)
        uniques.append(item)
    elif item not in duplicates:
        duplicates.append(item)
        
print(len(uniques))
print(uniques)


nums[:] = sorted(set(nums))
print(len(nums))


name = "Chris"

if name == 'Bob' or 'Tom' or 'Mike':
    print("Access graned!")
else:    
    print("Access denied!")
