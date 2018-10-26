import pygame
from imagerect import ImageRect
from node import Node


class Maze:
    RED = (255, 0, 0)
    # BRICK_SIZE = 13
    BRICK_SIZE = 20
    DOT_SIZE = 10
    PILL_SIZE = 20

    def __init__(self, screen, mazefile, brickfile, dotfile, powerpill):
        self.screen = screen
        self.filename = mazefile
        with open(self.filename, 'r') as f:
            self.rows = f.readlines()

        self.bricks = []

        self.dots = []
        # self.dots = Group()

        self.pills = []
        sz = Maze.BRICK_SIZE
        sz1 = Maze.DOT_SIZE
        sz2 = Maze.PILL_SIZE

        self.brick = ImageRect(screen, brickfile, sz, sz)

        self.dot = ImageRect(screen, dotfile, sz1, sz1)
        # self.dots.add(ImageRect(screen, dotfile, sz1, sz1))

        self.nodes = []

        self.pill = ImageRect(screen, powerpill, sz2, sz2)
        self.deltax = self.deltay = Maze.BRICK_SIZE

        self.build()

    def __str__(self): return 'maze(' + self.filename + ')'

    def build(self):
        r = self.brick.rect
        w, h = r.width, r.height
        dx, dy = self.deltax, self.deltay
        row_char = ''
        col_char = ''

        for nrow in range(len(self.rows)):
            row = self.rows[nrow]
            for ncol in range(len(row)):
                col = row[ncol]
                if ncol == 50 and col.isalpha() and col.islower():
                    row_char = col
                if col.isalpha() and col.isupper() and col != 'N' and col != 'X' and col != 'P':
                    col_char = col
                if col == 'X':
                    self.bricks.append(pygame.Rect(ncol * dx, nrow * dy, w, h))
                # create nodes for ghosts to navigate with using rect collide
                elif col == 'N':
                    row_label = str(row_char)
                    col_label = str(col_char)
                    label = str(row_label + col_label)
                    self.nodes.append(Node(ncol * dx, nrow * dy, label))
                elif col == 'o':
                    self.dots.append(pygame.Rect(ncol * dx, nrow * dy, w, h))
                elif col == 'P':
                    self.pills.append(pygame.Rect(ncol * dx, nrow * dy, w, h))

    def blitme(self):
        for rect in self.bricks:
            self.screen.blit(self.brick.image, rect)
        for rect in self.dots:
            self.screen.blit(self.dot.image, rect)
        for rect in self.pills:
            self.screen.blit(self.pill.image, rect)
        # draw nodes for testing
        for rect in self.nodes:
            pygame.draw.rect(self.screen, (230, 0, 0), rect, 1)
