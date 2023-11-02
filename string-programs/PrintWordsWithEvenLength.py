"""
Input: s = "This is a python language"
Output: This is python language

Input: s = "i am laxmi"
Output: am
"""

s = "This is a python language"
newstr = []
for i in s.split(" "):
    if len(i) % 2 == 0:
        newstr.append(i)
    
print(" ".join(newstr))
