'''
MP2P1 - Schedule information
Program Specifications

Write a program that creates a dictionary containing course numbers and the room numbers of the rooms where the courses meet. The dictionary should have the following key-value pairs:
Course Number (key) Room Number (key)
CS101               3004
CS102               4501
CS103               6755
NT110               1244
CM241               1411

The program should also create a dictionary containing course numbers and the names of the instructors that teach each course. The dictionary should have the following key-value pairs:
Course Number (key) Instructor (value)
CS101               Haynes
CS102               Alvarado
CS103               Rich
NT110               Burke
CM241               Lee

The program should also create a dictionary containing course numbers and the meeting times of each course. The dictionary should have the following key-value pairs:
Course Number (key) Meeting Time (value)
CS101               8:00am
CS102               9:00am
CS103               10:00am
NT110               11:00am
CM241               1:00pm

The program should let the user enter a course number, and then it should display the course's room number, instructor, and meeting time.

Look carefully at the following sample run of the program. In particular, notice the wording of the messages and the placement of spaces and colons. Your program's output must match this.
Sample Run (User input shown in bold)
Enter a class name:
    CS101

    Class: CS101
    Room: 3004
    Instructor: Haynes
    Time: 8:00am
'''
# Create the dictionary for class number (key) and room number (value)
rooms = {
    'CS101': '3004',
    'CS102': '4501',
    'CS103': '6755',
    'NT110': '1244',
    'CM241': '1411'
}

# create dictionary for class number (key) and instructor (value)
instructors = {
    'CS101': 'Haynes',
    'CS102': 'Alvarado',
    'CS103': 'Rich',
    'NT110': 'Burke',
    'CM241': 'Lee'
}

# create dictionary for class number (key) and meeting time (value)
meeting_times = {
    'CS101': '8:00am',
    'CS102': '9:00am',
    'CS103': '10:00am',
    'NT110': '11:00am',
    'CM241': '1:00pm'
}

# get user input and put into variable
class_input = input()

# not included in instructions, but check if the class in the rooms dictionary
# and only output info if it is found.
if class_input in rooms:
    print(f'Class: {class_input}')
    print(f'Room: {rooms[class_input]}')
    print(f'Instructor: {instructors[class_input]}')
    print(f'Time: {meeting_times[class_input]}')