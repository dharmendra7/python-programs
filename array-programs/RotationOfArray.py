array = [1, 2, 3, 5, 6, 7, 8, 9]

# for value in range(len(array)):
temp = array[0]                 
for value in range(len(array)):
    if value < len(array) -1 :
        array[value] = array[value+1]
array[-1] = temp

print(array)    