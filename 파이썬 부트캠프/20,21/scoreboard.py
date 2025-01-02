import turtle

class MultipleTurtles:
    def __init__(self):
        # 여러 개의 Turtle 객체 생성
        self.turtle1 = turtle.Turtle()
        self.turtle2 = turtle.Turtle()
        self.turtle3 = turtle.Turtle()

    def draw_shapes(self):
        # 첫 번째 Turtle로 원 그리기
        self.turtle1.penup()
        self.turtle1.goto(-100, 0)
        self.turtle1.pendown()
        self.turtle1.circle(50)

        # 두 번째 Turtle로 사각형 그리기
        self.turtle2.penup()
        self.turtle2.goto(100, 0)
        self.turtle2.pendown()
        for _ in range(4):
            self.turtle2.forward(100)
            self.turtle2.left(90)

        # 세 번째 Turtle로 삼각형 그리기
        self.turtle3.penup()
        self.turtle3.goto(0, -150)
        self.turtle3.pendown()
        for _ in range(3):
            self.turtle3.forward(100)
            self.turtle3.left(120)

# 실행
if __name__ == "__main__":
    screen = turtle.Screen()
    screen.bgcolor("white")

    # 클래스 인스턴스화
    mt = MultipleTurtles()
    mt.draw_shapes()

    # 화면을 유지
    turtle.done()
