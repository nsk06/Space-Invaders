import pygame
pygame.init()
myscreen = pygame.display.set_mode((800, 800))
pygame.font.init()
pygame.display.set_caption("My Space Invaders")


class Spaceship(pygame.sprite.Sprite):
    def __init__(self):
        self.myfont = pygame.font.SysFont('monospace', 100)
        self.textsurface = self.myfont.render("$", 1, (255, 255, 255))
        self.textsurface_left = myscreen.get_width()/2 - self.textsurface.get_width()/2
        self.textsurface_top = myscreen.get_height() - self.textsurface.get_height()
        self.textsurface_x = self.textsurface_left
        self.textsurface_y = self.textsurface_top
        self.textsurface_speed = 10
        self.poscord = pygame.rect.Rect(
            self.textsurface_x, self.textsurface_y, self.textsurface.get_width(), self.textsurface.get_height())

    def _update(self, newposx):
        self.textsurface_x = newposx
        self.poscord = pygame.rect.Rect(
            self.textsurface_x, self.textsurface_y, self.textsurface.get_width(), self.textsurface.get_height())
