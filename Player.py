import pygame


def move_player(keys, character_x, character_y, character_speed, dash_speed, dashing, screen_width, screen_height, character_size):
    """Update the player's position based on the keys pressed and keep the player within the window bounds."""
    speed = dash_speed if dashing else character_speed

    if keys[pygame.K_LEFT] and character_x - speed >= 0:
        character_x -= speed
    if keys[pygame.K_RIGHT] and character_x + speed + character_size <= screen_width:
        character_x += speed
    if keys[pygame.K_UP] and character_y - speed >= 0:
        character_y -= speed
    if keys[pygame.K_DOWN] and character_y + speed + character_size <= screen_height:
        character_y += speed

    return character_x, character_y

