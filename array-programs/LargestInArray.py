l1 = [10, 20, 30]

largest = l1[0]
for value in range(len(l1)):
    if value < len(l1) - 1:
        print(value)
        if l1[value] < l1[value+1]:
            largest = l1[value+1]

        else:
            largest = l1[value]

print(f"Largest in list is {largest}") 


"""Using the max function"""

print(f"Using the max function the largest number is {max(l1)}")