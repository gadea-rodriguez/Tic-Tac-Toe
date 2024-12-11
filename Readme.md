# Tic-Tac-Toe
This is a simple game of Tic-Tac-Toe programed in python with the extension of Pygame
## Contents
- [Introduction](#introduction)
- [Pre-requisites](#pre-requisites)
- [Installation](#isntallation)
- [Usage](#usage)
- [Code explanation](#explanation)
    - [Functions](#functions)
        - [draw_playboard](#draw_playboard)
        - [draw_player](#draw_player)
        - [move](#move)
        - [winner](#winner)
        - [draw_winning_line](#draw_winning_line)
        - [game_ober_msg](#game_ober_msg)
    - [Main Game](#main_game)
- [License](#license)

## Introduction
Tic-Tac-Toe is a game that consists of 2 players, X and O. They take turns marking the spaces in a 3x3 grid. If one player can place 3 consecutive marks in any orientation, they win. If no one succeeds, the game is over.

## Pre-requisites

- Python 3.x
- Pygame

## Installation
1. Clone the repository:
**Using SSH**:
```sh
git clone git@github.com:gadea-rodriguez/Tic-Tac-Toe.git
```
**Using HTTPS**:
```sh
git clone https://github.com/gadea-rodriguez/Tic-Tac-Toe.git
```

2. Install Requirements:
```sh
pip install pygame
```

## Usage
1. Run the game:
```sh
python Tic-Tac-Toe.py
```
2. Start playing the game by clicking on the empty spaces

## Code Explanation
### Functions
#### draw_playboard
This function draws the playboard with the grid and the white backgroung
```python
def draw_playboard():
    playboard.fill(white)
    for i in range(1,3):
        pygame.draw.line(playboard, black, (0,i*100), (300, i*100),2)
        pygame.draw.line(playboard, black, (i*100,0), (i*100, 300),2)
```
#### draw_player
This function draws each player's marks (X in red and O in blue) based on who is playing
```python
def draw_player():
    for i in range(9):
        x= (i % 3) * 100 + 50
        y= (i // 3) * 100 + 50
        #if player 1(x) is in a position in the playboard, we draw an x
        if positions[i] == "X":
            pygame.draw.line(playboard, red, (x - 25 , y - 25), (x + 25, y + 25) , 2)
            pygame.draw.line(playboard, red, (x - 25 , y + 25), (x + 25, y - 25) , 2)
        #if player 2 (o) is in the position, we drawa circle
        elif positions[i]== "O":
            pygame.draw.circle(playboard, blue , (x,y), 25, 2)
```

#### move
This function updates the positions list with the players move with X/O depending on who is playing
```python
def move (pos, player):
    position_board = positions.index(pos)
    positions[position_board]=player
```

#### winner
This function checks if someone has won yet by checking if any of the winning combinations is filled with one player's marks
```python
def winner ():
    win=""
    line = []
    for i in wins:
        if positions[i[0]] == positions[i[1]]== positions[i[2]] =="X":
            win = "X"
            line=i
        elif positions[i[0]] == positions[i[1]]== positions[i[2]] =="O":
            win = "O"
            line=i
    return win, line
```
#### draw_winning_line
This function draws a line over the winning combinartion if any player wins
```python
def draw_winning_line (line):
    if line:
        start_position = ((line[0]%3)*100 + 50, (line[0]//3)*100 + 50)
        end_position = ((line[2]%3)*100 + 50,(line[2]//3)*100 + 50)
        pygame.draw.line(playboard, purple , start_position, end_position, 5)
```

#### game_over_msg
This function shows a game over mesage on the playboard if no player has won and all the spots in the grid are filled
```python
def game_over_msg (message):
    font = pygame.font.Font(None, 72)
    text = font.render(message, True, white)
    #the center of the rectangle is on the center of the playboard
    rectangle = text.get_rect(center=(playboard_size[0]//2, playboard_size[1]//2))
    pygame.draw.rect(playboard,black, rectangle.inflate(22,22))
    playboard.blit(text, rectangle)
```
### Main Game
This part of the code handles the logic that the game follows, calling all the functions and making them work together
```python
game_over = False
#The game starts with player 1
player_1 = True
line=[]

while not game_over:
    #if the game is closed, we quit and exit the program 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        #if we click and the game is not over, we get the position
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            x, y = event.pos
            pos = (y // 100)*3 + (x//100)+1
            #if the position is valid, we check which player clicked 
            if pos in positions:
                if player_1:
                    player = "X"
                else:
                    player = "O"
                #we make the move
                move(pos,player)
                #we check if someone won yet
                win, line = winner()
                if win:
                    game_over = True
                elif all(isinstance(item, str) for item in positions):
                    game_over = True
                    win = "End"
                #if no one won, we print game over
                player_1 = not player_1
    draw_playboard()
    draw_player()
    draw_winning_line(line)
    pygame.display.update()


if win == "End":
    game_over_msg("Game Over")
else:
    game_over_msg(f"{win} won")


pygame.display.update()
pygame.time.wait(3000)       
pygame.quit()
```

## License
This project is licensed under the MIT license