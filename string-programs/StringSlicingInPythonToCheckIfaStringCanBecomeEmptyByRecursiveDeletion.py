"""
Input  : str = "GEEGEEKSKS", sub_str = "GEEKS"
Output : Yes
Explanation : In the string GEEGEEKSKS, we can first 
              delete the substring GEEKS from position 4.
              The new string now becomes GEEKS. We can 
              again delete sub-string GEEKS from position 1. 
              Now the string becomes empty.


Input  : str = "GEEGEEKSSGEK", sub_str = "GEEKS"
Output : No
Explanation : In the string it is not possible to make the
              string empty in any possible manner.
"""

str1 = "GEEGEEKSKS" 
sub_str = "GEEKS"

for i in sub_str:
    if i in str1:
        str1 = str1.replace(i,"")
        print(str1)

print(str1, "str1")


def checkEmpty(input, pattern):
	
	# If both are empty
	if len(input)== 0 and len(pattern)== 0:
		return 'true'

	# If only pattern is empty
	if len(pattern)== 0:
		return 'false'

	while (len(input) != 0):

		# find sub-string in main string
		index = input.find(pattern)

		# check if sub-string founded or not
		if (index ==(-1)):
			return 'false'

		# slice input string in two parts and concatenate
		input = input[0:index] + input[index + len(pattern):]		 
	return 'true'

# Driver program
if __name__ == "__main__":
	input ='GEEGEEKSKS'
	pattern ='GEEKS'
	print (checkEmpty(input, pattern))




input = "GEEGEEKSSGEK"
pattern = "GEEKS"

def checkEmpty(input, pattern):
	
    while(len(input) != 0):
		
        index=input.find(pattern)
        print(index)
        if (index ==(-1)):
            return 'false'
        
        input=input[0:index]+input[index+len(pattern):]
		
    return 'true'

print(checkEmpty(input, pattern))