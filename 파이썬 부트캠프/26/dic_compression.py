import random
from compression import names  # compression.py의 실행 코드는 실행되지 않음

if __name__ == "__main__":
    student_score = {student: random.randint(1, 100) for student in names}
    print(student_score)

    passed_students = {student: score for student, score in student_score.items() if score >= 60}
    print(passed_students)



# import random 
# from compression import names 


# if __name__ == "__main__" :
#     student_score = {student: random.randint(1,100) for student in names}
#     print(student_score)
