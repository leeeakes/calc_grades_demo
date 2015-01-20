from statistics import mean

def student_means(cohort, drop_lowest=False):
    """Given a dictionary of students and all their grades, return the mean
    grade for each student in a new dictionary."""
    if drop_lowest:
        cohort = {student: sorted(grades)[1:]
                  for (student, grades)
                  in cohort.items()}

    return {student: mean(grades)
            for (student, grades)
            in cohort.items()}


def student_grades(cohort, drop_lowest=False):
    """Given a dictionary of students and all their grades, return the letter
    grade for each student in a new dictionary."""
    return {student: letter_grade(grade)
            for (student, grade)
            in student_means(cohort, drop_lowest).items()}


def letter_grade(numerical_grade):
    """Given a numerical grade, return the correct letter grade for it.

    A = 90+
    B = [80, 90)
    C = [70, 80)
    D = [60-69)
    F = < 60
    """
    if numerical_grade >= 90:
        return "A"
    elif numerical_grade >= 80:
        return "B"
    elif numerical_grade >= 70:
        return "C"
    elif numerical_grade >= 60:
        return "D"
    else:
        return "F"

if __name__ == '__main__':
    cohort1 = {
        'Avery': [63, 62, 41, 66, 84, 82, 73, 89, 69, 75],
        'Blake': [79, 97, 78, 78, 74, 69, 80, 100, 74, 70],
        'Casey': [93, 97, 99, 95, 98, 91, 96, 99, 100, 88],
        'Dakota': [71, 65, 72, 65, 24, 100, 84, 71, 59, 50],
        'Elliot': [84, 73, 90, 72, 69, 93, 61, 65, 81, 98],
        'Fox': [80, 91, 90, 80, 83, 73, 84, 89, 84, 84],
        'Gale': [41, 7, 64, 60, 78, 48, 73, 50, 69, 89]
    }

    for (student, grade) in student_means(cohort1).items():
        print("{student}: {grade}".format(student=student, grade=grade))
