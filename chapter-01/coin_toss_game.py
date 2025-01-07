import random

# Check if the input is correct (0 or 1)
def is_correct_input(choice):
    return choice in [0, 1]

# Randomly generate coin toss result
def get_coin_side():
    return random.randint(0, 1)

# Convert 0 to "head" and 1 to "tail"
def get_side_name(side):
    return "head" if side == 0 else "tail"

# Display both the player's bet and the coin's outcome
def view_side(player_side, coin_side):
    print(f"My bet is {get_side_name(player_side)}")
    print(f"Coin is {get_side_name(coin_side)}")

# Determine if the player won or lost
def get_result(player_side, coin_side):
    return "win" if player_side == coin_side else "lose"

# Display the final result of the game
def view_result(result):
    print(result)

# Main game function
def play():
    print("Start 'coin toss'")
    
    # Get player's bet with validation
    while True:
        try:
            print("Input your bet")
            player_input = int(input("0:head, 1:tail "))
            if is_correct_input(player_input):
                break
            else:
                print("Invalid input. Please enter 0 for head or 1 for tail.")
        except ValueError:
            print("Invalid input. Please enter a valid number (0 or 1).")
    
    # Get coin toss result
    player_side = player_input
    coin_side = get_coin_side()
    
    # Display the sides
    view_side(player_side, coin_side)
    
    # Determine and display the result
    result = get_result(player_side, coin_side)
    view_result(result)

# Execute the game
play()
