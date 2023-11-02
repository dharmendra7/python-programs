"""
Input : Geek
        i = 1
Output : Gek

Input : Peter 
        i = 4
Output : Pete
"""

# Logic 1
s = "Peter"
l = 1
ns = []
for i in range(len(s)):
    if i is not l: 
        ns.append(s[i])

print(("").join(ns))

# Logic 2
t = list(s)
t.pop(l)
print(("").join(t))