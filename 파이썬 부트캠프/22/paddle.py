from turtle import Turtle

class Paddle(Turtle) : 
    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(x,y)
    def up(self):
        y = self.ycor() 
        y += 20
        self.sety(y)
    def down(self):
         y = self.ycor() 
         y -= 20
         self.sety(y)

        