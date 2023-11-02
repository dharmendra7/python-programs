"""
Input : string = 'My Profile: 
https://auth.geeksforgeeks.org/user/Chinmoy%20Lenka/articles 
in the portal of https://www.geeksforgeeks.org/'

Output : URLs :  ['https://auth.geeksforgeeks.org/user/Chinmoy%20Lenka/articles',
'https://www.geeksforgeeks.org/']

Input : string = 'I am a blogger at https://geeksforgeeks.org'
Output : URL :  ['https://geeksforgeeks.org']
"""

s = """My Profile: https://auth.geeksforgeeks.org/user/Chinmoy%20Lenka/articles 
in the portal of https://www.geeksforgeeks.org/"""
urls = []
res = []
for i in s.split(" "):
    if i.startswith("https") or i.startswith("http"):
        urls.append(i)

    if i.find("https:")==0 or i.find("http:")==0:
            res.append(i)
print(urls)
print(res)