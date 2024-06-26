'''
A pedometer treats walking 1 step as walking 2.5 feet. Define a function named feet_to_steps that takes a float as a parameter, representing the number of feet walked, and returns the number of steps walked as an integer by using int(). Then, write a main program that reads the number of feet walked as an input, calls function feet_to_steps() with the input as an argument, and outputs the number of steps returned from feet_to_steps().

Use floating-point arithmetic to perform the conversion.

Note: Converting a float to an integer may affect the result's accuracy.

Ex: If the input is:
    150.5
the output is:
    60
The program must define and call the following function:
def feet_to_steps(user_feet)
'''
def feet_to_steps(user_feet):
    return int(user_feet / 2.5)
    
    
if __name__ == '__main__':
    walked = float(input())
    print(feet_to_steps(walked))