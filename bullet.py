import pygame
import time
import sys
import os
import random
pygame.init()
myscreen = pygame.display.set_mode((800, 800))
pygame.font.init()
pygame.display.set_caption("My Space Invaders")


class Bullet(pygame.sprite.Sprite):
    def __init__(self, char):
        self.char = char
        self.b = pygame.font.SysFont('monospace', 20)
        self.bul = self.b.render(self.char, 1, (255, 255, 255))
        self.bul_y = 500
        self.bul_x = 500
        self.fire = "not"
        self.bul_speed = 10
        self.pos = pygame.rect.Rect(
            self.bul_x, self.bul_y, self.bul.get_width(), self.bul.get_height())

    def _update(self, newbulx, newbuly):
        self.bul_x = newbulx
        self.bul_y = newbuly
        self.pos = pygame.rect.Rect(
            self.bul_x, self.bul_y, self.bul.get_width(), self.bul.get_height())

    def is_collided_with(self, sprite):
        return self.pos.colliderect(sprite.pos)


class Iibullet(Bullet):
    def __init__(self):
        super(Iibullet, self).__init__("i")
        self.bul_speed = 10

    def collision(self, sprite):
        return super(Iibullet, self).is_collided_with(sprite)

    def _update(self, newx, newy):
        return super(Iibullet, self)._update(newx, newy)


class Ssbullet(Bullet):
    def __init__(self):
        super(Ssbullet, self).__init__("|")
        self.bul_speed = 20

    def collision(self, sprite):
        return super(Ssbullet, self).is_collided_with(sprite)

    def _update(self, newx, newy):
        return super(Ssbullet, self)._update(newx, newy)
