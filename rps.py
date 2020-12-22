#!/usr/bin/python3

import tkinter as tk
import random

# Game Logic and Callbacks
def compare(user, bot):
    if user is bot:
        return 0
    elif (user is 'rock' and bot is 'scissors'):
        return 1
    elif (user is 'paper' and bot is 'rock'):
        return 1
    elif (user is 'scissors' and bot is 'paper'):
        return 1
    else:
        return -1

def user_select(text):
    user_choice = text
    btn_rock['state'] = 'disable'
    btn_paper['state'] = 'disable'
    btn_scissors['state'] = 'disable'

    bot_choice = random.choice(['rock', 'paper', 'scissors'])

    gametext.insert(tk.INSERT, 'Your choice:' + user_choice + '\n')
    gametext.insert(tk.INSERT, 'Bot choice:' + bot_choice + '\n')

    result = compare(user_choice, bot_choice)

    if (result == 0):
        gametext.insert(tk.INSERT, 'DRAW')
    elif (result == -1):
        gametext.insert(tk.INSERT, 'YOU LOSE')
    else:
        gametext.insert(tk.INSERT, 'WINNER WINNER')

def play_again():
    btn_rock['state'] = 'normal'
    btn_paper['state'] = 'normal'
    btn_scissors['state'] = 'normal'
    gametext.delete(1.0, 4.0)

# USER INTERFACE
root = tk.Tk()
topframe = tk.Frame(root)
topframe.pack()

btn_rock = tk.Button(topframe,
                     bg='green',
                     fg='white',
                     text='Rock',
                     width=25,
                     command=lambda:user_select('rock'))
btn_rock.pack(side=tk.LEFT)
btn_paper = tk.Button(topframe,
                      bg='black',
                      fg='white',
                      text='Paper',
                      width=25,
                      command=lambda:user_select('paper'))
btn_paper.pack(side=tk.LEFT)
btn_scissors = tk.Button(topframe,
                         bg='blue',
                         fg='white',
                         text='Scissors',
                         width=25,
                         command=lambda:user_select('scissors'))
btn_scissors.pack(side=tk.LEFT)

padtop = tk.Frame(root, height=50)
padtop.pack()
gametext = tk.Text(root)
gametext.pack()
padbottom = tk.Frame(root, height=50)
padbottom.pack()
bottom = tk.Frame(root)
bottom.pack()

btn_quit = tk.Button(bottom, bg='red', fg='white', text='QUIT', width=20, command=root.quit)
btn_quit.pack()
btn_again = tk.Button(bottom, bg='white', text='Play Again',width=20, command=play_again)
btn_again.pack()

tk.mainloop()
