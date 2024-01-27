student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
student_grades = {}


def getCriteria(score):
    if score > 90:
        return "Outstanding"
    elif 80 < score < 91:
        return "Exceeds Expectations"
    elif 70 < score < 81:
        return "Acceptable"
    elif score < 71:
        return "Fail"


for key in student_scores:
    student_grades[key] = getCriteria(student_scores[key])

# 🚨 Don't change the code below 👇
print(student_grades)

#
# Scores 91 - 100: Grade = "Outstanding"
#
# Scores 81 - 90: Grade = "Exceeds Expectations"
#
# Scores 71 - 80: Grade = "Acceptable"
#
# Scores 70 or lower: Grade = "Fail"
