l1 = [1,2,3,4,5,6]

# l1.reverse()
print(len(l1))


#Logic 2

if len(l1) == 1:
    print(l1)
    
elif len(l1) == 2:
    l1[0], l1[1] = l1[1], l1[0]

# l1 = [1,2,3,4,5,6,7,8,9]
else:
    for i in range(len(l1)-1):
        if i < len(l1)/2:
            l1[i] , l1[(len(l1)-1)-i] = l1[(len(l1)-1)-i] , l1[i]

print(l1)