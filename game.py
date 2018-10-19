import pygame
from maze import Maze
from pacman import Pacman
from settings import Settings
from eventloop import EventLoop
from menu import Menu
from pygame import mixer
from os import path
from scoreboard import Scoreboard

class Game:
    BLACK = (0, 0, 0)

    def __init__(self):
        pygame.init()
        mixer.init()
        ai_settings = Settings()
        self.ai_settings = ai_settings
        self.screen = pygame.display.set_mode((self.ai_settings.screen_width, self.ai_settings.screen_height))
        pygame.display.set_caption("PacMan X Portal")
        self.dir = False
        self.menu = Menu(self.screen, 'PAC-MAN X PORTAL', 'HIGHSCORE:')
        self.sb = Scoreboard(self.ai_settings, self.screen)
        self.load_data()

        self.maze = Maze(self.screen, 'images/maze.txt', 'brick', 'dot', 'powerpill')

        self.pacman = Pacman(self.screen, self.ai_settings)

    def __str__(self): return 'Game(Pacman Portal), maze=' + str(self.maze) + ')'

    def load_data(self):
        self.dir = path.dirname(__file__)
        with open(path.join(self.dir, self.ai_settings.hs_file), 'r') as f:
            try:
                self.ai_settings.high_score = int(f.read())
            except:
                self.ai_settings.high_score = 0

    def play(self):
        eloop = EventLoop(self.ai_settings.finished)

        while not eloop.finished:
            eloop.check_events(self.ai_settings, self.menu, self.pacman)
            self.pacman.check_dot_collision(self.ai_settings, self.maze.dots, self.maze.pills, self.sb)
            self.sb.check_high_score(self.sb)
            self.update_screen()
            self.pacman.check_wall_collision(self.maze.bricks)
            self.pacman.update()

    def update_screen(self):
        self.screen.fill(Game.BLACK)

        if not self.ai_settings.finished:
            self.menu.draw_menu()
            self.sb.check_high_score(self.sb)
            self.sb.prep_high_score()
            self.sb.display_high_score()
        else:
            self.maze.blitme()
            self.pacman.blitme()
            self.sb.show_score()

        pygame.display.flip()


game = Game()
game.play()
