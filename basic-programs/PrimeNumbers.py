prime_numbers = []
for value in range(20):
    if value > 1:
        for i in range(2, int(value/2)+1):
            if value % i == 0:
                print(f"{value} is not prime number")
                break
        else:
            prime_numbers.append(value)
            print(f"{value} is prime number")

print(f"################### {prime_numbers} ######################## ")


"""Check whether a number is prime or not"""
prime_numbers =[]
num = 11
# If given number is greater than 1
if num > 1:
    # Iterate from 2 to n / 2
    for i in range(2, int(num/2)+1):
        # If num is divisible by any number between
        # 2 and n / 2, it is not prime
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")

print(prime_numbers)
"""Print all the prime numbers"""

n = 11
prime_numbers = []
for i in range(11):
    if i > 1:
        for j in range(2, int(i/2)+1):
            if i % j == 0:
                break
                # pass
        else:
            prime_numbers.append(i)

print(prime_numbers)