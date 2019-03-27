"""Scoring algorithm. Award man of the match."""


def score_algorithm(matches):
    """Function to calculate the score."""
    highest_score = 0
    highest_score_player = {}
    highest_w_score = 0
    highest_w_score_player = {}
    balls_played_score = 24
    balls_played_w_score = 24
    for m in matches:
        for team in m:
            for player in m[team]:
                if m[team][player]['player_type'] == 'batsman':
                    if m[team][player]['run_score'] > highest_score and m[team][player]['balls_played'] <= balls_played_score:
                        highest_score = m[team][player]['run_score']
                        highest_score_player = m[team]
                        balls_played_score = m[team][player]['balls_played']
                else:
                    if m[team][player]['wicket_score'] > highest_w_score and m[team][player]['balls_played'] <= balls_played_w_score:
                        highest_w_score = m[team][player]['wicket_score']
                        highest_w_score_player = m[team]
                        balls_played_w_score = m[team][player]['balls_played']
    return highest_w_score_player, highest_score_player


def update_team_player(team_name):
    """Function to update the team."""
    player = {}
    player_name = input("Enter {} player name : \t".format(team_name))
    player_type = input("Enter the player type (batsman / bowler) : \t ")
    balls_played = int(input("Enter the balls played : \t "))
    if player_type == 'batsman':
        scores = int(input("Enter the score in a match : \t"))
        player[player_name] = {}
        player[player_name]['player_type'] = player_type
        player[player_name]['run_score'] = scores
        player[player_name]['balls_played'] = balls_played
    else:
        wickets = int(input("Enter the wickets in a match : \t"))
        player[player_name] = {}
        player[player_name]['player_type'] = player_type
        player[player_name]['wicket_score'] = wickets
        player[player_name]['balls_played'] = balls_played
    return player

matches = []

number_matches = int(input("Enter the number of matches: \t"))

for i in range(number_matches):
    match = {}
    team1 = input("Enter the team name 1: \t")
    team2 = input("Enter the team name 2: \t")
    match[team1] = {}
    match[team2] = {}
    team_member_1 = int(input("Enter team strength for team 1: \t"))
    team_member_2 = int(input("Enter team strength for team 2: \t"))
    for tm in range(team_member_1):
        match[team1].update(update_team_player(team1))
    for tm in range(team_member_2):
        match[team2].update(update_team_player(team2))

    matches.append(match)

# pprint.pprint(matches)
man = score_algorithm(matches)
print('\n\n Man of the match goes to...\n')
for i in man:
    if i:
        print(i)
