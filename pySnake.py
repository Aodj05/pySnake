import pygame
import random

# Initialize
pygame.init()

# game window
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snaku")

#clock for frame rate
clock = pygame.time.Clock()