import pygame
from snake import Snake
from apple import Apple
from utilites import *

PAGE_INIT = 0
START = 1
STARTED = 2
GAME_OVER = 3
PAUSED = 4
RETURN = 5

ENTER = 13
SPACE = 32
ESC = 27

WHITE = (255, 255, 255)
GRAY = (20, 20, 20)

pygame.init()
screen = pygame.display.set_mode((600, 600))
icon = pygame.image.load('media/snake.png')

pygame.display.set_caption('Snake')
pygame.display.set_icon(icon)

font30 = pygame.font.SysFont('ISOCPEUR', 30, 0)
font200 = pygame.font.SysFont('ISOCPEUR', 130, 0)

status = PAGE_INIT

snake = Snake()
apple = Apple()

running = True

clock = pygame.time.Clock()

while running:

    clock.tick(10)

    screen.fill(GRAY)

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

        text_init = font200.render(message_init, 1, WHITE)
        text_play = font30.render(message_play, 1, WHITE)

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

        score_multiple_of_ten = snake.score % 10 == 0
        if score_multiple_of_ten:
            snake.bonus_mixed_color()
    
        plot_in_surface(snake, apple, screen)

        message_score = f"SCORE: {snake.score}"
        text_score = font30.render(message_score, 1, WHITE)
        screen.blit(text_score, (15, 10))

    if status == GAME_OVER:
        plot_in_surface(snake, apple, screen)

        message_game = f"GAME"
        message_over = f"OVER"
        message_score = f"SCORE = {snake.score}"
        message_restart = f"Press space for restart!"

        text_game = font200.render(message_game, 1, WHITE)
        text_over = font200.render(message_over, 1, WHITE)
        text_score = font30.render(message_score, 1, WHITE)
        text_restart = font30.render(message_restart, 1, WHITE)

        screen.blit(text_game, (160, 150))
        screen.blit(text_over, (170, 250))
        screen.blit(text_score, (250, 400))
        screen.blit(text_restart, (185, 425))

    if status == PAUSED:
        snake.sleep()
        plot_in_surface(snake, apple, screen)

        message_game = f"GAME"
        message_paused = f"PAUSED"
        message_return = f"Press space for return to game"

        text_game = font200.render(message_game, 1, WHITE)
        text_paused = font200.render(message_paused, 1, WHITE)
        text_return = font30.render(message_return, 1, WHITE)

        screen.blit(text_game, (165, 180))
        screen.blit(text_paused, (120, 280))
        screen.blit(text_return, (150, 400))

    if status == RETURN:
        snake.wake_up()
        status = STARTED

    pygame.display.update()

pygame.quit()
