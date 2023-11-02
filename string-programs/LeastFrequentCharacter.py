"""
The original string is : GeeksforGeeks
The minimum of all characters in GeeksforGeeks is : f
"""

s = "GeeksforGeeks"

count_dic = {}
for i in s:
    if i in count_dic:
        count_dic[i] = count_dic[i] + 1 
    else:
        count_dic[i] = 1

print(min(zip(count_dic.values(), count_dic.keys()))[1])

"""
Max Frequent Character
"""
s = "GeeksforGeeks"

count_dic = {}
for i in s:
    if i in count_dic:
        count_dic[i] = count_dic[i] + 1 
    else:
        count_dic[i] = 1

print(max(zip(count_dic.values(), count_dic.keys()))[1])

