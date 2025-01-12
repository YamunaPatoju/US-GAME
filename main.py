import turtle
import pandas

# Set up the screen
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Load state data
data = pandas.read_csv("C:\\Users\\DELL\\Desktop\\us game\\50_states.csv")
states_list = data["state"].to_list()
guessed_states = []

# Main game loop
while len(guessed_states) < 50:
    # Ask user for a state name
    answer = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?")

    # Convert the answer to title case for uniform comparison
    answer = answer.title()
    # exit the game
    if answer == "Exit":
        break
    # Check if the user clicked "Cancel" or closed the dialog box
    if answer is None:
        break  # Exit the game if user cancels or closes the input box



    # Check if the guess is correct and not already guessed
    if answer in states_list and answer not in guessed_states:
        guessed_states.append(answer)
        q = turtle.Turtle()
        q.hideturtle()
        q.penup()
        state_data = data[data.state == answer]
        q.goto(state_data.x.item(), state_data.y.item())
        q.write(answer, align="center")


