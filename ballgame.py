#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 600, 400
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jumping Ball Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Ball properties
BALL_RADIUS = 20
BALL_X = 100
BALL_Y = HEIGHT // 2
BALL_SPEED_Y = 0
GRAVITY = 0.5

# Hurdle properties
HURDLE_WIDTH = 50
HURDLE_HEIGHT = 300
HURDLE_GAP = 150
HURDLE_SPEED = 3
hurdles = []

# Fonts
FONT = pygame.font.SysFont('comicsans', 30)

# Function to create a new hurdle
def create_hurdle():
    hurdle_height = random.randint(50, HEIGHT - HURDLE_GAP - 50)
    top_hurdle = pygame.Rect(WIDTH, 0, HURDLE_WIDTH, hurdle_height)
    bottom_hurdle = pygame.Rect(WIDTH, hurdle_height + HURDLE_GAP, HURDLE_WIDTH, HEIGHT - hurdle_height - HURDLE_GAP)
    hurdles.append(top_hurdle)
    hurdles.append(bottom_hurdle)

# Function to draw the game objects
def draw():
    WIN.fill(WHITE)
    pygame.draw.circle(WIN, BLACK, (BALL_X, BALL_Y), BALL_RADIUS)
    for hurdle in hurdles:
        pygame.draw.rect(WIN, BLACK, hurdle)
    pygame.display.update()

# Function to move the ball
def move_ball():
    global BALL_Y, BALL_SPEED_Y
    BALL_SPEED_Y += GRAVITY
    BALL_Y += BALL_SPEED_Y

# Function to move the hurdles
def move_hurdles():
    for hurdle in hurdles:
        hurdle.x -= HURDLE_SPEED
    if hurdles and hurdles[0].x < -HURDLE_WIDTH:
        hurdles.pop(0)
        hurdles.pop(0)

# Function to check for collisions
def check_collisions():
    for hurdle in hurdles:
        if hurdle.colliderect((BALL_X - BALL_RADIUS, BALL_Y - BALL_RADIUS, 2 * BALL_RADIUS, 2 * BALL_RADIUS)):
            return True
    return False

# Main game loop
clock = pygame.time.Clock()
score = 0
create_hurdle()

running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                BALL_SPEED_Y = -10

    move_ball()
    move_hurdles()
    if hurdles[-1].x < WIDTH - 200:
        create_hurdle()

    if check_collisions():
        running = False

    draw()

pygame.quit()
sys.exit()


# In[2]:


pip install pygame


# In[7]:


import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 600, 400
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jumping Ball Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Ball properties
BALL_RADIUS = 20
BALL_X = 100
BALL_Y = HEIGHT // 2
BALL_SPEED_Y = 0
GRAVITY = 0.5

# Hurdle properties
HURDLE_WIDTH = 50
HURDLE_HEIGHT = 300
HURDLE_GAP = 150
HURDLE_SPEED = 3
hurdles = []

# Fonts
FONT = pygame.font.SysFont('comicsans', 30)

# Function to create a new hurdle
def create_hurdle():
    hurdle_height = random.randint(50, HEIGHT - HURDLE_GAP - 50)
    top_hurdle = pygame.Rect(WIDTH, 0, HURDLE_WIDTH, hurdle_height)
    bottom_hurdle = pygame.Rect(WIDTH, hurdle_height + HURDLE_GAP, HURDLE_WIDTH, HEIGHT - hurdle_height - HURDLE_GAP)
    hurdles.append(top_hurdle)
    hurdles.append(bottom_hurdle)

# Function to draw the game objects
def draw():
    WIN.fill(WHITE)
    pygame.draw.circle(WIN, BLACK, (BALL_X, BALL_Y), BALL_RADIUS)
    for hurdle in hurdles:
        pygame.draw.rect(WIN, BLACK, hurdle)
    pygame.display.update()

# Function to move the ball
def move_ball():
    global BALL_Y, BALL_SPEED_Y
    BALL_SPEED_Y += GRAVITY
    BALL_Y += BALL_SPEED_Y

# Function to move the hurdles
def move_hurdles():
    for hurdle in hurdles:
        hurdle.x -= HURDLE_SPEED
    if hurdles and hurdles[0].x < -HURDLE_WIDTH:
        hurdles.pop(0)
        hurdles.pop(0)

# Function to check for collisions
def check_collisions():
    for hurdle in hurdles:
        if hurdle.colliderect((BALL_X - BALL_RADIUS, BALL_Y - BALL_RADIUS, 2 * BALL_RADIUS, 2 * BALL_RADIUS)):
            return True
    return False

# Main game loop
clock = pygame.time.Clock()
score = 0
create_hurdle()

running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                BALL_SPEED_Y = -10

    move_ball()
    move_hurdles()
    if hurdles[-1].x < WIDTH - 200:
        create_hurdle()

    if check_collisions():
        running = False

    draw()

pygame.quit()
sys.exit()


# In[ ]:





# In[ ]:




