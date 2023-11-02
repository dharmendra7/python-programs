"""
Input : malayalam
Output : Yes

Input : geeks
Output : No
"""

# Logic 1
string = "khokho"

if string == string[::-1]:
    print("String is palindrome")
else:
    print("String is not palindrome")


# symmentric
half = int(len(string)/2)
firsthalf = string[:half]
secondhalf = string[half:]

if firsthalf == secondhalf:
    print("String is symmentrical")
else:
    print("String is not symmentrical")

