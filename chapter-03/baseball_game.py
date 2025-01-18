import random
import math

# List to store all teams
teams = []

# Dictionary to store the selected teams
playing_teams = {'myself': False, 'enemy': False}


class Team:
    def __init__(self, name, attack, defense):
        # Initialize team attributes
        self.name = name
        self.attack = attack
        self.defense = defense
        self.total_score = 0  # Total score across all innings

    def info(self):
        # Print team information
        print(self.name + ': Offensive power:' + str(self.attack) +
              ' / Defensive power:' + str(self.defense))

    def get_hit_rate(self):
        # Generate a random hit rate based on the team's attack power
        return random.randint(10, self.attack)

    def get_out_rate(self):
        # Generate a random out rate based on the team's defense power
        return random.randint(10, self.defense)


def create_teams():
    # Create predefined teams and add them to the global list
    global teams
    team1 = Team('Atackers', 80, 20)
    team2 = Team('Defenders', 30, 70)
    team3 = Team('Averages', 50, 50)
    teams = [team1, team2, team3]


def show_teams():
    # Display all team information
    index = 1
    print('Information of all teams')
    for team in teams:
        print(str(index))  # Print team index
        team.info()
        index += 1


def choice_team(player):
    # Allow the player to choose a team
    if player == 'myself':
        player_name = 'Your'
    elif player == 'enemy':
        player_name = 'Opponent\'s'

    choice_team_number = int(input('Select ' + player_name + ' team(1-3) '))
    playing_teams[player] = teams[choice_team_number - 1]
    print(player_name + ' team is \'' + playing_teams[player].name + '\'')


def get_play_inning(inning):
    # Calculate the score for a single inning
    if inning == 'top':
        hit_rate = playing_teams['myself'].get_hit_rate()
        out_rate = playing_teams['enemy'].get_out_rate()
    elif inning == 'bottom':
        hit_rate = playing_teams['enemy'].get_hit_rate()
        out_rate = playing_teams['myself'].get_out_rate()
    inning_score = math.floor((hit_rate - out_rate) / 10)
    return max(inning_score, 0)  # Ensure score is not negative


def play():
    create_teams()  # Initialize teams
    show_teams()  # Display teams
    choice_team('myself')  # Player chooses their team
    choice_team('enemy')  # Player chooses opponent's team

    # Initialize scoreboard
    score_boards = ['________|', 'You     |', 'Opponent|']
    for i in range(9):  # Loop through 9 innings
        score_boards[0] += str(i + 1) + '｜'  # Add inning number
        # Top inning (player attacks)
        inning_score = get_play_inning('top')
        score_boards[1] += str(inning_score) + '｜'
        playing_teams['myself'].total_score += inning_score
        # Bottom inning (opponent attacks)
        if i == 8 and playing_teams['myself'].total_score < playing_teams['enemy'].total_score:
            score_boards[2] += 'X｜'  # Skip if opponent already won
        else:
            inning_score = get_play_inning('bottom')
            score_boards[2] += str(inning_score) + '｜'
            playing_teams['enemy'].total_score += inning_score

    # Add total scores to the scoreboard
    score_boards[0] += 'R｜'
    score_boards[1] += str(playing_teams['myself'].total_score) + '｜'
    score_boards[2] += str(playing_teams['enemy'].total_score) + '｜'

    # Print the final scoreboard
    print(score_boards[0])
    print(score_boards[1])
    print(score_boards[2])


play()