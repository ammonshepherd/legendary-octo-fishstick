'''
Many user-created passwords are simple and easy to guess. Write a program that takes a simple password and makes it stronger by replacing characters using the key below, and by appending "!" to the end of the input string.

i becomes 1
a becomes @
m becomes M
B becomes 8
s becomes $
Ex: If the input is:
    mypassword
the output is:
    Myp@$$word!
Hint: Python strings are immutable, but support string concatenation. Store and build the stronger password in the given password variable.
'''

password =  input()

newpass = ''
for c in password:
    if c == 'i':
        c = '1'
    elif c == 'a':
        c = '@'
    elif c == 'm':
        c = 'M'
    elif c == 'B':
        c = '8'
    elif c == 's':
        c = '$'
    newpass += c

newpass = newpass + '!'

print(newpass)