"""
Input : [12, 35, 9, 56, 24]
Output : [24, 35, 9, 56, 12]

Input : [1, 2, 3]
Output : [3, 2, 1]

Interchange the first and the last element of List
"""

# Logic 1

l1 = [12, 35, 9, 56, 24]

temp = l1[0]
l1[0] = l1[len(l1)-1]
l1[len(l1)-1] = temp

print(f"Logic 1 {l1}")


# Logic 2

l1 = [1, 2, 3]

l1[0], l1[-1] = l1[-1], l1[0]

print(f"Logic 2 {l1}")