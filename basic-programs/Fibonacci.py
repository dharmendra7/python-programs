# import time
# number = 5

# if number > 0:
#     sum = 0
#     for i in range(0, number):
#         # sum = (i+1) + sum
#         index = i + (i+1)
#         sum = index + sum

#         print(f"sum {sum}--- i+1 {i+1}") 
#         time.sleep(2)
#         print(sum)
#     print(sum)

# Function for nth Fibonacci number

def Fibonacci(n):
	if n<= 0:
		print("Incorrect input")
	# First Fibonacci number is 0
	elif n == 1:
		return 0
	# Second Fibonacci number is 1
	elif n == 2:
		return 1
	else:
		return Fibonacci(n-1)+Fibonacci(n-2)

# Driver Program

print(Fibonacci(5))
