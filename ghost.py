import pygame
from pygame.sprite import Sprite
from dijkstra import dijkstra


class Ghost(Sprite):
    def __init__(self, screen, ai_settings):
        super(Ghost, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.screen_rect = screen.get_rect()

        self.images = []
        self.images.append(pygame.image.load('images/ghost_right-1.png'))
        self.images.append(pygame.image.load('images/ghost_right-2.png'))

        self.index = 0
        self.image = self.images[self.index]
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.rect.centerx = 460  # self.screen_rect.centerx + 15
        self.rect.centery = 280  # self.screen_rect.centery - (self.screen_rect.centery / 3) - 13
        self.x = float(self.rect.x)

        self.active = False
        self.start_node = 'dF'
        self.curr_node = 'dF'
        self.goal_node = []
        self.path_counter = 1

    def update(self, path):
        # a -> d = +int and a <- d = -int
        # col check
        if ord(self.curr_node[0]) < ord(path[self.path_counter][0]):
            self.rect.centery += 1
        elif ord(self.curr_node[0]) > ord(path[self.path_counter][0]):
            self.rect.centery -= 1
        # row check
        elif ord(self.curr_node[1]) < ord(path[self.path_counter][1]):
            self.rect.centerx += 1
        elif ord(self.curr_node[1]) > ord(path[self.path_counter][1]):
            self.rect.centerx -= 1

        # if collide rect is detected increase the respective col or row

        # animation -------------------------------
        # self.rect.x = self.x

        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]
        # -----------------------------------------

        # path = dijkstra(self.curr_node, 'hD')
        # print(path[0])

    def update_ghost(self, pacman, nodes):
        # find the nearest node to pacman
        self.goal_node = pacman.find_node(nodes)

        # find a path from current node to pacman node
        path = dijkstra(self.start_node, str(self.goal_node))
        self.curr_node = self.start_node

        # update direction according to label
        Ghost.update(self, path)
        # update next node by updating the label
        for node in nodes:
            if self.rect.center == node.rect.center:
                self.curr_node = path[self.path_counter]
                if self.curr_node == self.goal_node:
                    self.path_counter = 1
                    break
                else:
                    self.path_counter += 1
                    print(self.path_counter)
                    print(self.curr_node)
                    break

    def blitme(self):
        self.screen.blit(self.image, self.rect)
