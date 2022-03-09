from tkinter import *
import tkinter.messagebox

#2. Put on the window we need
def game_spots():
    h=[]
    for i in range(3):
        for j in range(3):
            if board[i][j]['text'] == '':
                h.append((i,j))
    return h

#3. Check for win
def check_for_win():
    for i in range(3):
        if board[i][0]['text'] == board[i][1]['text'] == board[i][2]['text'] !='':
            return 1
    for j in range(3):
        if board[0][j]['text'] == board[1][j]['text'] == board[2][j]['text'] !='':
            return 1
    if board[0][0]['text'] == board[1][1]['text'] == board[2][2]['text'] !='':
            return 1
    elif board[0][2]['text'] == board[1][1]['text'] == board[2][0]['text'] !='':
            return 1
    elif game_spots() == []:
        return 0
    else:
        return -1

#4.Game flow function
player = 'X'
def game_flow(r,c):
    global player
    if board[r][c]['text'] == '' and check_for_win() == -1:
        if player == 'X':
            board[r][c].config(text=('X'))
            if check_for_win() == -1:
                player = 'O'
                label.config(text=("It's O's turn"))
            elif check_for_win() == 1:
                tkinter.messagebox.showinfo("Winner", "X Win")
            elif check_for_win() == 0:
                tkinter.messagebox.showinfo("Tic Tac Toe", "Draw!")
        elif player == 'O':
            board[r][c].config(text=('O'))
            if check_for_win() == -1:
                player = 'X'
                label.config(text=("It's X's turn"))
            elif check_for_win() == 1:
                tkinter.messagebox.showinfo("Winner", "O Win")
            elif check_for_win() == 0:
                tkinter.messagebox.showinfo("Tic Tac Toe", "Draw!")

#1.Create the game window
root = Tk()
root.title("Tic Tac Toe")
root['bg'] = 'blue'
root.iconbitmap("K:\Python\icon_game.ico")
board = [[0,0,0], [0,0,0], [0,0,0]]
for i in range(3):
    for j in range(3):
        board[i][j]=Button(root, text='', font=('normal', 50, 'normal'), width=6, height=3, command=lambda r=i, c=j: game_flow(r,c))
        board[i][j].grid(row=i, column=j)
label = Label(root, text="It's X's turn", font=('normal', 20,'bold'), fg='white', bg='black')
label.grid(row=3, column=0, columnspan=3)

#5. Restart 
def restart():
    for i in range(3):
        for j in range(3):
            board[i][j]['text'] = ''
button = Button(root, text="Restart", font=('Courier', 18, 'normal'), fg="blue", command = restart)
button.grid(row = 4, column = 0, columnspan = 3)
root.mainloop()