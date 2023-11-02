# """
# Input : {‘a’: 100, ‘b’:200, ‘c’:300}
# Output : 600

# Input : {‘x’: 25, ‘y’:18, ‘z’:45}
# Output : 88
# """

# original_dic = {'a' : 100, 'b' : 200}

# print(sum(original_dic.values()))


# # Remove the key

# poped_ele = original_dic.pop('a')
# print(poped_ele)
# print(original_dic)

scoreList = []
for _ in range(int(input())):
    nameList = []
    name = input()
    score = float(input())
    nameList.append(name)
    nameList.append(score)
    
    scoreList.append(nameList)

new_list = []
for i in scoreList:
    new_list.append(i[1])

for i in sorted(new_list):
    print(i)