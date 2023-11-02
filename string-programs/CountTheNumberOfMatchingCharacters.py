"""
Input : str1 = 'abcdef'
        str2 = 'defghia'
Output : 4 
(i.e. matching characters :- a, d, e, f)

Input : str1 = 'aabcddekll12@'
        str2 = 'bb22ll@55k'
Output : 5 
(i.e. matching characters :- b, 1, 2, @, k)

"""

str1 = 'abcdefaa'
str2 = 'defghia'

count = 0
for i in str1:
    if i in str2:
        count += 1

print(count)