# Rock, Paper, Scissors
## Overview
This application employs the use of Python for both the game logic and the UI portion of Rock, Paper, Scissors. The solution is a repeatable, single round of the traditional rock, paper, scissors. The code is a bit sloppy and was slapped together in about an hour. It would be interesting to try to refactor it into a cleaner, possibly more object oriented solution. All in all, it works just fine. Here's the breakdown:

## The Game Logic
The game logic is simple - split it into three parts - a comparison function, a selection function, and a refreshing function.

### The Comparison Function
```
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
```
First, check if the values of `user` and `bot` are equal, implying the game is a draw. If not, check if the user is the winner by `elif`-ing the three scenarios in which the user wins. Lastly, assume that the user has lost if program hasn't returned by now. The function returns 0 for a draw, 1 for a user win, and -1 for a user loss.

### The Selection Function
```
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
```
Here we have the meat and potatoes of the game logic (in my mind). Essentially, this function is used to control the flow of the game. It is used as a callback in the form of a lambda callback from the UI. When the user selects their move by pressing a button, this is called with the move corresponding to the button that was selected (rock, paper, or scissors). As this is event driven the function first disables the buttons from being pressed again, then makes a choice for the bot (non-user player), then inserts the moves into the text widget, and finally it makes the comparison and displays the outcome for the win (or loss or draw... ba dum tisssssssss).

### The Refreshing Function
```
def play_again():
    btn_rock['state'] = 'normal'
    btn_paper['state'] = 'normal'
    btn_scissors['state'] = 'normal'
    gametext.delete(1.0, 4.0)
```
A simple function that resets the state of the UI by enabling the previously disabled buttons and by deleting the displayed text that was the outcome of the previous game.

## The User Interface
Barf...

### Tkinter is Nice
The solution is pretty simple. A few button widgets for selections, quitting the application, and refreshing the game. A text widget for the outcome of the game. And yeah... that's pretty much it. Some frame widgets were used for spacing and organization.

### The UI Code
```
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
```
