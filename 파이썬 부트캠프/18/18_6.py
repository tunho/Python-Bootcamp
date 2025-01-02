# 원 연속으로 그리기기

from turtle import Turtle, Screen

t = Turtle()
t.speed("fastest")

def draw_cicele() : 
    for _ in range(200) :
        t.circle(100)
        t.penup()
        t.setheading(t.heading()+5)
        t.pendown()
draw_cicele()
s = Screen()
s.exitonclick()