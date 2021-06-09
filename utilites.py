def collision(position_object_1, position_object_2):
    return position_object_1 == position_object_2


def collision_between_body(snake_positions):
    for position in snake_positions[1:]:
        if collision(snake_positions[0], position):
            return True
    return False


def collision_on_the_wall(position_head):
    for position in position_head:
        if position < 0 or position > 580:
            return True
    return False


def plot_in_surface(snake, apple, screen):
    for position in snake.positions:
        screen.blit(snake.surface, position)

    screen.blit(apple.surface, apple.position)


def score_is_multiple_of_ten(score):
    return score % 10 == 0


