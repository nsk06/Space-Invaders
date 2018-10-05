import sys
import time
import pygame
import random
pygame.init()
myscreen = pygame.display.set_mode((800, 800))
pygame.font.init()
clock = pygame.time.Clock()
pygame.display.set_caption("My Space Invaders")

class Alien(pygame.sprite.Sprite):
    def __init__(self):
        self.char = "*"
        self.alien = pygame.font.SysFont('monospace', 60)
        self.alien = self.alien.render("*", 1, (255, 255, 255))
        self.alien_show = "true"
        self.alien_st = time.time()
        self.alien_x = random.randint(100, 700)
        self.alien_y = random.randint(0, 200)
        self.pos = pygame.rect.Rect(
            self.alien_x, self.alien_y, self.alien.get_width(), self.alien.get_height())
        self.col = False
        self._col = False

    def _updatech(self, ch):
        self.alien = pygame.font.SysFont('monospace', 60)
        self.alien = self.alien.render(ch, 1, (255, 255, 255))
