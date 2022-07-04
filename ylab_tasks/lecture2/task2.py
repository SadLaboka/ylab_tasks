#!/usr/bin/env python3
"""Reverse tic-tac-toe game. The one who puts 5 symbols in a row loses."""
import random
from tkinter import Tk, Label, Button, ttk

root = Tk()
root.title = "Reverse tic-tac-toe"
game_run = True

# List of field cells
field = []

# Number of user moves
cross_count = 0

# Difficulty level
difficulty = "Easy"

# Sets of moves made by the user and the computer
crosses = set()
zeroes = set()


def app():
    """Creates an interface and starts the game"""
    label = Label(root, text='0', width=35)
    label.grid(row=0, column=0, columnspan=4, sticky="nsew")

    # Creating cells on the field
    for row in range(10):
        line = []
        for col in range(10):
            button = Button(root, text=' ', width=4, height=2,
                            font=('Verdana', 20, 'bold'),
                            background='black',
                            command=lambda row=row, col=col: click(row, col))
            button.grid(row=row, column=col, sticky='nsew')
            line.append(button)
        field.append(line)

    # Creating "New game"-button
    new_button = Button(root, text='New game', command=new_game,
                        background="red", font=('Verdana', 14, 'bold'))
    new_button.grid(row=10, column=0, columnspan=10, sticky='nsew')

    # Creating a Difficulty Switcher
    difficulty_label = Label(root, text="Change difficulty:",
                             background='blue', font=('Verdana', 12, 'bold'))
    difficulty_label.grid(row=11, column=0, columnspan=6, sticky='nsew')
    font_for_list = ('Verdana', 12, 'bold')
    difficulty_list = ttk.Combobox(root, values=[
        "Easy",
        "Medium",
        "Hard"
    ], font=font_for_list, background='blue')
    difficulty_list.grid(row=11, column=6, columnspan=4, sticky='nsew')
    difficulty_list.bind("<<ComboboxSelected>>", change_difficulty)
    root.option_add('*TCombobox*Listbox.font', font_for_list)
    current_difficulty = Label(root, fg='white',
                               text=f"Current difficulty"
                                    f" level is {difficulty}",
                               background='black',
                               font=('Verdana', 14, 'bold'))
    current_difficulty.grid(row=12, column=0, columnspan=10, sticky='nsew')

    root.mainloop()


def new_game():
    """Starts new game"""
    crosses.clear()
    zeroes.clear()
    for row in range(10):
        for col in range(10):
            field[row][col]['text'] = ' '
            field[row][col]['background'] = 'black'

    global game_run
    game_run = True
    global cross_count
    cross_count = 0


def click(row, col):
    """Handles a player click"""
    if game_run and field[row][col]['text'] == ' ':
        field[row][col]['text'] = 'X'
        field[row][col]['fg'] = "red"
        crosses.add((row, col))
        global cross_count
        cross_count += 1
        change_lose_line(check_lose(crosses, 5))
        if game_run and cross_count < 50:
            computer_move()
        elif cross_count >= 50:
            draw_draw()


def computer_move(): # noqa
    """Creates a computer move"""
    attempts_count = 0
    lose_attempts = 0
    hard_checks_count = 0
    difficulty_map = {
        "Easy": {"checks": 2, "depth": 4, "hard": False},
        "Medium": {"checks": 10, "depth": 4, "hard": False},
        "Hard": {"checks": 20, "depth": 3, "hard": True}
    }
    checks_count = difficulty_map[difficulty]["checks"]
    inspection_depth = difficulty_map[difficulty]["depth"]
    hard_mode = difficulty_map[difficulty]["hard"]
    if len(zeroes) > 30:
        hard_mode = False

    while True:
        row = random.randint(0, 9)
        col = random.randint(0, 9)
        attempt = {(row, col)}

        if field[row][col]['text'] == ' ':

            # Checks neighboring cells
            if hard_mode and hard_checks_count < 10:
                neighboring_cells = check_lose(zeroes | crosses | attempt, 2)
                if neighboring_cells:
                    hard_checks_count += 1
                    continue

            # Checks the square.
            # The size of the square depends on the difficulty level
            lose_combination = check_lose(zeroes | attempt, inspection_depth)
            if lose_combination and attempts_count < checks_count:
                hard_checks_count = 0
                attempts_count += 1
                continue

            lose = check_lose(zeroes | attempt, 5)
            if lose and lose_attempts < checks_count:
                lose_attempts += 1
                continue

            change_lose_line(lose)
            field[row][col]['text'] = 'O'
            field[row][col]['fg'] = 'blue'
            zeroes.add((row, col))
            break


