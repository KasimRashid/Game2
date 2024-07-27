import pygame

def check_collision(rect1, rect2):
    """Check if two rectangles (rect1 and rect2) collide."""
    return rect1.colliderect(rect2)

def draw_object(screen, color, x, y, size):
    """Draw a collidable object on the screen."""
    object_rect = pygame.Rect(x, y, size, size)
    pygame.draw.rect(screen, color, object_rect)
    return object_rect

def handle_collision(character_rect, object_rect, character_speed, speed_boost, boost_duration):
    """Handle the collision by bouncing the player away from the object and applying a speed boost."""
    if character_rect.colliderect(object_rect):
        dx = character_rect.centerx - object_rect.centerx
        dy = character_rect.centery - object_rect.centery

        if abs(dx) > abs(dy):  # Horizontal collision
            if dx > 0:
                character_rect.left = object_rect.right  # Move right
            else:
                character_rect.right = object_rect.left  # Move left
        else:  # Vertical collision
            if dy > 0:
                character_rect.top = object_rect.bottom  # Move down
            else:
                character_rect.bottom = object_rect.top  # Move up

        return character_rect.x, character_rect.y, boost_duration
    return character_rect.x, character_rect.y, 0


'''
def handle_collision(character_rect, object_rect, character_speed, speed_boost, boost_duration):
    """Handle the collision by bouncing the player away from the object and applying a speed boost."""
    if character_rect.colliderect(object_rect):
        dx = character_rect.centerx - object_rect.centerx
        dy = character_rect.centery - object_rect.centery

        if abs(dx) > abs(dy):  # Horizontal collision
            if dx > 0:
                character_rect.left = object_rect.right  # Move right
            else:
                character_rect.right = object_rect.left  # Move left
        else:  # Vertical collision
            if dy > 0:
                character_rect.top = object_rect.bottom  # Move down
            else:
                character_rect.bottom = object_rect.top  # Move up

        return character_rect.x, character_rect.y, speed_boost, boost_duration
    return character_rect.x, character_rect.y, 0, 0







'''