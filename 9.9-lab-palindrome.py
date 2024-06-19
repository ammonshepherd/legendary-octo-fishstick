'''
A palindrome is a word or a phrase that is the same when read both forward and backward. Examples are: "bob," "sees," or "never odd or even" (ignoring spaces). Write a program whose input is a word or phrase, and that outputs whether the input is a palindrome.

Ex: If the input is:
    bob
the output is:
    palindrome: bob
Ex: If the input is:
    bobby
the output is:
    not a palindrome: bobby
Hint: Start by removing spaces. Then check if the string equals itself in reverse.
'''

# get the input
phrase = input()

# take out all the spaces
no_spaces = phrase.replace(" ", "")
# reverse the phrase
esarhp = reversed(no_spaces)

# put the characters back together
backwards = ''
for c in esarhp:
    backwards += c

# compare the original with the reversed
if no_spaces == backwards:
    print(f'palindrome: {phrase}')
else:
    print(f'not a palindrome: {phrase}')

