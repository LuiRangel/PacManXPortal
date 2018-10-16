import sys
import pygame


def check_keydown_events(event, pacman):
    if event.key == pygame.K_RIGHT:                                 #if the right arrow key is pressed...
        pacman.moving_right = True                                    #Set the flag = true to get the ship to move right
    elif event.key == pygame.K_LEFT:
        pacman.moving_left = True
    elif event.key == pygame.K_UP:                                 #if the right arrow key is pressed...
        pacman.moving_up = True                                    #Set the flag = true to get the ship to move right
    elif event.key == pygame.K_DOWN:
        pacman.moving_down = True
    elif event.key == pygame.K_q:
        sys.exit()


def check_wall_collision(pacman, bricks):
    # checks if there are any collisions with a wall.
    for brick in bricks:
        if pacman.rect.colliderect(brick):
            if pacman.moving_left:
                pacman.rect.left = brick.rect.right
            if pacman.moving_right:
                pacman.rect.right = brick.rect.left
            if pacman.moving_up:
                pacman.rect.top = brick.rect.bottom
            if pacman.moving_down:
                pacman.rect.bottom = brick.rect.top

