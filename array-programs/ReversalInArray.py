"""
Input:  arr[] = [1, 2, 3, 4, 5, 6, 7]
         d = 2
Output: arr[] = [3, 4, 5, 6, 7, 1, 2] 
"""
# first Logic

array = [1, 2, 3, 4, 5, 6]
reversal = 7

second_half = array[reversal:]
first_half = array[:reversal]

second_half.extend(first_half)
print(second_half)

print(array[1:4:2])