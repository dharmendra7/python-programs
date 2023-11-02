array = [1, 2, 3, 4, 5, 6]

new_array = []
def fun(n):
    if n > 0:
        new_array.append(array[n-1])
        fun(n-1)
    return new_array

print(fun(len(array)))

print(array)

print(array[::-1])
