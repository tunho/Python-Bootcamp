from turtle import Turtle, Screen
import random

t = Turtle()
t.speed(0)
def move_fowards() :
    t.forward(10)
def move_backwards() :
    t.backward(10)
def counter_clockwise() :
    t.setheading(t.heading()+10)
def clockwize() :
    t.setheading(t.heading()-10)
def reset() :
    t.reset()





s = Screen()
s.listen()
s.onkey(key = "w", fun = move_fowards)
s.onkey(key = "s", fun = move_backwards)
s.onkey(key = "a", fun = counter_clockwise)
s.onkey(key = "d", fun = clockwize)
s.onkey(key = "c", fun = reset)
s.exitonclick()

