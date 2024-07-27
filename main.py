import pygame
import sys
import math
from Player import move_player
from Environment import check_collision, draw_object, handle_collision
from Enemy import move_enemy, handle_enemy_collision, display_message
pygame.init()



def display_timer(screen, start_time, font, color, screen_width):
    """Display the elapsed time since the start of the game."""
    elapsed_time = (pygame.time.get_ticks() - start_time) / 1000  # convert to seconds
    timer_text = font.render(f'Time: {elapsed_time:.2f} s', True, color)
    screen.blit(timer_text, (10, 10))


# Set up the display
screen_width = 1200
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('My Pygame Window')

# Define colors
background_color = (0, 200, 150)  # RGB color (blue)

character_color = (255, 0, 0)     # RGB color (red)

#object_color = (0, 255, 0)        # RGB color (green)
object_color1 = (0, 255, 0)       # RGB color (green)
object_color2 = (255, 255, 0)     # RGB color (yellow)
enemy_color = (0, 0, 0)           # RGB color (black)
message_color = (255, 255, 255)   # RGB color (white)

character_size = 10
character_x = screen_width // 2
character_y = screen_height // 2
character_speed = .5

# Set up collidable objects
objects = [
        {'x': screen_width // 3, 'y': screen_height // 3, 'size': 100, 'color': object_color1},
        {'x': 2 * screen_width // 3, 'y': 2 * screen_height // 3, 'size': 100, 'color': object_color2}
    ]

# Set up enemy
enemy_size = 10
enemy_x = screen_width // 4
enemy_y = screen_height // 4
enemy_speed = .5


dash_speed = 6
dash_duration = 5  # frames
dash_cooldown = 60  # frames
dash_timer = 0

speed_boost = 10
boost_duration = 30  # frames
boost_timer = 0




 # Font for displaying message
font = pygame.font.SysFont(None, 55)

# Timer start
start_time = pygame.time.get_ticks()



 # Main loop
running = True
game_over = False
while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if not game_over:
            # Get key states
            keys = pygame.key.get_pressed()

            # Check for dash
            if keys[pygame.K_SPACE] and dash_timer == 0:
                dashing = True
                dash_timer = dash_duration + dash_cooldown
            else:
                dashing = dash_timer > dash_cooldown

            # Update dash timer
            if dash_timer > 0:
                dash_timer -= 1

            # Update character speed with boost
            character_speed_current = character_speed + (speed_boost if boost_timer > 0 else 0)
            
            # Update character position
            character_x, character_y = move_player(keys, character_x, character_y, character_speed_current, dash_speed, dashing, screen_width, screen_height, character_size)
            character_rect = pygame.Rect(character_x, character_y, character_size, character_size)

            # Update enemy position
            enemy_x, enemy_y = move_enemy(enemy_x, enemy_y, enemy_speed, character_x, character_y)
            enemy_rect = pygame.Rect(enemy_x, enemy_y, enemy_size, enemy_size)

            # Fill the background
            screen.fill(background_color)

            # Draw the character
            pygame.draw.rect(screen, character_color, character_rect)

            # Draw the enemy
            pygame.draw.rect(screen, enemy_color, enemy_rect)

            # Draw collidable objects and check for collisions
            for obj in objects:
                object_rect = draw_object(screen, obj['color'], obj['x'], obj['y'], obj['size'])
                if check_collision(character_rect, object_rect):
                    character_x, character_y, boost_timer = handle_collision(character_rect, object_rect, character_speed, speed_boost, boost_duration)
                    character_rect = pygame.Rect(character_x, character_y, character_size, character_size)
                    print("Collision detected with object! Player bounced and speed boosted.")

            # Check for collision between player and enemy
            if handle_enemy_collision(character_rect, enemy_rect):
                game_over = True

            # Update boost timer
            if boost_timer > 0:
                boost_timer -= 1
                        # Display the timer
            display_timer(screen, start_time, font, message_color, screen_width)
            
        else:
            # Display "You died" message
            display_message(screen, "You died", font, message_color, screen_width, screen_height)




        # Update the display
        pygame.display.flip()

pygame.quit()
sys.exit()

'''
 # Main loop
running = True
game_over = False
while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if not game_over:
            # Get key states
            keys = pygame.key.get_pressed()

            # Check for dash
            if keys[pygame.K_SPACE] and dash_timer == 0:
                dashing = True
                dash_timer = dash_duration + dash_cooldown
            else:
                dashing = dash_timer > dash_cooldown

            # Update dash timer
            if dash_timer > 0:
                dash_timer -= 1

            # Update character position
            character_speed_current = character_speed + (speed_boost if boost_timer > 0 else 0)
            character_x, character_y = move_player(keys, character_x, character_y, character_speed_current, dash_speed, dashing, screen_width, screen_height, character_size)
            character_rect = pygame.Rect(character_x, character_y, character_size, character_size)

            # Update enemy position
            enemy_x, enemy_y = move_enemy(enemy_x, enemy_y, enemy_speed, character_x, character_y)
            enemy_rect = pygame.Rect(enemy_x, enemy_y, enemy_size, enemy_size)

            # Fill the background
            screen.fill(background_color)

            # Draw the character
            pygame.draw.rect(screen, character_color, character_rect)

            # Draw the enemy
            pygame.draw.rect(screen, enemy_color, enemy_rect)

            # Draw collidable objects and check for collisions
            for obj in objects:
                object_rect = draw_object(screen, obj['color'], obj['x'], obj['y'], obj['size'])
                if check_collision(character_rect, object_rect):
                    character_x, character_y, speed_boost, boost_duration = handle_collision(character_rect, object_rect, character_speed, speed_boost, boost_duration)
                    character_rect = pygame.Rect(character_x, character_y, character_size, character_size)
                    boost_timer = boost_duration
                    print("Collision detected with object! Player bounced and speed boosted.")

            # Check for collision between player and enemy
            if handle_enemy_collision(character_rect, enemy_rect):
                game_over = True
        else:
            # Display "You died" message
            display_message(screen, "You died", font, message_color, screen_width, screen_height)





'''





        # Draw the collidable object
      #  object_rect = draw_object(screen, object_color, object_x, object_y, object_size)

        # Draw the collidable object2
       # object_rect2 = draw_object(screen, object_color, object_x+ 100 , object_y + 200, object_size2)

'''
# Main loop
game_over = False
running = True
while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


        
        if not game_over:
            # Get key states
            keys = pygame.key.get_pressed()
        # Get key states
        keys = pygame.key.get_pressed()

        # Check for dash
        if keys[pygame.K_SPACE] and dash_timer == 0:
            dashing = True
            dash_timer = dash_duration + dash_cooldown
        else:
            dashing = dash_timer > dash_cooldown

        # Update dash timer
        if dash_timer > 0:
            dash_timer -= 1

         # Update character position
        character_speed_current = character_speed + (speed_boost if boost_timer > 0 else 0)
        character_x, character_y = move_player(keys, character_x, character_y, character_speed_current, dash_speed, dashing, screen_width, screen_height, character_size)
        character_rect = pygame.Rect(character_x, character_y, character_size, character_size)

        #character_x, character_y = move_player(keys, character_x2, character_y2, character_speed_current, dash_speed, dashing, screen_width, screen_height, character_size)
        #character_rect = pygame.Rect(character_x2, character_y2, character_size, character_size)
 
     # Update enemy position
        enemy_x, enemy_y = move_enemy(enemy_x, enemy_y, enemy_speed, character_x, character_y)
        enemy_rect = pygame.Rect(enemy_x, enemy_y, enemy_size, enemy_size)



        # Fill the background
        screen.fill(background_color)

        # Draw the character
        pygame.draw.rect(screen, character_color, (character_x, character_y, character_size, character_size))#, #character_rect)

        # Draw the enemy
        pygame.draw.rect(screen, enemy_color, enemy_rect)


        # Draw collidable objects and check for collisions

        for obj in objects:
            object_rect = draw_object(screen, obj['color'], obj['x'], obj['y'], obj['size'])
            if check_collision(character_rect, object_rect):
                character_x, character_y, speed_boost, boost_duration = handle_collision(character_rect, object_rect, character_speed, speed_boost, boost_duration)
                character_rect = pygame.Rect(character_x, character_y, character_size, character_size)
                boost_timer = boost_duration
                print("Collision detected with object! Player bounced and speed boosted.")

        # Check for collision between player and enemy
        if handle_enemy_collision(character_rect, enemy_rect):
            game_over = True



        # Update boost timer
        if boost_timer > 0:
            boost_timer -= 1


        else:
            # Display "You died" message
            display_message(screen, "You died", font, message_color, screen_width, screen_height)

       # if check_collision(character_rect, object_rect):
        #    print("Collision detected!")



        # Update the display
        pygame.display.flip()

      
'''


