from calc_grades import *

cohort = {"August": [91, 90, 92],
          "Sam": [85, 87, 89],
          "India": [75, 80, 82]}

def test_student_means_simple():
    means = student_means(cohort)
    assert means["August"] == 91


def test_student_means_drop_lowest():
    means = student_means(cohort, drop_lowest=True)
    assert means["Sam"] == 88


def test_grade():
    assert letter_grade(92) == "A"
    assert letter_grade(90) == "A"
    assert letter_grade(89.9) == "B"
    assert letter_grade(85) == "B"
    assert letter_grade(74) == "C"
    assert letter_grade(67) == "D"
    assert letter_grade(59) == "F"
    assert letter_grade(0) == "F"


def test_student_grades():
    grades = student_grades(cohort)
    assert grades["August"] == "A"
    assert grades["India"] == "C"

def test_student_grades_drop_lowest():
    grades = student_grades(cohort, drop_lowest=True)
    assert grades["India"] == "B"