def check_lose(cells: set, count: int) -> set:
    """Checks for defeat conditions"""
    global game_run
    for cell in cells:

        tmp_cells = check_vertical(cell, cells, count)
        if len(tmp_cells) >= 4:
            tmp_cells.add(cell)
            return tmp_cells

        tmp_cells = check_horizontal(cell, cells, count)
        if len(tmp_cells) >= 4:
            tmp_cells.add(cell)
            return tmp_cells

        tmp_cells = check_first_diagonal(cell, cells, count)
        if len(tmp_cells) >= 4:
            tmp_cells.add(cell)
            return tmp_cells

        tmp_cells = check_second_diagonal(cell, cells, count)
        if len(tmp_cells) >= 4:
            tmp_cells.add(cell)
            return tmp_cells

    return set()


def check_vertical(cell: tuple, cells: set, count: int) -> set:
    """Checks the cell vertical"""
    tmp_cells = set()
    for i in range(1, count):
        bot_cell = (cell[0] + i, cell[1])
        if bot_cell in cells:
            tmp_cells.add(bot_cell)
        else:
            break

    for i in range(1, count):
        top_cell = (cell[0] - i, cell[1])
        if top_cell in cells:
            tmp_cells.add(top_cell)
        else:
            break

    return tmp_cells


def check_horizontal(cell: tuple, cells: set, count: int) -> set:
    """Checks the cell horizontal"""
    tmp_cells = set()
    for i in range(1, count):
        right_cell = (cell[0], cell[1] + i)
        if right_cell in cells:
            tmp_cells.add(right_cell)
        else:
            break

    for i in range(1, count):
        left_cell = (cell[0], cell[1] + i)
        if left_cell in cells:
            tmp_cells.add(left_cell)
        else:
            break

    return tmp_cells


def check_first_diagonal(cell: tuple, cells: set, count: int) -> set:
    """Checks diagonal top-left to bot-right"""
    tmp_cells = set()
    for i in range(1, count):
        bot_right_cell = (cell[0] + i, cell[1] + i)
        if bot_right_cell in cells:
            tmp_cells.add(bot_right_cell)
        else:
            break

    for i in range(1, count):
        top_left_cell = (cell[0] - i, cell[1] - i)
        if top_left_cell in cells:
            tmp_cells.add(top_left_cell)
        else:
            break

    return tmp_cells


def check_second_diagonal(cell: tuple, cells: set, count: int) -> set:
    """Checks diagonal bot-left to top-right"""
    tmp_cells = set()
    for i in range(1, count):
        bot_left_cell = (cell[0] + i, cell[1] - i)
        if bot_left_cell in cells:
            tmp_cells.add(bot_left_cell)
        else:
            break

    for i in range(1, count):
        top_right_cell = (cell[0] - i, cell[1] + i)
        if top_right_cell in cells:
            tmp_cells.add(top_right_cell)
        else:
            break

    return tmp_cells


def change_lose_line(cells: set) -> None:
    """Changes the background of the losing line to white"""
    global game_run
    if cells:
        game_run = False
    for cell in cells:
        field[cell[0]][cell[1]]['background'] = 'white'


def draw_draw():
    """Draws the field in case of a tie"""
    for row in range(10):
        for col in range(10):
            field[row][col]['background'] = 'yellow'


def change_difficulty(event):
    """Changes the difficulty level"""
    global difficulty
    difficulty = root.__dict__["children"]['!combobox'].get()
    current_difficulty = Label(root, fg='white',
                               text=f"Current difficulty"
                                    f" level is {difficulty}",
                               background='black',
                               font=('Verdana', 14, 'bold'))
    current_difficulty.grid(row=12, column=0, columnspan=10, sticky='nsew')

    new_game()


if __name__ == "__main__":
    app()
