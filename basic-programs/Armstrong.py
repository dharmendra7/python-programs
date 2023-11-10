num = 1634 # armstrong numbers 153, 407, 1634
length = len(str(num))

armstrong_total = 0
for i in str(num):
    armstrong_total += pow(int(i),length)
if num == armstrong_total:
    print(f"{num} is armstrong number")
else:
    print(f"{num} is not armstrong number")