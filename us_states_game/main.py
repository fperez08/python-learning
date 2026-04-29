import turtle
import pandas


# Set up the screen and map
screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Load the states data
states_data = pandas.read_csv("50_states.csv")
states_list = states_data["state"].tolist()
guessed_states = []

# Create a turtle for writing state names
state_writer = turtle.Turtle()
state_writer.hideturtle()
state_writer.speed(0)
state_writer.penup()


def show_score():
    """Display the current score in the window title."""
    score = len(guessed_states)
    screen.title(f"US States Game - {score}/50 states guessed")


def is_valid_guess(user_input):
    """Check if the input is a valid state that hasn't been guessed."""
    user_input = user_input.title()
    
    if user_input not in states_list:
        return False, None
    
    if user_input in guessed_states:
        return False, None
    
    return True, user_input


def write_state_on_map(state_name):
    """Write the state name at its coordinates on the map."""
    state_data = states_data[states_data["state"] == state_name]
    x = int(state_data.x.values[0])
    y = int(state_data.y.values[0])
    
    state_writer.goto(x, y)
    state_writer.write(state_name, align="center", font=("Arial", 7, "normal"))


def game_loop():
    """Main game loop - ask for input until player quits or guesses all states."""
    show_score()
    
    while len(guessed_states) < 50:
        # Prompt for input
        answer = screen.textinput(
            f"Guess the State",
            f"What's another state's name?\n({len(guessed_states)}/50)"
        )
        
        # If user clicks cancel, end the game
        if answer is None:
            break
        
        # Check the guess
        is_valid, state_name = is_valid_guess(answer)
        
        if is_valid:
            guessed_states.append(state_name)
            write_state_on_map(state_name)
            show_score()
    
    # Game over message
    remaining = 50 - len(guessed_states)
    screen.textinput(
        "Game Over!",
        f"You guessed {len(guessed_states)}/50 states.\n{remaining} states remaining."
    )
    screen.bye()


if __name__ == "__main__":
    game_loop()
