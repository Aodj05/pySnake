import pygame
import random

# Initialize
pygame.init()

# game window
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snaku")

#clock for controlling the frame rate
clock = pygame.time.Clock()

# color definitions
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

#grid setup
grid_size = 20
grid_width = screen_width // grid_size
grid_height = screen_height // grid_size

#snake setup
snake_size = 1
snake_speed = 10

#font
font = pygame.font.Font(None, 42)

#direction coordinates
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

#drawing the text on the screen
def draw_text(text, color, x, y):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

#generation of a random position on the grid
def get_random_position():
    x = random.randint(0, grid_width - 1) * grid_size
    y = random.randint(0, grid_height - 1) * grid_size
    return x, y

class Snake:
    def __init__(self):
        #the snake is made with a one segment at the center
        self.segments = [(grid_width // 2 * grid_size, grid_height // 2 * grid_size)] # why // 2
        self.direction = RIGHT
        self.grow = False

    def update(self):
        # get current position if the snakes head
        x, y = self.segments[0]

        # calculate the new position of the head in the current direction
        dx, dy = self.direction
        new_x = x +dx * grid_size
        new_y = y + dy * grid_size

        # check when the new position of the head is outside of the screens boundaries
        if(new_x, new_y) in self.segments[1:]: # why 1: here
            game_over()

        # add new position for the head to the front of the snake's segments
        self.segments.insert(0, (new_x, new_y))

        #check if snake hit food
        if (new_x, new_y) == food.position:
            #increase the score
            global score
            score += 1
            # spawn more food
            food.spawn()
            # set grow flag to True
            self.grow = True
        else:
            # if collision was not food, remove the last segment
            if not self.grow:
                self.segments.pop()
            else:
                self.grow = False # explain to me why this whole if not
    
    def render(self):
        for segment in self.segments:
            pygame.draw.rect(screen, GREEN, (segment[0], segmant[1], grid_size, grid_size))# explain rect()

# class for food
class Food:
    def __init_(self):
        #spawn food at a random position on grid
        self.position = get_random_position()

    def render(self):
        pygame.draw.rect(screen, RED, (self.position[0], self.position[1], grid_size, grid_size)) #why grid_size twice

# handling game over
def game_over():
    #Display end of game message
    draw_text("Game Over!", WHITE, screen_width // 2 - 100, screen_height // screen_height // 2 - 18) #why 2 - 100 and 2-18
    pygame.display.flip()
    pygame.time.wait(2000)
    pygame.quit()

#create snake and food
snake = Snake()
food = Food()

# set initial score
score = 0

#main game loop
running = True #why running
while running:
#handle the events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            # change the snake's direction using the arrow keys
            if event.key == pygame.K_UP and snake.direction != DOWN:
                snake.direction = UP
            elif event.key == pygame.K_DOWN and snake.direction !=UP:
                snake.direction = DOWN
            elif event.key == pygame.K_LEFT and snake.direction != RIGHT:
                snake.direction = LEFT
            elif event.key == pygame.K_RIGHT and snake.direction != LEFT:
                snake.direction = RIGHT

    #update the snake
    snake.update()

    #render the game objects
    screen.fill(BLACK)
    snake.render()
    food.render()

    #score display
    draw_text("Score: " + str(score), WHITE, 10, 10) #what is str?

    #update display
    pygame.display.flip() #explain flip() to me?

    #control the frame rate
    clock.tick(snake_speed)

pygame.quit()
