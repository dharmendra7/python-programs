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

ls = {i:u_input.count(i) for i in u_input}
print(ls)
# if ls.values > 2:
#     print()
for i in ls:
    if ls[i] > 1:
        print(i)


tuple = [("akash", 10), ("gaurav", 12), ("anand", 14), 
         ("suraj", 20), ("akhil", 25), ("ashish", 30)]
print(dict(tuple))
# for i in tuple:
#     print(dict(i))