import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
states = pandas.read_csv("50_states.csv")
states_list = states.state.to_list()
correct_answers = 0
correct_guesses = []
writer = turtle.Turtle()
writer.ht()

def write_state(coords, state):
    writer.pu()
    writer.goto(coords)
    writer.write(state)


while len(correct_guesses) < 50:
    answer_state = screen.textinput(f"{correct_answers}/50 States Correct", "What's another state's name?").title()
    if answer_state == "Exit":
        break
    for state in states_list:
        if answer_state == state:
            answer = states[states.state == answer_state]
            answer_coord = (float(answer.x), float(answer.y))
            write_state(answer_coord, answer_state)
            if answer_state not in correct_guesses:
                correct_guesses.append(answer_state)
                correct_answers += 1
turtle.mainloop()

with open("states_to_learn.csv", "w") as file:
    for state in states_list:
        if state not in correct_guesses:
            file.write(state + "\n")

