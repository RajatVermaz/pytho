import random

def play():
    user = input("What is your choice ? 'r' for rock, 'p' for paper, 's' for scissors ")
    computer = random.choice(['r','p','s'])

    if user == computer:
        return 'it\'s a tie'
    
    if is_win(user, computer):
        return 'You won!'
    return 'You lost!'
    
def is_win(player,opponent):
    # r > s, s > p and p > r
    # returns true if player wins
    if((player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r') ):
        return True

print(play())