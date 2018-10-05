import pygame
import time
import sys
import os
import random
from spaceship import *
from alien import *
from bullet import *

pygame.init()
myscreen = pygame.display.set_mode((800, 800))
pygame.font.init()
clock = pygame.time.Clock()
pygame.display.set_caption("My Space Invaders")
res = 0
ship = Spaceship()
aliens = []
ob = Alien()
aliens.append(ob)
Ibullet = []
Sbullet = []
aliencount = 1
st = time.time()
tex = pygame.font.SysFont("Times New Roman", 18)
text = tex.render("SCORE:", 1, (255, 255, 255))
if __name__ == "__main__":
    while True:
        clock.tick(30)
        myscreen.fill((0, 0, 0))
        myscreen.blit(ship.textsurface,
                      (ship.textsurface_x, ship.textsurface_y))
        cur_time = time.time()
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_q]:
            sys.exit()
        if pressed[pygame.K_a]:
            ship._update(ship.textsurface_x - ship.textsurface_speed)
            if ship.textsurface_x < 0:
                ship._update(0)
        if pressed[pygame.K_d]:
            ship._update(ship.textsurface_x + ship.textsurface_speed)
            if ship.textsurface_x > 740:
                ship._update(740)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    mybul = Iibullet()
                    if mybul.fire == "not":
                        mybul.fire = "ready"
                        mybul.bul_x = int(
                            ship.textsurface_x + ship.textsurface.get_width())
                        mybul.bul_y = int(ship.textsurface_y+10)
                        Ibullet.append(mybul)
                if event.key == pygame.K_s:
                    Mybul = Ssbullet()
                    if Mybul.fire == "not":
                        Mybul.fire = "ready"
                        Mybul.bul_x = int(
                            ship.textsurface_x + ship.textsurface.get_width())
                        Mybul.bul_y = int(ship.textsurface_y+10)
                        Sbullet.append(Mybul)
        if (int(cur_time) - int(st)) > 10:
            st = time.time()
            aliens.append(Alien())
            aliencount += 1
        for alien in aliens:
            if cur_time - alien.alien_st < 8 and alien.col == False:
                myscreen.blit(alien.alien, (alien.alien_x, alien.alien_y))
            if cur_time - alien.alien_st > 8:
                aliens.remove(alien)
                aliencount -= 1
        for mybul in Ibullet:
            if mybul.fire == "ready":
                mybul.fire = "firing"
            if mybul.fire == "firing":
                mybul._update(mybul.bul_x, mybul.bul_y-mybul.bul_speed)
                myscreen.blit(mybul.bul, (mybul.bul_x, mybul.bul_y))
            if mybul.bul_y < 0:
                Ibullet.remove(mybul)
            for alien in aliens:
                if mybul.collision(alien) and alien.col == False:
                    alien.col = True
                    aliens.remove(alien)
                    aliencount -= 1
                    res += 1
        for Mybul in Sbullet:
            if Mybul.fire == "ready":
                Mybul.fire = "firing"
            if Mybul.fire == "firing":
                Mybul._update(Mybul.bul_x, Mybul.bul_y-Mybul.bul_speed)
                myscreen.blit(Mybul.bul, (Mybul.bul_x, Mybul.bul_y))
            if Mybul.bul_y < 0:
                Sbullet.remove(Mybul)
            for alien in aliens:
                if Mybul.collision(alien) and alien.col == False:
                    if alien._col == False:
                        res += 1
                    alien._col = True
                    alien.alien_st += 5
                    alien._updatech("@")
        resdis = tex.render(str(res), 1, (255, 255, 255))
        myscreen.blit(text, (400, 450))
        myscreen.blit(resdis, (475, 450))
        pygame.display.update()
