!lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}

# Add your function below!
def average(numbers):
    total = sum(numbers)
    total = float(total)
    result = total / len(numbers)
    return result
def get_average(student):
    homework = average(student["homework"])
    quizzes = average(student["quizzes"])
    tests = average(student["tests"])
    ave1 = 0.1 * homework
    ave2= 0.3 * quizzes
    ave3 = 0.6 * tests
    final = ave1 + ave2 + ave3
    return final
def get_letter_grade(score):
    if score >= 90 :
        return "A"
    elif score >=80 and score<90:
        return "B"
    elif score >=70 and score <80:
        return "C"
    elif score >=60 and score < 70:
        return "D"
    else :
        return "F"
print get_letter_grade(get_average(lloyd))
def get_class_average(student):
    results=[]
    for student in students:
        get_average(student)
        results.append(get_average(students))
    return average(results)
