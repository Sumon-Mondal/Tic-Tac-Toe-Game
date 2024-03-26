import tkinter as tk

def check_winner():
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        # Check rows
        if board[i][0] == board[i][1] == board[i][2] != "":
            draw_winning_line(i, 0, i, 2)  # Draw horizontal line
            return board[i][0]

        # Check columns
        if board[0][i] == board[1][i] == board[2][i] != "":
            draw_winning_line(0, i, 2, i)  # Draw vertical line
            return board[0][i]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != "":
        draw_winning_line(0, 0, 2, 2)  # Draw diagonal line
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] != "":
        draw_winning_line(0, 2, 2, 0)  # Draw diagonal line
        return board[0][2]

    return None

def draw_winning_line(x1, y1, x2, y2):
    x1_pos, y1_pos = x1 * cell_size + cell_size / 2, y1 * cell_size + cell_size / 2
    x2_pos, y2_pos = x2 * cell_size + cell_size / 2, y2 * cell_size + cell_size / 2
    canvas.create_line(x1_pos, y1_pos, x2_pos, y2_pos, fill="red", width=4)

def click(event):
    global current_player

    x, y = int(event.x // cell_size), int(event.y // cell_size)

    if board[x][y] == "":
        board[x][y] = current_player
        draw_symbol(x, y, current_player)
        winner = check_winner()
        if winner:
            label.config(text=f"Player {winner} wins! 🎉")
            canvas.unbind("<Button-1>")
        else:
            current_player = "O" if current_player == "X" else "X"
            label.config(text=f"Player {current_player}'s turn")

def draw_symbol(x, y, symbol):
    x_pos, y_pos = x * cell_size + cell_size / 2, y * cell_size + cell_size / 2
    canvas.create_text(x_pos, y_pos, text=symbol, font=("Arial", 36))

root = tk.Tk()
root.title("Tic-Tac-Toe")

canvas_width, canvas_height = 300, 300
cell_size = canvas_width / 3
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height)
canvas.pack()

# Draw horizontal lines
for i in range(1, 3):
    canvas.create_line(0, i * cell_size, canvas_width, i * cell_size, fill="black", width=2)

# Draw vertical lines
for i in range(1, 3):
    canvas.create_line(i * cell_size, 0, i * cell_size, canvas_height, fill="black", width=2)

board = [["" for _ in range(3)] for _ in range(3)]
current_player = "X"
label = tk.Label(root, text=f"Player {current_player}'s turn")
label.pack()

canvas.bind("<Button-1>", click)

root.mainloop()
