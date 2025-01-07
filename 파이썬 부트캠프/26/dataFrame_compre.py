import pandas as pd



student_dics = {"student": ["Angela", "James", "Lily"],
                "score": [56, 76, 98]}

student_data_frame = pd.DataFrame(student_dics)
# 데이터 프레임
print(student_data_frame)

# 데이터 프레임 속성과 속성 값들 출력(처음 부터)
for key, value in student_data_frame.items():
    print(key)
    print(value)

# 행 출력
for (index, row) in student_data_frame.iterrows():
    print(index)
    print(row.student)
    if row.student == "Angela":
        print(row.score)