"""
файл для запуска игры, содержит в себе основной цикл игры и обработчик событий
"""

from Objects import *

pygame.display.set_caption("Snake")

background = Background()

snake = Snake()
# snake.set_length_snake(10)

apple = Apple()

while True:

    background.draw()

    apple.draw()

    snake.draw()

    snake.eat(apple)
    snake.move()

    for envent in pygame.event.get():
        if envent.type == pygame.QUIT:
            pygame.quit()
            quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            snake.direction += pi / 2
        elif keys[pygame.K_RIGHT]:
            snake.direction -= pi / 2

    pygame.display.update()
    clock.tick(FPS)
