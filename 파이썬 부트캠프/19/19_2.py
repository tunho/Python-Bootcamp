# turtle 경주

from turtle import Turtle, Screen
import random
COLOR = ["red", "blue", "green", "white", "black", "pink"]



s = Screen()
s.setup(width=500, height=400)
user_bet = s.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color : ")
print(user_bet)

turtle_list = [Turtle(shape="turtle"), Turtle(shape="turtle"), Turtle(shape="turtle"), Turtle(shape="turtle"), Turtle(shape="turtle"), Turtle(shape="turtle")]
for i in range(len(turtle_list)) :
   turtle_list[i].penup()
   turtle_list[i].color(COLOR[i])
   turtle_list[i].goto(x=-230,y=100-40*i)

if user_bet : 
   is_race_on = True
while is_race_on :
   for turtle in turtle_list :
      if turtle.xcor() > 230 :
         print(turtle.pencolor(), "win")
         is_race_on = False
         break
      turtle.forward(random.randint(1,50))


s.exitonclick()