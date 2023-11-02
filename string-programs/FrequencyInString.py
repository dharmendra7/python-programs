"""
Input : test_str = 'Gfg is best' 
Output : {'Gfg': 1, 'is': 1, 'best': 1} 

Input : test_str = 'Gfg Gfg Gfg' 
Output : {'Gfg': 3}
"""


# Logic 1
test_str = 'Gfg Gfg Gfg'

dic = {}
for i in test_str.split(" "):
    count = 0
    for j in test_str.split():
        if i == j:
            count += 1
            dic[i] = count

print(dic)


# Logic 2 Using count() function


res = {key : test_str.count(key) for key in test_str.split()}
print(res)