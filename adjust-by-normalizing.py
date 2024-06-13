'''
When analyzing data sets, such as data for human heights or for human weights, a common step is to adjust the data. This adjustment can be done by normalizing to values between 0 and 1, or throwing away outliers.

For this program, adjust the values by dividing all values by the largest value. The input begins with an integer indicating the number of floating-point values that follow. Assume that the list will always contain positive floating-point values.

Output each floating-point value with two digits after the decimal point, which can be achieved as follows:
    print(f'{your_value:.2f}')
Ex: If the input is:
    5
    30.0
    50.0
    10.0
    100.0
    65.0
the output is:
    0.30
    0.50
    0.10
    1.00
    0.65
The 5 indicates that there are five floating-point values in the list, namely 30.0, 50.0, 10.0, 100.0, and 65.0. 100.0 is the largest value in the list, so each value is divided by 100.0.
'''

num_floats = int(input())

# Put the numbers into a list from input
num_list = []
for i in range(num_floats):
    num_list.append(float(input()))

# Find the largest number in the list
largest = 0
for n in range(len(num_list) + 1):
    if num_list[n-1] > largest:
        largest = num_list[n-1]

# print out each value divided by largest
for n in range(len(num_list)):
    print(f"{(num_list[n] / largest):.2f}")