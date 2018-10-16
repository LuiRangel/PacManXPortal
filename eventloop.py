import pygame
import sys


class EventLoop:
    def __init__(self, finished):
        self.finished = finished

    def __str__(self): return 'eventloop, finished=' + str(self.finished) + ')'

    @staticmethod
    def check_events(ai_settings, menu, pacman):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                EventLoop.check_keydown_events(event, pacman)
            if event.type == pygame.KEYUP:
                EventLoop.check_keyup_events(event, pacman)
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                EventLoop.check_play_button(ai_settings, menu, mouse_x, mouse_y)

    @staticmethod
    def check_keydown_events(event, pacman):
        if event.key == pygame.K_RIGHT:
            pacman.moving_right = True
        elif event.key == pygame.K_LEFT:
            pacman.moving_left = True
        elif event.key == pygame.K_UP:
            pacman.moving_up = True
        elif event.key == pygame.K_DOWN:
            pacman.moving_down = True
            # elif event.key == pygame.K_SPACE:
            # fire_bullet(ai_settings, screen, ship, bullets)
        elif event.key == pygame.K_q:
            sys.exit()

    @staticmethod
    def check_keyup_events(event, pacman):
        if event.key == pygame.K_RIGHT:  # if the right arrow key is pressed...
            pacman.moving_right = False  # Set the flag = true to get the ship to move right
        elif event.key == pygame.K_LEFT:
            pacman.moving_left = False
        elif event.key == pygame.K_UP:  # if the right arrow key is pressed...
            pacman.moving_up = False  # Set the flag = true to get the ship to move right
        elif event.key == pygame.K_DOWN:
            pacman.moving_down = False

    @staticmethod
    def check_play_button(ai_settings, menu, mouse_x, mouse_y):
        """Starts a new game when the player clicks play"""
        button_clicked = menu.play_button.rect.collidepoint(mouse_x, mouse_y)
        if button_clicked and not ai_settings.finished:
            pygame.mixer.music.play(0)
            # Hide the mouse cursor.
            pygame.mouse.set_visible(False)
            ai_settings.finished = True
