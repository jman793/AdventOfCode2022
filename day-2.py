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

desired_outcome = {
    'X': 'LOSE',
    'Y': 'DRAW',
    'Z': 'WIN'
}

hand_to_win = {
    'ROCK': 'PAPER',
    'PAPER': 'SCISSORS',
    'SCISSORS': 'ROCK'
}

hand_to_lose = {
    'ROCK': 'SCISSORS',
    'PAPER': 'ROCK',
    'SCISSORS': 'PAPER'
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
            [opp_move_code, your_instruction] = line.split()
            opp_move = hand_letter_opp[opp_move_code]
            your_move = hand_to_throw(opp_move, your_instruction)
            yield score_hand[your_move] + outcome_score[desired_outcome[your_instruction]]
            line = fp.readline()
                
def hand_to_throw(opp_move, your_instruction):
    match your_instruction:
        case 'Y':
            return opp_move
        case 'X':
            return hand_to_lose[opp_move]
        case 'Z':
            return hand_to_win[opp_move]
    
print(sum(read_in_game())) 