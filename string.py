team="New England Patriots"

letter=team[1]

print(len(team))

print(letter)

print(team[-20])

print(team[3])

prefixes = "JKLMNOPQ"
suffix = "ack"
for letter in prefixes:
    if letter != "O" and letter != "Q":
        print(letter+suffix)
    else:
        print(letter+"u"+suffix)


prefixes = "JKLMNOPQ"
suffix = "ack"
for letter in prefixes:
    if letter not in "OQ":
        print(letter+suffix)
    else:
        print(letter+"u"+suffix)

print(team[0:13])

print(team[::-1])

word="New England Patriots"
count=0
for letter in word.lower():
    if letter == "n":
        count=count+1
print(count)


# print a string without a letter
new_team=""
for letter in team:
    if letter != 'a':
        new_team=new_team+letter

print(new_team)