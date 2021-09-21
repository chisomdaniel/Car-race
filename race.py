import pygame
import random
import math

pygame.init()

# screen size
screen = pygame.display.set_mode((332, 600))

# Set icon and title
pygame.display.set_caption("Car Race")
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)

# Background Image
background = pygame.image.load("raceroad.png")

# Player Image and Co-ordinates
playerImg = pygame.image.load("player.png")
playerX = 134
playerY = 536
playerX_change = 0
playerY_change = 0
player_speed = 3
change_speed = 2.5
gameover = "no"

font = pygame.font.Font("freesansbold.ttf", 32)
score_value = 0
textX = 10  # the score coordinate on the screen
textY = 10

gameover_font = pygame.font.Font("freesansbold.ttf", 64)

# Bringing in the racing cars
racecarImg1 = pygame.image.load("racingcar1.png")  # Car 1
racecarX = 0
racecarY = -64
racecarY_change = 2

racecarImg2 = pygame.image.load("racingcar2.png")  # Car 2
racecar2X = 0
racecar2Y = -64

racecarImg3 = pygame.image.load("racingcar3.png")  # Car 3
racecar3X = 0

racecars = [racecarImg1, racecarImg2, racecarImg3]  # Sport Car loop
positions = {1: 50, 2: 134, 3: 218}
a = random.randint(1, 3)
b = random.randint(0, 2)
c = random.randint(1, 3)
d = random.randint(0, 2)
# call_car="yes"

# First Road line
road_lineImg = []
road_lineX = []
road_lineY = []
road_lineY_change = 1
road_line_position = (560, 480, 400, 320, 240, 160, 80, 0)

# Create different image of the white dash for the first side of the road
for i in road_line_position:
    road_lineImg.append(pygame.image.load("dash.png"))
    road_lineX.append(77)
    road_lineY.append(i)

# Second Road line
road_lineImg2 = []
road_lineX2 = []

# Create different image of the white dash for the second side of the road
for i in road_line_position:
    road_lineImg2.append(pygame.image.load("dash.png"))
    road_lineX2.append(161)

# Third Road line
road_lineImg3 = []
road_lineX3 = []

# Create different image of the white dash for the third side of the road
for i in road_line_position:
    road_lineImg3.append(pygame.image.load("dash.png"))
    road_lineX3.append(245)

# Function to draw the road line


def road_line(x, y, i):
    screen.blit(road_lineImg[i], (x, y))

# Function to draw the Second road line


def second_road_line(x, y, i):
    screen.blit(road_lineImg2[i], (x, y))

# Function to draw the Second road line


def third_road_line(x, y, i):
    screen.blit(road_lineImg3[i], (x, y))

# Function to draw the Player image


def player(x, y):
    screen.blit(playerImg, (x, y))


def racecar(x, y, i):  # Function draw the sport cars image
    screen.blit(racecars[i], (x, y))


def second_racecar(x, y, i):  # Function draw the sport cars image
    screen.blit(racecars[i], (x, y))


def iftouching(x1, y1, x2, y2):
    distance = math.sqrt(math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2))
    if distance >= 100:
        return True
    else:
        return False


def iftouchingplayer(x1, y1, x2, y2, a3, b3):
    distance = math.sqrt(math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2))
    distance2 = math.sqrt(math.pow(a3 - x2, 2) + math.pow(b3 - y2, 2))
    if distance <= 55 or distance2 <= 55:
        return True
    else:
        return False


def show_score(textX, textY):
    # rendering the score
    score = font.render("Score: " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (textX, textY))


def over(x, y, a, b):
    over = gameover_font.render("GAME", True, (0, 0, 0))
    text = gameover_font.render("OVER", True, (0, 0, 0))
    screen.blit(over, (x, y))
    screen.blit(text, (a, b))


running = True
while running:

    # Background image
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -player_speed
            if event.key == pygame.K_RIGHT:
                playerX_change = player_speed
            if event.key == pygame.K_UP:
                playerY_change = -player_speed
            if event.key == pygame.K_DOWN:
                playerY_change = player_speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerY_change = 0

    if iftouchingplayer(racecarX, racecarY, playerX, playerY, racecar2X, racecar2Y):
        gameover = "yes"
        # print("Score is " + str(score_value))
        # print("gameover")

    # Player Movement
    if gameover == "no":
        playerX += playerX_change
        playerY += playerY_change

    # Player Boundaries
    if playerY >= 536:
        playerY = 536
    if playerY <= 0:
        playerY = 0
    if playerX >= 228:
        playerX = 228
    if playerX <= 40:
        playerX = 40

    for i in range(8):
        road_line(road_lineX[i], road_lineY[i], i)

        if gameover == "no":
            road_lineY[i] += road_lineY_change
        if road_lineY[i] >= 600:
            road_lineY[i] = -40

    for i in range(8):
        second_road_line(road_lineX2[i], road_lineY[i], i)

    for i in range(8):
        third_road_line(road_lineX3[i], road_lineY[i], i)

    # Race cars
    if score_value >= change_speed:  # Increase the speed of the game
        racecarY_change += 0.1
        player_speed += 0.05
        change_speed += 2.5
        road_lineY_change += 0.1

    racecarX = positions[a]
    racecar(racecarX, racecarY, b)

    if gameover == "no":
        racecarY += racecarY_change
    if racecarY >= 600:
        a = random.randint(1, 3)
        b = random.randint(0, 2)
        racecarX = positions[a]
        racecarY = -64
        score_value += 1

    if iftouching(racecarX, racecarY, racecar2X, racecar2Y):
        racecar2X = positions[c]
        second_racecar(racecar2X, racecar2Y, d)

        if gameover == "no":
            racecar2Y += racecarY_change
        else:
            racecar2Y = racecar2Y

        if racecar2Y >= 600:
            c = random.randint(1, 3)
            d = random.randint(0, 2)
            racecar2X = positions[c]
            racecar2Y = -64
            score_value += 1

    player(playerX, playerY)
    show_score(textX, textY)

    if gameover == "yes":
        over(76, 236, 76, 300)

    pygame.display.update()
