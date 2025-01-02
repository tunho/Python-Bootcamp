from turtle import Turtle, Screen
import random

t= Turtle()
t.pensize(10)
t.speed("fastest")
a=200
while a :
    b = random.randint(0,255)
    c = random.randint(0,255)
    d = random.randint(0,255)
    t.color(b/255,c/255,d/255)
    t.forward(10)
    t.right(random.randint(1,360))
    a-= 1

s= Screen()
s.exitonclick()


