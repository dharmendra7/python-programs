l1 = [1, 2, 3, 4, 5, 6]
ele_to_check = 3

# Logic 1
if ele_to_check in l1:
    print(f"{ele_to_check} is exists")

# Logic 2
for i in l1:
    if ele_to_check == i:
        print(f"{ele_to_check} is exist at {l1.index(ele_to_check)}")


# Logic 3
result = any(item in l1 for item in l1)
print(result)


del l1[:]
print(l1)
