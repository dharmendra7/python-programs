n = 5

# Logic 1 
for i in range(n):
    for j in range(n-i):
        print("*", end=" ")
    print()

# Logic 2

for i in range(n):
    for m in range(i, n):
        print("*", end=" ")
    print()


"""
* * * * *
* * * *
* * *
* * 
*
"""