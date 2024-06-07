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

    # if any average is above 100% set it to 100%
    if homework_average > 100:
        homework_average = 100
    if quiz_average > 100:
        quiz_average = 100
    if midterm_average > 100:
        midterm_average = 100
    if final_average > 100:
        final_average = 100

    # calculate course average based on student status
    TOTAL_POINTS = HOMEWORK_MAX + QUIZZES_MAX + MIDTERM_MAX + FINAL_MAX
    if status == 'UG':
        homework_total = ((homework / HOMEWORK_MAX) * 100) * 0.20
        quiz_total = ((quiz / QUIZZES_MAX) * 100) * 0.20
        midterm_total = ((midterm / MIDTERM_MAX) * 100) * 0.30
        final_total = ((final / FINAL_MAX) * 100) * 0.30
        grade_average = homework_total + quiz_total + midterm_total + final_total
    elif status == 'G':
        homework_total = ((homework / HOMEWORK_MAX) * 100) * 0.15
        quiz_total = ((quiz / QUIZZES_MAX) * 100) * 0.05
        midterm_total = ((midterm / MIDTERM_MAX) * 100) * 0.35
        final_total = ((final / FINAL_MAX) * 100) * 0.45
        grade_average = homework_total + quiz_total + midterm_total + final_total
    elif status == 'DL':
        homework_total = ((homework / HOMEWORK_MAX) * 100) * 0.05
        quiz_total = ((quiz / QUIZZES_MAX) * 100) * 0.05
        midterm_total = ((midterm / MIDTERM_MAX) * 100) * 0.40
        final_total = ((final / FINAL_MAX) * 100) * 0.50
        grade_average = homework_total + quiz_total + midterm_total + final_total

    if grade_average >= 90.0:
        grade = "A"
    elif 80.0 <= grade_average < 90.0:
        grade = "B"
    elif 70.0 <= grade_average < 80.0:
        grade = "C"
    elif 60.0 <= grade_average < 70.0:
        grade = "D"
    else:
        grade = "F"

    # print out results
    print(f"Homework: {homework_average:2.1f}%")
    print(f"Quizzes: {quiz_average:.1f}%")
    print(f"Midterm: {midterm_average:.1f}%")
    print(f"Final: {final_average:.1f}%")
    print(f"{status} average: {grade_average:.1f}%")
    print("Course grade:", grade)
else:
    print("Error: student status must be UG, G or DL")