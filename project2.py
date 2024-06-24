from tkinter import *
import random

def next_turn(row, column):

    global player
    if board[row][column]['text'] == "" and winner() is False:

        if player == players[0]:
            board[row][column]['text'] = player

            if winner() is False:
             player = players[1]
             label.config(text=(players[1]+' turn'))

            elif winner() is True:
             label.config(text=(players[0]+' wins'))
 
            elif winner() == 'Tie':
             label.config(text=('Tie!'))

        else:
            board[row][column]['text'] = player

            if winner() is False:
             player = players[0]
             label.config(text=(players[0]+' turn'))

            elif winner() is True:
             label.config(text=(players[1]+' wins'))
 
            elif winner() == 'Tie':
             label.config(text=('Tie!'))


def winner():
    
    for row in range(3):
        if board[row][0]['text'] == board[row][1]['text'] == board[row][2]['text'] != "":
            board[row][0].config(bg='green')
            board[row][1].config(bg='green')
            board[row][2].config(bg='green')
            return True

    for column in range(3):
        if board[0][column]['text'] == board[1][column]['text'] == board[2][column]['text'] != "":
            board[0][column].config(bg='green')
            board[1][column].config(bg='green')
            board[2][column].config(bg='green')
            return True

    if board[0][0]['text'] == board[1][1]['text'] == board[2][2]['text'] != "":
        return 
        
    elif board[0][2]['text'] == board[1][1]['text'] == board[2][0]['text'] != "":
        board[0][2].config(bg='green')
        board[1][1].config(bg='green')
        board[2][0].config(bg='green')
        return True

    elif blank_spaces() is False:
        
        for row in range(3):
            for column in range(3):
                   board[row][column].config(bg="yellow")

        return "Tie"

    else:
        return False

def blank_spaces():
    spaces = 9

    for row in range(3):
        for column in range(3):
            if board[row][column]['text'] != "":
                spaces -= 1

    if spaces == 0:
        return False

    else:
        return True

def new_game():
    global player

    player = random.choice(players)

    label.config(text=player+" turn")

    for row in range(3):
        for column in range(3):
            board[row][column].config(text="",bg="#F0F0F0")


window = Tk()
window.title('Tic-tac-toe')

players = ["X","O"]
player = random.choice(players)
board = [[0,0,0],
         [0,0,0],
         [0,0,0]]

label = Label(text = player+"'s turn", font = ('arial',40))
label.pack(side='top')

restart_button = Button(text = "restart", font = ('arial',25), command = new_game)
restart_button.pack(side='top')

frame = Frame(window)
frame.pack()

for row in range(3):
    for column in range(3):
        board[row][column] = Button(frame, text="",font = ('arial',40), height= '1', width = '3',
        command= lambda row=row, column= column: next_turn(row,column) )
        board[row][column].grid(row=row,column=column)

window.mainloop()