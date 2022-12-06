score_hand = {
    'ROCK': 1,
    'PAPER': 2,
    'SCISSORS': 3
}

outcome_score = {
    'WIN': 6,
    'DRAW': 3,
    'LOSE': 0
}

hand_letter_opp = {
    'A': 'ROCK',
    'B': 'PAPER',
    'C': 'SCISSORS'
}

hand_letter_you = {
    'X': 'ROCK',
    'Y': 'PAPER',
    'Z': 'SCISSORS'
}

# reads in one game of RPS
# returns the score
def read_in_game():
    filepath = './inputs/day-2.txt'
    with open(filepath) as fp:
        line = fp.readline()
        ctr = 0
        while line:
            ctr +=1
            [opp_move_code, your_move_code] = line.split()
            opp_move = hand_letter_opp[opp_move_code]
            your_move = hand_letter_you[your_move_code]
            did_win = did_you_win(opp_move, your_move)
            yield score_hand[your_move] + outcome_score[did_win]
            line = fp.readline()
            
            
# returns string based on the outcome        
def did_you_win(opp_move, your_move):
    if opp_move == your_move:
        return 'DRAW'
    elif your_move == 'ROCK' and opp_move == 'SCISSORS':
        return 'WIN'
    elif your_move == 'SCISSORS' and opp_move == 'PAPER':
        return 'WIN'
    elif your_move == 'PAPER' and opp_move == 'ROCK':
        return 'WIN'
    else:
        return 'LOSE'
    
print(sum(read_in_game())) 