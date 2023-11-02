sentance = "My name is Dharmendra"

splitted_sentance = sentance.split(" ")

new_sentance = []
for i in range(len(splitted_sentance)):
    lth = (len(splitted_sentance) - 1) - i
    new_sentance.append(splitted_sentance[lth])
print(" ".join(new_sentance))

str = "geeks for geeks"

if "geeks" in str:
    print("availabe")