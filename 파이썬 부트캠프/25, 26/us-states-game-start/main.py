import pandas as pd
import turtle
data = pd.read_csv("./25/us-states-game-start/50_states.csv")
names = data.state.to_list()
print(names)

correct = 0
screen = turtle.Screen()
screen.title("U.S States Games")

screen.addshape("./25/us-states-game-start/blank_states_img.gif")

turtle.shape("./25/us-states-game-start/blank_states_img.gif")
t = turtle.Turtle()
t.hideturtle()
t.penup()
guessed_states = []
while len(guessed_states) < 50:
  answer_state = str(screen.textinput(title=f"{len(guessed_states)}/50 Guess the State", prompt="What's another state's name? ")).title()

  if answer_state == "Exit" :
    missing_states = [state for state in names if state not in guessed_states]
    
    new_data = pd.DataFrame(missing_states)
    new_data.to_csv("state_to_learn.csv")
    break

  if answer_state in names and not answer_state in guessed_states :
    correct += 1
    guessed_states.append(answer_state)
    state_data = data[data.state == answer_state]

    t.goto(int(state_data.x), int(state_data.y))

    t.write(answer_state)
    



screen.exitonclick()