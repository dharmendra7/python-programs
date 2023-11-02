"""
Input : list = [10, 20, 30, 40, 50]
Output : [10, 30, 60, 100, 150]

Input : list = [4, 10, 15, 18, 20]
Output : [4, 14, 29, 47, 67]

find Cumulative sum of a list
"""

# Logic 1
li = [10, 20, 30 ,40, 50]
cummulative = []
summ = 0
for value in li:
    summ = summ + value
    cummulative.append(summ)

print(cummulative)

# Logic 2
cummulates = [sum(li[0:i:1]) for i in range(1,len(li) + 1)]
print(cummulates)