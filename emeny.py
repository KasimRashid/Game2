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
