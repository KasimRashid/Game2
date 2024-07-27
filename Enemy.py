import pygame
import math

def move_enemy(enemy_x, enemy_y, enemy_speed, player_x, player_y):
    """Move the enemy towards the player's position."""
    dx = player_x - enemy_x
    dy = player_y - enemy_y
    distance = math.hypot(dx, dy)
    
    if distance != 0:
        dx /= distance
        dy /= distance

    enemy_x += dx * enemy_speed
    enemy_y += dy * enemy_speed

    return enemy_x, enemy_y


def handle_enemy_collision(player_rect, enemy_rect):
    """Check for collision between the player and enemy. Stop the game and display 'You died' if a collision occurs."""
    if player_rect.colliderect(enemy_rect):
        return True
    return False

def display_message(screen, message, font, color, screen_width, screen_height):
    """Display a message on the screen."""
    text = font.render(message, True, color)
    text_rect = text.get_rect(center=(screen_width // 2, screen_height // 2))
    screen.blit(text, text_rect)