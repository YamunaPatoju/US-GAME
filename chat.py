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

# Ask user for input
answer = screen.textinput(title="Guess the State", prompt="Enter a state name:").title()

# Check if the answer is in the list of states
if answer in states_list:
    q = turtle.Turtle()  # Create an instance of Turtle
    q.hideturtle()
    q.penup()
    state_data = data[data.state == answer]
    q.goto(state_data.x.item(), state_data.y.item())
    q.write(answer, align="center")

# Keep the window open
screen.mainloop()
