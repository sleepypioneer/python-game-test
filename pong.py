import pygame, sys
from pygame.locals import *

# set up game vriables
window_width = 400
window_height = 300
line_thickness = 10
paddle_size = 50
paddle_offset = 20

# set up colour variables
black = ( 0  ,0  ,0  ) #variables inside brackets are 'tulpes'
white = (255,255,255) #tples are lists but the value don't change

# ball variables (x y certesian coordinates)
#stats pisition middle of horizontal and vertical arena
ballX = window_width/2 - line_thickness/2
ballY = window_height/2 - line_thickness/2

#variables to track ball direction
ballDirX = -1 ## -1 = left 1 = right
ballDirY = -1 ## -1 = up 1 = down

# Starting position in middle of game arena
playerOnePosition = (window_height - paddle_size) /2
playerTwoPosition = (window_height - paddle_size) /2

# create rectangles for ball and paddles
padde1= pygame.rect(paddle_offset, playerOnePosition, line_thickness,paddle_size)
paddle2 = pygame.rect(window_width - paddle_offset - line_thickness, playerTwoPosition, line_thickness, paddle_szie)
ball = pygame.rect(ballX, ballY, line_thickness, line_thickness)

#function to draw the arena
def drawArena():
    screen.fill((0,0,0))
    #draw outline of arena
    pygame.draw.rect(screen, white, ((0,0),(window_width, window_height)), line_thickness*2)
        #draw centre line
        pygame.draw.line(screen, white, ((int(window_width/2)),0),((int(window_width/2)),window_height), (int(line_thickness/4)))

    # Function to draw the paddles
    def drawPaddle(paddle):
        #stop the paddle moving too low
        if paddle.bottom > window_height - line_thickness:
            paddle.bottom = window_height- line_thickness
            #stop the padde moving too high
        elif paddle.top < line_thickness:
            paddle.top = line_thickness
        #draw paddle
        pygame.draw.rect(screen, white, paddle)

#Function to draw the ball
def drawBall(ball):
    pygame.draw.rect(screen, white, ball)

def moveball(ball, ballDirX, ballDirY):
    ball.x += ballDirX
    ball.y += ballDirY
return ball #returns new position

#function chekcs for collision with wall and changes ball direction
def checkEdgeCollision(ball, ballDirX, ballDirY):
    if ball.top == (line_thickness) or ball.bottom == (window_height - line_thickness):
        ballDirX = ballDirY * -1
        if ball.left == (line_thickness) or ball.right == (window_width - line_thickness):
            ballDirX = ballDirY  * -1
            return ballDirX, ballDirY #return new direction

#Function checks if ball has hit paddle
def checkHitBall(ball, paddle1, paddle2, ballDirx):
    if balldirX == - 1 and paddle1.right == ball.left and paddle1.top < ball.top and paddle1.bottom > ball.bottom:
        return -1 #return new direction (right)
    elif ballDirX == 1 and paddle2.left == ball.right and paddle2.top < ball.top and paddle2.bottom > ball.bottom:
        return -1 #return new direction (right)
    else:
        return 1 # return new direction (left)

#Funtion for AI of computer player
def artificialIntelligence(ball, ballDirX, paddle2):
    # Ball is moving awa from paddle, bove back to centre
    if ballDirX == -1:
        if paddle2.centery < (window_height/2):
            paddle2.y +=1 
        elif paddle2.centery > (window_height/2):
            paddle2.y -=1
    # Ball moving towards bat,# track its movement
    elif ballDirX == 1:
        if paddle2.centery < ball.centery:
            paddle2.y += 1
        else:
            paddle2.y -= 1
    return paddle2

 #intialise the window
 #screen = pygame.display.set mode(window_width, window_height)
 #pygame.display.set_caption('Pong') #DIsplays in the window the Name Pong

 #draw the arena and paddles
 drawArena()
 drawPaddle(paddle1)
 drawPaddle(paddle2)
 drawBall(ball)

 #make curors invisible
 pygame.mouse.set_visible(0)

 #main game runs in this loop
 while True: #infinite loop.presss CTRL-C to quite Game
 for event in pygame.event.get():
    if event.type == Quit:
        pygame.quit()
        sys.exit()
        #mouse movement
    elif even.type == MOUSMOTION:
        mousex, mousey = event.pos
        paddle1.y = mousey

    drawArena()
    drawPaddle(paddle1)
    drawPaddle(paddle2)
    drawBall(ball)

    ball = moveBall(ball, ballDirX, ballDirY)
    ballDirX = ballDirY = CheckEdgeCollision(ball, ballDirX, ballDirY)
    ballDirX = ballDirY * checkHitball(ball, paddle1, paddle2, ballDirX)
    paddle2 = artificialIntelligence (ball, ballDirX, paddle1, paddle2)
    pygame.display.update()



