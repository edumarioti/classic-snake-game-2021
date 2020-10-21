import pygame
from snake import Snake
from apple import Apple

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Snake')

running = True
clock = pygame.time.Clock()

# size -> variavel utilizada nos testes de escala do jogo
size = (20, 20)

snake = Snake(size=size)
apple = Apple(size=size)


def collision(position_object_1, position_object_2):
    return position_object_1 == position_object_2


def collision_between_body(snake_positions):

    for position in snake_positions[1:]:
        if collision(snake_positions[0], position):
            return True
    return False


def collision_on_the_wall(snake_positions):
    for position_head in snake_positions[0]:
        if position_head < 0 or position_head > 600:
            return True
    return False


while running:

    clock.tick(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.new_direction(Snake.UP)
            if event.key == pygame.K_DOWN:
                snake.new_direction(Snake.DOWN)
            if event.key == pygame.K_RIGHT:
                snake.new_direction(Snake.RIGHT)
            if event.key == pygame.K_LEFT:
                snake.new_direction(Snake.LEFT)

    screen.fill((0, 0, 0))

    if collision(snake.positions[0], apple.position):
        apple.new_position()
        snake.ate_apple()
        print(snake.score)

    if collision_between_body(snake.positions) or collision_on_the_wall(snake.positions):
        snake.death()

    for position in snake.positions:
        screen.blit(snake.surface, position)

    screen.blit(apple.surface, apple.position)

    snake.update_positions()
    snake.move()
    pygame.display.update()

pygame.quit()
