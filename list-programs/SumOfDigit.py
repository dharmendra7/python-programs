li = [12,34,54,65,1]

summ = []
for i in li:
    total = 0
    for j in str(i):
        total+= int(j)
    summ.append(total)

print(summ)

my_list = [1, 2, 3, 4, 5, 
           6, 7, 8, 9] 
start = 0
end = len(my_list) 
step = 4
for i in range(start, end, step):
    print(i)
    x = i 
    print(my_list[x:x+step]) 