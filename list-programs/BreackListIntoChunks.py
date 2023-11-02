li = [1,2,3,4,5,6,67,7,9,0,45]

start = 0
end = len(li)
steps = 3

for i in range(start, end, steps):
    print(li[i:i+steps])