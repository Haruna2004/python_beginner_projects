#lets play rock paper scissors
import random
def play():
    user = input("What's your choice? 'r' for rock, 'p' for paper , 's' for scissors \n").lower()
    computer = random.choice(['r','p','s'])

    if user == computer:
        return "Its a ties!"
    if is_win(user,computer):
        return ('You won!')
    return 'You lost'

    

def is_win(player,computer):
    #return true if player wins
    if (player == 'r' and computer == 's') or (player == 'p' and computer == 'r') or \
        (player == 's' and computer == 'p'):
        return True
print(play())