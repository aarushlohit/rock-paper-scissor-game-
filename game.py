import tkinter as tk

def set_tile(row, column):
    global defaultplayer
    if game_over:
        return
    if board[row][column]["text"] != "":
        return
    board[row][column]["text"] = defaultplayer
    if defaultplayer == playerO:
        defaultplayer = playerX
    else:
        defaultplayer = playerO
    label["text"] = defaultplayer + "'s turn"  # Moved outside the if-else block
    check_winner()

def check_winner():
    global turns, game_over
    turns += 1  # Increment the turns count

    # Check horizontally for a winner
    for row in range(3):
        if (board[row][0]["text"] == board[row][1]["text"] == board[row][2]["text"]
                and board[row][0]["text"] != ""):
            label.config(text=board[row][0]["text"] + " is the winner!", foreground=color_blue)
            for column in range(3):
                board[row][column].config(foreground=color_yellow, background=color_blue)
            game_over = True
            return

    # Check vertically for a winner
    for column in range(3):
        if (board[0][column]["text"] == board[1][column]["text"] == board[2][column]["text"]
                and board[0][column]["text"] != ""):
            label.config(text=board[0][column]["text"] + " is the winner!", foreground=color_blue)
            for row in range(3):
                board[row][column].config(foreground=color_yellow, background=color_gray)
            game_over = True
            return

    # Check diagonally (top-left to bottom-right) for a winner
    if (board[0][0]["text"] == board[1][1]["text"] == board[2][2]["text"]
            and board[0][0]["text"] != ""):
        label.config(text=board[0][0]["text"] + " is the winner!", foreground=color_blue)
        for i in range(3):
            board[i][i].config(foreground=color_yellow, background=color_gray)
        game_over = True
        return

    # Check diagonally (top-right to bottom-left) for a winner
    if (board[0][2]["text"] == board[1][1]["text"] == board[2][0]["text"]
            and board[0][2]["text"] != ""):
        label.config(text=board[0][2]["text"] + " is the winner!", foreground=color_blue)
        board[0][2].config(foreground=color_yellow, background=color_gray)
        board[1][1].config(foreground=color_yellow, background=color_gray)
        board[2][0].config(foreground=color_yellow, background=color_gray)
        game_over = True
        return

    # Check for a draw
    if turns == 9:
        game_over = True
        label.config(text="Tie!", foreground=color_blue)

def new_game():
    global turns, game_over, defaultplayer
    turns = 0
    game_over = False
    defaultplayer = playerX
    label.config(text=defaultplayer + "'s turn", foreground="white")
    for row in range(3):
        for column in range(3):
            board[row][column].config(text="", foreground=color_gray, background=color_yellow)

# Game setup
color_blue = "#4584b6"
color_yellow = "#ffde57"
color_gray = "#343434"
light_gray = "#646464"
turns = 0
game_over = False
playerX = "X"
playerO = "O"
board = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]
defaultplayer = playerX

window = tk.Tk()
frame = tk.Frame(window)

window.title("TIC-TAC-TOE BY AARUSHLOHIT")
window.resizable(False, False)
label = tk.Label(frame, text=defaultplayer + "'s turn", font=("Comic Sans MS", 20, "bold"), background=color_yellow, foreground="black")
label.pack()
label.grid(row=0, column=0, columnspan=3, sticky="we")

for row in range(3):
    for column in range(3):
        board[row][column] = tk.Button(frame, text="", font=("Comic Sans MS", 50, "bold"), background=color_yellow, foreground=color_gray, width=4, height=1, command=lambda row=row, column=column: set_tile(row, column))
        board[row][column].grid(row=row+1, column=column)

reset_button = tk.Button(frame, text="RESTART", font=("Comic Sans MS", 20), background=color_yellow, foreground="white", command=new_game)
reset_button.grid(row=4, column=0, columnspan=3, sticky="we")
frame.pack()

window.mainloop()
