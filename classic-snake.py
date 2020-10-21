import pygame
from snake import Snake
from apple import Apple

PAGE_INIT = 0
START = 1
STARTED = 2
GAME_OVER = 3
PAUSED = 4
RETURN = 5

ENTER = 13
SPACE = 32
ESC = 27


def collision(position_object_1, position_object_2):
    return position_object_1 == position_object_2


def collision_between_body(snake_positions):
    for position in snake_positions[1:]:
        if collision(snake_positions[0], position):
            return True
    return False


def collision_on_the_wall(position_head):
    for position in position_head:
        if position < 0 or position > 600:
            return True
    return False


def plot_in_surface(snake, apple):
    for position in snake.positions:
        screen.blit(snake.surface, position)

    screen.blit(apple.surface, apple.position)

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Snake')

icon = pygame.image.load('media/snake.png')
pygame.display.set_icon(icon)

white = (255, 255, 255)
font30 = pygame.font.SysFont('ISOCPEUR', 30, 0)
font200 = pygame.font.SysFont('ISOCPEUR', 130, 0)

status = PAGE_INIT

snake = Snake()
apple = Apple()

running = True
clock = pygame.time.Clock()

while running:

    clock.tick(10)

    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == ENTER and status == PAGE_INIT:
                status = START
            if event.key == SPACE and status == GAME_OVER:
                status = START
            if event.key == ESC and status == STARTED:
                status = PAUSED
            if event.key == SPACE and status == PAUSED:
                status = RETURN

            if status == STARTED:
                if event.key == pygame.K_UP:
                    snake.new_direction(Snake.UP)
                if event.key == pygame.K_DOWN:
                    snake.new_direction(Snake.DOWN)
                if event.key == pygame.K_RIGHT:
                    snake.new_direction(Snake.RIGHT)
                if event.key == pygame.K_LEFT:
                    snake.new_direction(Snake.LEFT)

    if status == START:

        snake = Snake()
        apple = Apple()

        status = STARTED

    if status == PAGE_INIT:
        message_init = f"SNAKE.PY"
        message_play = f"Press enter for play"

        text_init = font200.render(message_init, 1, white)
        text_play = font30.render(message_play, 1, white)

        screen.blit(text_init, (60, 200))
        screen.blit(text_play, (200, 300))

    if status == STARTED:

        snake.update_positions()
        snake.move()

        if collision(snake.positions[0], apple.position):
            apple.new_position()
            snake.ate_apple()

        if collision_between_body(snake.positions) or collision_on_the_wall(snake.positions[0]):
            snake.death()
            status = GAME_OVER

        plot_in_surface(snake, apple)

        message_score = f"SCORE: {snake.score}"
        text_score = font30.render(message_score, 1, white)
        screen.blit(text_score, (15, 10))

    if status == GAME_OVER:
        plot_in_surface(snake, apple)

        message_game = f"GAME"
        message_over = f"OVER"
        message_score = f"SCORE = {snake.score}"
        message_restart = f"Press space for restart!"

        text_game = font200.render(message_game, 1, white)
        text_over = font200.render(message_over, 1, white)
        text_score = font30.render(message_score, 1, white)
        text_restart = font30.render(message_restart, 1, white)

        screen.blit(text_game, (160, 150))
        screen.blit(text_over, (170, 250))
        screen.blit(text_score, (250, 400))
        screen.blit(text_restart, (185, 425))

    if status == PAUSED:
        snake.sleep()
        plot_in_surface(snake, apple)

        message_game = f"GAME"
        message_paused = f"PAUSED"
        message_return = f"Press space for return to game"

        text_game = font200.render(message_game, 1, white)
        text_paused = font200.render(message_paused, 1, white)
        text_return = font30.render(message_return, 1, white)

        screen.blit(text_game, (165, 180))
        screen.blit(text_paused, (120, 280))
        screen.blit(text_return, (150, 400))

    if status == RETURN:
        snake.wake_up()
        status = STARTED

    pygame.display.update()

pygame.quit()
