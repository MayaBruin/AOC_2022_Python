score_rock = 1
score_paper = 2
score_scissors = 3

score_win = 6
score_draw = 3
score_loss = 0

total_score = 0

def what_to_play(opponent, outcome):
    if outcome == "Z":
        if opponent == "A":
            return score_paper
        if opponent == "B":
            return score_scissors
        if opponent == "C":
            return score_rock
    
    if outcome == "X":
        if opponent == "A":
            return score_scissors
        if opponent == "B":
            return score_rock
        if opponent == "C":
            return score_paper

    if outcome == "Y":
        if opponent == "A":
            return score_rock
        if opponent == "B":
            return score_paper
        if opponent == "C":
            return score_scissors


input = open("input", "r")

for line in input:
    theirplay = line[0]
    desired_outcome = line[2]

    if desired_outcome == "Z":
        total_score += score_win
    if desired_outcome == "Y":
        total_score += score_draw
    if desired_outcome == "X":
        total_score += score_loss

    total_score += what_to_play(theirplay, desired_outcome)

print("total score: " + str(total_score))
