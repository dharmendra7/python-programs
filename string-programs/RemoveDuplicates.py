"""
Input : geeksforgeeks 
Output : geksfor
"""


s = "geeksforgeeks"

unique = []
duplicate = []

for i in s:
    if i not in unique:
        unique.append(i)
    elif i not in duplicate:
        duplicate.append(i)

print(("").join(unique))
print(duplicate)