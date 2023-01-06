import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")


image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


answer_state = screen.textinput(title = "Guess the State", prompt="What is another state's name?")
formatted_state = answer_state.title()

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
found = data[data.state == formatted_state]
count = 0
guessed_states = []
states_to_learn = []
while count < 50:
    if formatted_state in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(float(data.x[data.state == formatted_state]), float(data.y[data.state == formatted_state]))
        t.write(f"{formatted_state}")
        guessed_states.append(formatted_state)
        count+=1
        answer_state = screen.textinput(title=f"{count}/50 correct", prompt="What is another state's name?")
        formatted_state = answer_state.title()
    elif formatted_state == "Exit":
        for state in all_states:
            if state not in guessed_states:
                states_to_learn.append(state)
        states_to_learn_clean = ' \n'.join(states_to_learn)
        with open("states_to_learn.csv", mode="w") as file:
            file.write(states_to_learn_clean)
        screen.bye()
        break
    else:
        answer_state = screen.textinput(title=f"{count}/50 correct", prompt="What is another state's name?")
        formatted_state = answer_state.title()


screen.exitonclick()
