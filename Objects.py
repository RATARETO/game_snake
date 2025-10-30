"""
Объекты игры - Snake и Apple, а также Background
"""

from settings import *


class Snake:
    def __init__(self):
        """
        points[0] - голова

        содержит поля:
            points - список объектов Rect, описывающих тело змеи
            deirection - угол поворота головы в радианах
        """
        self.body_color = COLOR_SNAKE
        self.direction = radians(0)
        self.points = [
            Rect(
                randint(0, WIDTH - 1) * TILE_SIZE,
                randint(0, HEIGHT - 1) * TILE_SIZE,
                TILE_SIZE,
                TILE_SIZE
            ),
        ]

    def set_length_snake(self, num):
        """
        функция для установки длины змеи
        :param num: int - длина змеи
        :return: None
        """
        for i in range(1, num):
            self.points.append(
                Rect(
                    self.points[0].x + TILE_SIZE * i,
                    self.points[0].y,
                    TILE_SIZE,
                    TILE_SIZE
                )
            )

    def draw(self):
        """
        отрисовка змеи
        :return: None
        """
        for point in self.points:
            pygame.draw.rect(window, self.body_color, point)

    def move(self):
        """
        движение змеи
            1. при выходе за границы поля, змея появляется с другой стороны поля
            2. перемещение тела
            3. перемещение головы
            4. конец игры при столкновении с собой

        :return: None
        """
        # конец игры при столкновении с собой
        for i in range(0, len(self.points) - 1):
            if self.points[i] in self.points[: i] + self.points[i + 1:]:
                exit()

        # перемещение тела
        for i in range(1, len(self.points)):
            self.points[-i].x = self.points[-i - 1].x
            self.points[-i].y = self.points[-i - 1].y

            # столкновение с границами поля
            if self.points[0].x < 0:
                self.points[0].x = WIDTH * TILE_SIZE
            if self.points[0].x > WIDTH * TILE_SIZE:
                self.points[0].x = 0
            if self.points[0].y < 0:
                self.points[0].y = HEIGHT * TILE_SIZE
            if self.points[0].y > HEIGHT * TILE_SIZE:
                self.points[0].y = 0

        # перемещение головы
        self.points[0].x -= TILE_SIZE * cos(self.direction)
        self.points[0].y += TILE_SIZE * sin(self.direction)

    def eat(self, apple):
        """
        змея съедает яблоко и увеличивает свой размер
        :param apple: Apple - объект яблоко
        :return: None

        боги змей едят только яблоки (;
        """
        if self.points[0] == apple.rect:
            apple.set_random_position()

            self.points.append(
                Rect(
                    self.points[-1].x * cos(self.direction),
                    self.points[-1].y * sin(self.direction),
                    TILE_SIZE,
                    TILE_SIZE
                    
                )
            )


class Apple:
    def __init__(self):
        """
        клфасс яблоко
        """
        self.color = COLOR_APPLE
        self.rect = Rect(
                randint(0, WIDTH - 1) * TILE_SIZE,
                randint(0, HEIGHT - 1) * TILE_SIZE,
                TILE_SIZE,
                TILE_SIZE
            )

    def draw(self):
        """
        отрисовка яблока
        :return:
        """
        pygame.draw.rect(window, self.color, self.rect)

    def set_random_position(self):
        """
        случайное положение яблока
        :return:
        """
        self.rect = Rect(
            randint(0, WIDTH - 1) * TILE_SIZE,
            randint(0, HEIGHT - 1) * TILE_SIZE,
            TILE_SIZE,
            TILE_SIZE
        )


class Background:
    def __init__(self):
        """
        класс фона
            active_color - цвет светлой клетки
            inactive_color - цвет тёмной клетки
        """
        self.active_color = ACTIVE_COLOR
        self.inactive_color = INACTIVE_COLOR

    def draw(self):
        """
        отрисовка поля чередованием цветов клеток
        :return: None
        """
        for i in range(0, WIDTH):
            for j in range(0, HEIGHT):
                if (i + j) % 2 == 0:
                    pygame.draw.rect(
                        window, self.active_color, (i * TILE_SIZE, j * TILE_SIZE, TILE_SIZE, TILE_SIZE)
                    )
                else:
                    pygame.draw.rect(
                        window, self.inactive_color, (i * TILE_SIZE, j * TILE_SIZE, TILE_SIZE, TILE_SIZE)
                    )


