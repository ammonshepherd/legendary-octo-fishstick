'''
Write a program whose input is two integers. Output the first integer and subsequent increments of 5 as long as the value is less than or equal to the second integer.

Ex: If the input is:
    -15
    10
the output is:
    -15 -10 -5 0 5 10 
Ex: If the second integer is less than the first as in:
    20
    5
the output is:
    Second integer can't be less than the first.
For coding simplicity, output a space after every integer, including the last. End the output with a newline.
'''

int1 = int(input())
int2 = int(input())

value = int1
if int2 < int1:
    print("Second integer can't be less than the first.")
else:
    while value <= int2:
        print(value, end=' ')
        value = value + 5
    print()