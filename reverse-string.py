'''
Write a program that takes in a line of text as input, and outputs that line of text in reverse. The program repeats, ending when the user enters "Done", "done", or "d" for the line of text.

Ex: If the input is:
    Hello there
    Hey
    done
then the output is:
    ereht olleH
    yeH
'''

word = input()

while word != 'Done' and word != 'done' and word != 'd':
    drow = ''
    for i in range(len(word)):
        c = abs(i - (len(word) - 1) )
        drow += word[c]
    print(drow)
    word = input()