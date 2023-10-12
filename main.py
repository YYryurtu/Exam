import logging
import random

logging.basicConfig(level=logging.DEBUG, filename="logs.log", filemode="w", format="%(asctime)s:%(levelname)s - %(message)s")

desk = [[" " for _ in range(3)] for _ in range(3)]


def display_field():
    logging.debug("Displaying the playing field on the screen")
    for line in desk:
        print(" | ".join(line))
        print("-" * 10)


def winner(sign):
    for i in range(3):
        if desk[i][0] == desk[i][1] == desk[i][2] == sign:
            logging.debug("Win on the line")
            return True
        if desk[0][i] == desk[1][i] == desk[2][i] == sign:
            logging.debug("Win on the column")
            return True
    if desk[0][0] == desk[1][1] == desk[2][2] == sign:
        logging.debug("Gain diagonally")
        return True
    if desk[0][2] == desk[1][1] == desk[2][0] == sign:
        logging.debug("Gain diagonally")
        return True
    return False


def computer_move():
    logging.debug("Computer's move")
    while True:
        line = random.randint(0, 2)
        column = random.randint(0, 2)
        if desk[line][column] == " ":
            desk[line][column] = "O"
            return


def two_player_move(player):
    logging.debug(f"Player {player}'s move")
    while True:
        line = input(f"Гравець {player}, введіть номер рядка (0, 1 або 2): ")
        column = input(f"Гравець {player}, введіть номер стовпця (0, 1 або 2): ")

        if line.isdigit() and column.isdigit():
            logging.debug("Checking the admissibility of the move")
            line = int(line)
            column = int(column)
            if 0 <= line <= 2 and 0 <= column <= 2:
                logging.debug("Checking the admissibility of the move")
                if desk[line][column] == " ":
                    desk[line][column] = player
                    return
                else:
                    logging.debug("The cell is busy")
                    print("Це місце вже зайняте. Спробуйте ще раз.")
            else:
                logging.debug("Invalid value entered")
                print("Введені значення мають бути 0, 1 або 2. Спробуйте ще раз.")
        else:
            logging.debug("Invalid number entered")
            print("Введіть коректні числові значення (0, 1 або 2). Спробуйте ще раз.")


mode = input("Виберіть режим гри (1 - проти комп'ютера, 2 - гра вдвох): ")

player = "X"
while True:
    display_field()
    if mode == "1":
        if player == "X":
            two_player_move(player)
        else:
            computer_move()
    elif mode == "2":
        two_player_move(player)
    else:
        logging.debug("Invalid game mode selected")
        print("Невірно вибраний режим гри. Виберіть 1 або 2.")
        break

    if winner(player):
        display_field()
        logging.debug(f"Player {player} win")
        print(f"Гравець {player} переміг!")
        break
    if all(all(cell != " " for cell in line) for line in desk):
        display_field()
        logging.debug("The game ended in a draw!")
        print("Гра закінчилася в нічию!")
        break

    player = "O" if player == "X" else "X"
