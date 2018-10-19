import pygame


class Settings():
    def __init__(self):
        # screen settings
        self.screen_width = 975
        self.screen_height = 1200
        self.BLACK = 0, 0, 0

        # Music and Sounds
        pygame.mixer.music.load('sounds/pacman_theme.wav')
        self.waka = pygame.mixer.Sound('sounds/waka.wav')

        # pacman settings
        self.pacman_speed = 1

        # game_active flag
        self.finished = False