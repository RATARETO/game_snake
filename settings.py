"""
Файл настроек, содержит все константы и переменные, а также инициализацию
"""


from random import randint, choice

from math import cos, sin, pi, radians

import pygame
from pygame.locals import Rect

# settings
WINDOW_SIZE = (640, 480)
TILE_SIZE = 20
WIDTH, HEIGHT = WINDOW_SIZE[0] // TILE_SIZE, WINDOW_SIZE[1] // TILE_SIZE

FPS = 20

# colors
ACTIVE_COLOR = (133, 133, 133)
INACTIVE_COLOR = (91, 93, 94)

COLOR_SNAKE = (54, 196, 242)

COLOR_APPLE = (255, 101, 54)


# init
window = pygame.display.set_mode(WINDOW_SIZE)
clock = pygame.time.Clock()

