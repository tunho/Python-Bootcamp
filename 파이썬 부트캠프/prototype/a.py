import turtle

# 화면 설정
screen = turtle.Screen()
screen.bgcolor("white")

# Turtle 객체 생성
t = turtle.Turtle()

# 첫 번째 그림: 원 그리기
t.penup()
t.goto(-100, 0)  # 원의 위치로 이동
t.pendown()
t.circle(50)

# 두 번째 그림: 사각형 그리기
t.penup()
t.goto(100, 0)  # 사각형의 위치로 이동
t.pendown()
for _ in range(4):
    t.forward(100)
    t.left(90)

# 세 번째 그림: 삼각형 그리기
t.penup()
t.goto(0, -150)  # 삼각형의 위치로 이동
t.pendown()
for _ in range(3):
    t.forward(100)
    t.left(120)

# 화면을 유지
turtle.done()
