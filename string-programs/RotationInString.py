"""
Input : s = "GeeksforGeeks"
        d = 2
Output : Left Rotation  : "eksforGeeksGe" 
         Right Rotation : "ksGeeksforGee"  


Input : s = "qwertyu" 
        d = 2
Output : Left rotation : "ertyuqw"
         Right rotation : "yuqwert"
"""

s = "GeeksforGeeks"
d = 2

# Left Rotation
first = s[:d]
second = s[d:]
print(second+first)

# Right Rotation

first = s[:-d]
last = s[-d:]
print(last+first)