'''
Given a sorted list of integers, output "Middle item: " followed by the middle integer. Assume the number of integers is always odd.

Ex: If the input is:
    2 3 4 8 11
the output is:
    Middle item: 4
The maximum number of inputs for any test case should not exceed 9. If exceeded, output "Too many inputs".
Hint: First read the data into a list. Then, based on the list's size, find the middle item.
'''

asorted = input().split()


if len(asorted) % 2 != 0 and len(asorted) <= 9:
    print(f'Middle item: {asorted[len(asorted)//2]}')
else:
    print("Too many inputs")