import tkinter as tk
from solve import solve

window = tk.Tk()
window.title("Sudoku Solver")

frame = tk.Frame(master=window, width=500, height=600)
frame.pack()

canvas= tk.Canvas(window, width=500, height=600)
canvas.place(x=0,y=0)

canvas.create_line(170,32,170,456, fill="black", width=5)
canvas.create_line(320,32,320,456, fill="black", width=5)
canvas.create_line(32,170,456,170, fill="black", width=5)
canvas.create_line(32,320,456,320, fill="black", width=5)

msg = tk.Label(fg="white", text="Enter Your Current GameBoard")
msg.place(x=150, y=5)

tiles = [[None for _ in range(9)] for _ in range(9)]
for i in range(9):
    for j in range(9):
        tiles[i][j] = tk.Entry(width=2)
        tiles[i][j].place(x=50*i+30, y=50*j+30)

def update():
    board = [[None for _ in range(9)] for _ in range(9)]
    for i in range(9):
        for j in range(9):
            board[j][i] = tiles[i][j].get()
    soln = solve(board)
    for i in range(9):
        for j in range(9):
            tiles[i][j].delete(0, tk.END)
            tiles[i][j].insert(0,str(int(soln[j][i])))

button = tk.Button(
    text="Solve",
    width=25,
    height=5,
    command=update
)
button.place(x=115, y=470)



window.mainloop()
