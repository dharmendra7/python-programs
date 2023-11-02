"""
Input : Geeks$For$Geeks
Output : String is not accepted.

Input : Geeks For Geeks
Output : String is accepted
"""

s1 = "Geeks$For$Geeks"
s2 = "Geeks For Geeks"

import re

regex = re.compile("[@%$]")

search = regex.search(s2)
if search is None:
    print("Given string is not contain the special characters")
else:
    print("Given string is contain special charaters")