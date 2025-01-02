from turtle import Turtle, Screen
import random

colors = ["burlywood", "lavender blush", "orange red", "sea green" ]

t = Turtle()
a = 90
t.left(90)
t.forward(100)
t.right(90)
for i in range(5) :
 t.color(random.choice(colors))
 for j in range(i+4) :
    t.forward(50)
    t.right(360//(i+4))



  






s = Screen()
s.exitonclick()

