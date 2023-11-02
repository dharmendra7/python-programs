"""
Input : A = “Geeks for Geeks”,  B = “Learning from Geeks for Geeks”
Output : [‘Learning’, ‘from’]

Input : A = “apple banana mango” , B = “banana fruits mango”
Output : [‘apple’, ‘fruits’]
"""

a = "Geeks for Geeks"
b = "Learning from Geeks for Geeks"
# a = "apple banana mango"
# b = "banana fruits mango"

uncomonword = []

la = a.split(" ")
lb = b.split(" ")

for i in la:
    if i not in b:
        uncomonword.append(i)
        
for i in lb:
    if i not in a:
        uncomonword.append(i)

print(uncomonword)


word_list = ["best", 'CS', 'for'] 
test_str = 'Geeksforgeeks is best for geeks and CS'
# test = test_str
for i in word_list:
    print(i)
    test_str = test_str.replace(i, "gfg")
print(test_str)