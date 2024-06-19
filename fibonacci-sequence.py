'''
The Fibonacci sequence begins with 0 and then 1 follows. All subsequent values are the sum of the previous two, ex: 0, 1, 1, 2, 3, 5, 8, 13. Complete the fibonacci() function, which has an index, n (starting at 0), as a parameter and returns the nth value in the sequence. Any negative index values should return -1.

Ex: If the input is:
    7
the output is:
    fibonacci(7) is 13
Note: Use a for loop and DO NOT use recursion.
'''
def fibonacci(n):
    # if an integer less than zero is entered, then return -1
    if n < 0:
        return -1
    # if the 0 position is wanted, return 0
    elif n == 0:
        return 0
    # if position 1 or 2 are wanted, return 0
    elif n == 1 or n == 2:
        return 1
    else:
        # loop through to the nth position
        for i in range(n):
            # increment i by one because there's no previous number for the 
            # first position
            i += 1
            # if i is less than 2, the 0 or 1st position, the preset 
            # prev1 and prev2
            if i < 2:
                prev1 = 1
                prev2 = 0
            # the fibonacci number is the sum of the previous two numbers
            fib = prev1 + prev2
            # set the first previous number with the second
            prev1 = prev2
            # set the second previous number with the fibonacci number
            prev2 = fib
        # after all the loops, the fibonacci number will be set in 
        # the fib variable
        return fib


if __name__ == '__main__':
    start_num = int(input())
    print(f'fibonacci({start_num}) is {fibonacci(start_num)}')
