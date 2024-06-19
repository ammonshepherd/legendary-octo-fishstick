'''
Write a program that takes in a positive integer as input, and outputs a string of 1's and 0's representing the integer in binary. For an integer x, the algorithm is:

As long as x is greater than 0
   Output x % 2 (remainder is either 0 or 1)
   x = x // 2
Note: The above algorithm outputs the 0's and 1's in reverse order. You will need to write a second function to reverse the string.

Ex: If the input is:
    6
the output is:
    110
The program must define and call the following two functions. Define a function named int_to_reverse_binary() that takes an integer as a parameter and returns a string of 1's and 0's representing the integer in binary (in reverse). Define a function named string_reverse() that takes an input string as a parameter and returns a string representing the input string in reverse.
    def int_to_reverse_binary(integer_value)
    def string_reverse(input_string)
'''
def int_to_reverse_binary(integer_value):
    reverse_binary = ''
    while integer_value > 0:
        reverse_binary += str(integer_value % 2)
        integer_value = integer_value // 2
    return reverse_binary

def string_reverse(input_string):
    drow = ''
    for i in range(len(input_string)):
        c = abs(i - (len(input_string) - 1) )
        drow += input_string[c]
    return drow


if __name__ == '__main__':
    # Type your code here. 
    # Your code must call int_to_reverse_binary() to get 
    # the binary string of an integer in a reverse order.
    # Then call string_reverse() to reverse the string
    # returned from int_to_reverse_binary().
    integer = int(input())
    print(string_reverse(int_to_reverse_binary(integer)))