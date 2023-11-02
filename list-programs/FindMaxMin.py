"""
Input : list1 = [10, 20, 4]
Output : 4

Input : list2 = [20, 10, 20, 1, 100]
Output : 1

Find the smallest and larges number in list
"""

l1 = [10, 20, 4]

print(min(l1))
print(max(l1))

maximum = l1[0]
for i in range(len(l1)-1):
    if l1[i] < l1[i+1]:
        maximum = l1[i+1]

print(maximum)


"""
Find the second largest in list
"""

l1.sort()
print(l1[-2])

