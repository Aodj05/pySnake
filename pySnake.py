import pygame
import random
import sys

# Initialize
pygame.init()

# Game window
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snaku")

# Clock for controlling the frame rate
clock = pygame.time.Clock()

# Color definitions
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Grid setup
grid_size = 20
grid_width = screen_width // grid_size
grid_height = screen_height // grid_size

# Snake setup
snake_size = 1
snake_speed = 10

# Font
font = pygame.font.Font(None, 42)

# Direction coordinates
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# The speed at each level (in pixels/frame)
speeds = [10, 15, 20]

# Initial level assigned to a level variable
level = 0

# Drawing the text on the screen
def draw_text(text, color, x, y):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

# Generation of a random position on the grid
def get_random_position():
    x = random.randint(0, grid_width - 1) * grid_size
    y = random.randint(0, grid_height - 1) * grid_size
    return x, y

class Snake:
    def __init__(self):
        # The snake is made with one segment at the center
        self.segments = [(grid_width // 2 * grid_size, grid_height // 2 * grid_size)]
        self.direction = RIGHT
        self.grow = False
        self.speed = snake_speed

    def update(self):
        # Get current position of the snake's head
        x, y = self.segments[0]

        # Calculate the new position of the head in the current direction
        dx, dy = self.direction
        new_x = x + dx * grid_size
        new_y = y + dy * grid_size

        # Check if the new position of the head is outside the screen boundaries
        if (
            new_x < 0
            or new_x >= screen_width
            or new_y < 0
            or new_y >= screen_height
            or (new_x, new_y) in self.segments[1:]
        ):
            game_over()

        # Add the new position for the head to the front of the snake's segments
        self.segments.insert(0, (new_x, new_y))

        # Check if the snake hit food
        if (new_x, new_y) == food.position:
            # Increase the score
            global score
            score += 1
            # Spawn more food
            food.spawn()
            # Set grow flag to True
            self.grow = True
            # Check the food effect
            if food.effect == "speed_increase":
                # Modify the snake's speed
                global snake_speed
                self.speed *= 2  # Double the speed
            elif food.effect == "speed_decrease":
                # Modify the snake's speed to slow
                self.speed /= 2
            elif food.effect == "food_right_in_your_face":
                # spawn the next food piece right in front of the snake's mouth
                head_x, head_y = snake.segments[0]
                dx, dy = snake.direction
                new_x = head_x + dx * grid_size
                new_y = head_y + dy * grid_size
                food.position = (new_x, new_y)
        else:
            # If collision was not food, remove the last segment
            if not self.grow:
                self.segments.pop()
            else:
                self.grow = False

    def render(self):
        for segment in self.segments:
            pygame.draw.rect(screen, GREEN, (segment[0], segment[1], grid_size, grid_size))


class Food:
    def __init__(self):
        # Spawn food at a random position on the grid
        self.position = get_random_position()
        # Normal food
        self.effect = "normal"

    def spawn(self):
        # Spawn food at a random position on the grid
        self.position = get_random_position()
        self.effect = random.choice(["speed_increase", "speed_decrease", "food_right_in_your_face"])


    def render(self):
        pygame.draw.rect(screen, RED, (self.position[0], self.position[1], grid_size, grid_size))

def game_over():
    # Display end of game message
    draw_text("Game Over!", WHITE, screen_width // 2 - 100, screen_height // 2 - 18)
    pygame.display.flip()
    pygame.time.wait(2000)
    sys.exit()  # Exit the program

# Create snake and food
snake = Snake()
food = Food()

# Set initial score
score = 0

# Main game loop
running = True
while running:
    # Handle the events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            # Change the snake's direction using the arrow keys
            if event.key == pygame.K_UP and snake.direction != DOWN:
                snake.direction = UP
            elif event.key == pygame.K_DOWN and snake.direction != UP:
                snake.direction = DOWN
            elif event.key == pygame.K_LEFT and snake.direction != RIGHT:
                snake.direction = LEFT
            elif event.key == pygame.K_RIGHT and snake.direction != LEFT:
                snake.direction = RIGHT

    # Update the snake
    snake.update()

    # Update the snake's speed based on the current level
    snake_speed = speeds[level]

    # Increase level based on score condition
    if score > 5 and level < len(speeds) - 1:
        level += 1

    # Render the game objects
    screen.fill(BLACK)
    snake.render()
    food.render()

    # Score display
    draw_text("Score: " + str(score), WHITE, 10, 10)

    # Food effects text
    draw_text("Food Effect: " + food.effect, WHITE, 10, 50)

    # Update display
    pygame.display.flip()

    # Control the frame rate
    clock.tick(snake.speed)

# Close the Pygame window
pygame.quit()
