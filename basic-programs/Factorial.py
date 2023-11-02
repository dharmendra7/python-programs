num = 2

sum = 1
for value in range(1,num+1):
    sum = sum * value

print(sum)



"""Second Logic"""

num = 6

def factorial(n):
    
    if n == 1 or n == 0:
        return 1  
    else: 
        print(factorial(n-1))
        return n * factorial(n-1)

print(factorial(6))