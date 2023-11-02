"""
Input : str = "hello geeks for geeks 
          is computer science portal" 
        k = 4

Output : hello geeks geeks computer 
         science portal

Explanation : The output is list of all 
words that are of length more than k.
"""

str = "hello geeks for geeks is computer science portal" 
k = 4
nw = []
for i in str.split(" "):
    if len(i) >= k:
        nw.append(i)

print((" ").join(nw))