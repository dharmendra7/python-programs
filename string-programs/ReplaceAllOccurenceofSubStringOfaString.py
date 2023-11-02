"""
Input : test_str = “geeksforgeeks” s1 = “geeks” s2 = “abcd” 
Output : test_str = “abcdforabcd” Explanation : We replace all occurrences of s1 with s2 in test_str. 

Input : test_str = “geeksforgeeks” s1 = “for” s2 = “abcd” 
Output : test_str = “geeksabcdgeeks”
"""

test_str = "geeksforgeeks"
s1 = "for"
s2 = "abcd"

# while(len(test_str)!=0):
#     index = test_str.find(s1)
#     print(index)
#     if geeks
if s1 in test_str:
    test_str = test_str.replace(s1, s2)
    print(test_str)


def replace_substring(test_str, s1, s2):
	# Initialize an empty string to store the result
	result = ""
	# Initialize a variable to keep track of our position in the string
	i = 0
	# Loop through the string one character at a time
	while i < len(test_str):
		# Check if the current substring matches the substring we want to replace
		if test_str[i:i+len(s1)] == s1:
			# If it does, add the replacement substring to the result and move the pointer forward
			result += s2
			i += len(s1)
		else:
			# If it doesn't, add the current character to the result and move the pointer forward
			result += test_str[i]
			i += 1
	# Return the final result
	return result

# test
test_str = "geeksforgeeks"
s1 = "geeks"
s2 = "abcd"
# print(replace_substring(test_str, s1, s2))

i= 0
result = ""
while(i < len(test_str)):
    if test_str[i:i+len(s1)] == s1:
        result += s2
        i += len(s1)
    
    else:
        result += test_str[i]
        i += 1

print(result)