score_rock = 1
score_paper = 2
score_scissors = 3

score_win = 6
score_draw = 3
score_loss = 0

total_score = 0

def playround(player, opponent):
    # Draws
    if player == "X" and opponent == "A":
        return "draw"
    if player == "Y" and opponent == "B":
        return "draw"
    if player == "Z" and opponent == "C":
        return "draw"
    
    # Losses
    if player == "X" and opponent == "B":
        return "loss"
    if player == "Y" and opponent == "C":
        return "loss"
    if player == "Z" and opponent == "A":
        return "loss"

    # Wins 
    if player == "X" and opponent == "C":
        return "win"
    if player == "Y" and opponent == "A":
        return "win"
    if player == "Z" and opponent == "B":
        return "win"


input = open("input", "r")

for line in input:
    theirplay = line[0]
    myplay = line[2]

    if myplay == "X":
        total_score += score_rock

    if myplay == "Y":
        total_score += score_paper

    if myplay == "Z":
        total_score += score_scissors
        
    result = playround(myplay, theirplay)

    if result == "win":
        total_score += score_win
    if result == "draw":
        total_score += score_draw
    if result == "loss":
        total_score += score_loss

print("total score: " + str(total_score))
