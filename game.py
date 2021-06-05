from random import choice

moves = ['rock','paper','scissors']
commands = ['!exit','!rating']
score_bank = {}
score = 0

def play(player: str,user_move: str, ai_move: str) -> str:
    global score
    if user_move == ai_move:
        s = score_bank.setdefault(player, score)
        score_bank[player] = s + 50
        return f"There is a draw ({user_move})"
    else:
        user_index = moves.index(user_move)
        ai_index = moves.index(ai_move)

        winning_condition = (ai_index + 1) % 3

        if winning_condition == user_index:
            s = score_bank.setdefault(player, score)
            score_bank[player] = s + 100
            return f"Well done. The computer chose {ai_move} and failed"
        else:
            return f"Sorry, but the computer chose {ai_move}"

def read_score() -> None:
    with open('rating.txt', 'r') as f:
        for line in f:
            name, score = line.split()
            score_bank[name] = int(score)

def play_game(player: str) -> None:
    while True:
        user_move = input()

        if user_move not in moves and user_move not in commands:
            print("Invalid input")
        elif user_move == "!exit":
             print("Bye!")
             break
        elif user_move == "!rating":
            s = score_bank.setdefault(player, score)
            print('Your rating:', s)
        else:
            ai_move = choice(moves)
            print(play(player, user_move, ai_move))

def main() -> None:
    bank = open('rating.txt', 'r')
    read_score()
    current_player = input('Enter your name: ')
    print(f'Hello, {current_player}')
    if current_player not in bank:
        score_bank.setdefault(current_player, score)
    score_bank.update(bank)
    play_game(current_player)

main()