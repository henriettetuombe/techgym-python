import random

hands = ['rock', 'scissors', 'paper']


def start_message():
    print('Start \'rock-paper-scissors\'')


def get_player():
    print('Input your hand')
    return int(input('0:rock, 1:scissors, 2:paper'))


def get_computer():
    return random.randint(0, 2)


def get_hand_name(hand_number):
    return hands[hand_number]


def view_hand(your_hand, computer_hand):
    print('My hand is ' + get_hand_name(your_hand))
    print('Rival\'s hand is ' + get_hand_name(computer_hand))


def view_result(hand_diff):
    if hand_diff == 0:
        print('draw')
    elif hand_diff == -1 or hand_diff == 2:
        print('win')
    else:
        print('lose')


def play_game():
    # Start the game
    start_message()
    # Get the player's choice and the computer's choice
    your_hand = get_player()
    computer_hand = get_computer()
    # Calculate the difference between the player's hand and the computer's hand
    hand_diff = your_hand - computer_hand
    # Show both hands to the player
    view_hand(your_hand, computer_hand)
    # Determine and display the result of the game
    view_result(hand_diff)


# Play the game
play_game()
