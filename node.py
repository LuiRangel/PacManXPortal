import pygame


class Node:
    def __init__(self, x, y, label):
        self.label = label
        self.rect = pygame.Rect(x, y, 1, 1)
