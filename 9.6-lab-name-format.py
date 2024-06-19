'''
Many documents use a specific format for a person's name. Write a program that reads a person's name in the following format:
    firstName middleName lastName (in one line)
and outputs the person's name in the following format:
    lastName, firstInitial.middleInitial.
Ex: If the input is:
    Pat Silly Doe
the output is:
    Doe, P.S.
If the input has the following format:
    firstName lastName (in one line)
the output is:
    lastName, firstInitial.

Ex: If the input is:
    Julia Clark
the output is:
    Clark, J.
'''
full_name = input().split()

if len(full_name) > 2:
    print(f'{full_name[2]},', f'{full_name[0][:1]}.{full_name[1][:1]}.')
else:
    print(f'{full_name[1]},', f'{full_name[0][:1]}.')