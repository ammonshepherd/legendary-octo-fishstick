'''
Write a program that compares two strings given as input. Output the number of characters that match in each string position. The output should use the correct verb (match vs matches) according to the character count.

Ex: If the input is:
    crash
    crush
the output is:
    4 characters match
Ex: If the input is:
    cat
    catnip
the output is:
    3 characters match
Ex: If the input is:
    mall
    saw
the output is:
    1 character matches
Ex: If the input is:
    apple
    orange
the output is:
    0 characters match
'''
string1 = input()
string2 = input()
match = 0

# get the shortest string
if len(string1) > len(string2):
    length = len(string2)
else:
    length = len(string1)

# loop through the shortest string number of times
for i in range(length):
    if string1[i] == string2[i]:
        match += 1

if match != 1:
    print(match, "characters match")
else:
    print("1 character matches")