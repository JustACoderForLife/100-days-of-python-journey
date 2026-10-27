import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
correct = 0
correct_answers = []
states_to_learn = []
game_on = True
while game_on:

    answer_state = screen.textinput(
        title=f"{correct}/50 States Correct", prompt="What is another state's name"
    ).title()
    data = pandas.read_csv("50_states.csv")

    if answer_state == "Exit":
        states_to_learn = [
            state for state in data["state"].to_list() if state not in correct_answers
        ]
        df = pandas.DataFrame(states_to_learn, columns=["States to Learn"])
        df.to_csv("states_to_learn.csv")
        break

    if answer_state in data.state.values:
        correct += 1
        state_data = data[data.state == answer_state]
        new_turtle = turtle.Turtle()
        new_turtle.ht()
        new_turtle.up()
        new_turtle.goto(state_data.x.item(), state_data.y.item())
        new_turtle.write(answer_state)
        correct_answers.append(answer_state)
print(correct)
