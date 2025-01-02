from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreborad
import time
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

paddle1 = Paddle(-350, 0)
paddle2 = Paddle(350, 0)
ball = Ball()
scoreborad = Scoreborad()

screen.listen()
screen.onkey(paddle1.up, "w")
screen.onkey(paddle1.down, "s")
screen.onkey(paddle2.up, "Up")
screen.onkey(paddle2.down, "Down")

game_is_on = True
while game_is_on :
  screen.update()
  time.sleep(ball.move_speed)

  ball.move()

  if ball.distance(paddle1) < 50 and ball.xcor() < -320 or ball.distance(paddle2) < 50 and ball.xcor() > 320 :
    ball.bounce_x()
    ball.bounce_y()
     
  if ball.ycor() > 280 or ball.ycor() < -280 :
    ball.bounce_y()
  
  if ball.xcor() > 380 : 
    ball.reset()
    scoreborad.l_point()
  
  if ball.xcor() < -380 :
    ball.reset()
    scoreborad.r_point()
    
    
    
 
     



  
  


screen.exitonclick()