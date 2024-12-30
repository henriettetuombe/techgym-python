import random

# Function to display the start message
def start_message():
    print("\nWelcome to the Rock-Paper-Scissors Game!")
    print("Instructions: Enter your choice as 0 (rock), 1 (scissors), or 2 (paper).")

# Function to get player's choice with input validation
def get_player():
    while True:
        try:
            player = int(input("\nYour choice (0 = rock, 1 = scissors, 2 = paper): "))
            if player in [0, 1, 2]:
                return player
            else:
                print("Invalid choice. Please enter 0, 1, or 2.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Function to get computer's choice
def get_computer():
    return random.randint(0, 2)

# Function to display hand names
def display_hands(player, computer):
    hands = ["rock", "scissors", "paper"]
    print(f"\nYou chose: {hands[player]}")
    print(f"Computer chose: {hands[computer]}")

# Function to determine and return the result
def determine_result(player, computer):
    if player == computer:
        print("It's a draw!")
        return "draw"
    elif (player == 0 and computer == 1) or (player == 1 and computer == 2) or (player == 2 and computer == 0):
        print("You win this round!")
        return "win"
    else:
        print("You lose this round!")
        return "lose"

# Main game function
def play_game():
    start_message()
    player = get_player()
    computer = get_computer()
    display_hands(player, computer)
    return determine_result(player, computer)

# Replay function with input validation
def ask_replay():
    while True:
        replay = input("\nDo you want to play again? (yes/no): ").lower()
        if replay in ["yes", "no"]:
            return replay == "yes"
        print("Invalid input. Please enter 'yes' or 'no'.")

# Main program loop with scorekeeping
def main():
    print("\n=== Rock-Paper-Scissors Game ===")
    player_score = 0
    computer_score = 0
    draws = 0

    while True:
        result = play_game()
        if result == "win":
            player_score += 1
        elif result == "lose":
            computer_score += 1
        else:
            draws += 1

        print("\nCurrent Scores:")
        print(f"Player: {player_score} | Computer: {computer_score} | Draws: {draws}")

        if not ask_replay():
            print("\nThanks for playing!")
            print(f"Final Scores: Player: {player_score} | Computer: {computer_score} | Draws: {draws}")
            print("Goodbye! Have a great day!")
            break

# Run the game
main()
