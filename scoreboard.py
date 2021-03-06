import pygame.font
from os import path


class Scoreboard:

    def __init__(self, ai_settings, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings

        self.hs_text_color = (254, 249, 27)
        self.s_text_color = (230, 230, 230)
        self.font = pygame.font.SysFont('helvetica', 48)

        self.score_rect = False
        self.score_image = False
        self.high_score_image = False
        self.high_score_rect = False
        self.dir = False
        self.prep_score()
        self.prep_high_score()

    def prep_score(self):
        score = round(self.ai_settings.score)
        score_str = "{:,}".format(score)
        self.score_image = self.font.render(score_str, True, self.s_text_color, self.ai_settings.BLACK)

        self.score_rect = self.score_image.get_rect()
        self.score_rect.centerx = self.screen_rect.left + 100
        self.score_rect.centery = (self.screen_rect.height / 2) - 130

    def prep_high_score(self):
        high_score = int(round(self.ai_settings.high_score, -1))
        high_score_str = "{:,}".format(high_score)

        self.high_score_image = self.font.render(high_score_str, True, self.hs_text_color, self.ai_settings.BLACK)
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.right - 100
        self.high_score_rect.centery = (self.screen_rect.height / 2) - 130

    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)

    def display_high_score(self):
        self.screen.blit(self.high_score_image, self.high_score_rect)

    def check_high_score(self, sb):
        if self.ai_settings.score > self.ai_settings.high_score:
            self.ai_settings.high_score = self.ai_settings.score
            self.dir = path.dirname(__file__)
            with open(path.join(self.dir, self.ai_settings.hs_file), 'w') as f:
                f.write(str(self.ai_settings.high_score))
        sb.prep_high_score()
