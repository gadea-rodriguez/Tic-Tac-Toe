import pygame
import sys


#First, we initialize pygame
pygame.init()

#PLAYBOARD FOR THE GAME
#We use set_mode and set_caption to establish the size and title of the playboard
playboard_size = [300,300]
playboard = pygame.display.set_mode(playboard_size)
pygame.display.set_caption("Tic-Tac-Toe")

#We make a list with the possible squares or positions 
positions= [1,2,3,4,5,6,7,8,9]

#Now, we define the colors we are going to use in our game
#white for the background, black for the grid, red and blue for the players, purple for the winning line
white = [255,255,255]
black = [0,0,0]
blue = [0,0,255]
red = [255,0,0]
purple =[128,0,255]

#Now, we draw the playboard
def draw_playboard():
    playboard.fill(white)
    for i in range(1,3):
        pygame.draw.line(playboard, black, (0,i*100), (300, i*100),2)
        pygame.draw.line(playboard, black, (i*100,0), (i*100, 300),2)

#PLAYERS
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

#GAME
#We establish the possible wins
wins = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]

#We define a move
#We actualize the positio with the player symbol
def move (pos, player):
    position_board = positions.index(pos)
    positions[position_board]=player
    

#function to get the winner
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

#WINNING LINE
def draw_winning_line (line):
    if line:
        start_position = ((line[0]%3)*100 + 50, (line[0]//3)*100 + 50)
        end_position = ((line[2]%3)*100 + 50,(line[2]//3)*100 + 50)
        pygame.draw.line(playboard, purple , start_position, end_position, 5)

#GAME OVER
def game_over_msg (message):
    font = pygame.font.Font(None, 72)
    text = font.render(message, True, white)
    #the center of the rectangle is on the center of the playboard
    rectangle = text.get_rect(center=(playboard_size[0]//2, playboard_size[1]//2))
    pygame.draw.rect(playboard,black, rectangle.inflate(22,22))
    playboard.blit(text, rectangle)

#MAIN GAME

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



