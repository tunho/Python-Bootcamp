from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0 
        with open("./20, 21, 24/data.txt") as data:
            self.highscore = int(data.read())
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.update()

    def update(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", align=ALIGNMENT, font=FONT)
    def reset(self):
        if self.score > self.highscore :
            self.highscore = self.score
            with open("./20, 21, 24/data.txt", 'w') as file:
                file.write(f"{str(self.score)}")
    def increase_score(self):
        self.score += 1
        self.update()
    
    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over", align=ALIGNMENT, font=FONT)
        self.reset()
        

                
                
                

        
        