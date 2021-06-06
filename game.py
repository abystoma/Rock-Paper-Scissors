from random import choice

moves = ['rock', 'paper', 'scissors']
commands = ['!exit', '!rating']
score_bank = {}
score = 0


def play(player: str, options: str, user_move: str, ai_move: str) -> str:
    global score
    if user_move == ai_move:
        s = score_bank.setdefault(player, score)
        score_bank[player] = s + 50
        write_score(player)
        return f"There is a draw ({user_move})"
    else:
        user_index = options.index(user_move)
        rev_list = options[user_index + 1:] + options[:user_index]
        index_sep = int(len(rev_list) / 2)
        winning_list = rev_list[:index_sep]
        loosing_list = rev_list[index_sep:]

        if ai_move in loosing_list:
            s = score_bank.setdefault(player, score)
            score_bank[player] = s + 100
            write_score(player)
            return f"Well done. The computer chose {ai_move} and failed"
        else:
            return f"Sorry, but the computer chose {ai_move}"

        #using circular array
        # offset = (options.index(ai_move) - options.index(user_move)) % len(options)
        # if offset > len(options) // 2:
        #     score += 100
        #     print(f'Well done. Computer chose {ai_move} and failed')
        # else:
        #     print(f'Sorry, but computer chose {ai_move}')

def read_score() -> None:
    with open('rating.txt', 'r') as f:
        for line in f:
            name, score = line.split()
            score_bank[name] = int(score)


def write_score(player: str) -> None:
    idx = None
    with open('rating.txt', 'r') as file:
    # read a list of lines into data
        data = file.readlines()
        for line in data:
            if line.split()[0] == player:
                idx = data.index(line)
                points = int(line.split()[1])

    if idx is not None:
        data[idx] = f'{player} {score_bank.setdefault(player, score)}\n'
        with open('rating.txt', 'w') as file:
            file.writelines(data)
    else:
        with open('rating.txt', 'a') as file:
            file.write(f"{player} {score_bank.setdefault(player, score)}")



def play_game(player: str, options: list) -> None:
    while True:
        user_move = input()

        if user_move == "!exit":
            print("Bye!")
            break
        elif user_move == "!rating":
            s = score_bank.setdefault(player, score)
            print('Your rating:', s)
        elif user_move not in options:
            print('Invalid input')
        else:
            ai_move = choice(moves)
            print(play(player, options, user_move, ai_move))


def main() -> None:
    bank = open('rating.txt', 'r')
    read_score()
    current_player = input('Enter your name: ')
    print(f'Hello, {current_player}')
    options = input()
    if options == '':
        options = moves
    else:
        options = options.split(",")
    print("Okay, let's start")
    if current_player not in bank:
        score_bank.setdefault(current_player, score)
    score_bank.update(bank)
    play_game(current_player, options)


main()
