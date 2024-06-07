HOMEWORK_MAX = 800.0
QUIZZES_MAX = 400.0
MIDTERM_MAX = 150.0
FINAL_MAX = 200.0

status = input("Student Status (UG = undergrad, G = graduate, DL = distance learner): ")

if (status == 'UG') or (status == 'G') or (status == "DL"):
    # get inputs all on one line
    homework, quiz, midterm, final = input().split()

    # convert them all to floats
    homework = float(homework)
    quiz = float(quiz)
    midterm = float(midterm)
    final = float(final)

    # calculate averages
    homework_average = (homework / HOMEWORK_MAX) * 100
    quiz_average = (quiz / QUIZZES_MAX) * 100
    midterm_average = (midterm / MIDTERM_MAX) * 100
    final_average = (final / FINAL_MAX) * 100

    # print out results
    print(f"Homework: {homework_average:2.1f}%")
    print(f"Quizzes: {quiz_average:.1f}%")
    print(f"Midterm: {midterm_average:.1f}%")
    print(f"Final: {final_average:.1f}%")
else:
    print("Error: student status must be UG, G or DL")