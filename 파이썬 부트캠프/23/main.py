import time
from turtle import Screen
from player import Player, FINISH_LINE_Y
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

scoreboard = Scoreboard()
player = Player()
carmanager = CarManager()

screen.listen()

screen.onkey(player.move, 'w')
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    if player.ycor() >= FINISH_LINE_Y:
       player.success()
       scoreboard.level_up()
       carmanager.level_up()
       
       
    for i in carmanager.all_cars:
        if player.distance(i) < 20:
            game_is_on = False
            scoreboard.game_over()
            
            
    carmanager.create_cars()
    carmanager.car_move()
    


screen.exitonclick()
