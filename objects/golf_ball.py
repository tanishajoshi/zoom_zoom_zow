import os
import math

import pygame


class GolfBall(pygame.sprite.Sprite):

    def __init__(self, screen):
        super(GolfBall, self).__init__()
        self.size = 80, 48
        self.screen = screen
        self.image = pygame.transform.scale(
            pygame.image.load(
                os.path.join(os.getcwd(), "resources", "golf_ball.png")
            ).convert(),
            self.size
        )
        self.rect = self.image.get_rect()
        self.vector = (0, 0)
        self.speed = 1

    def update(self, pressed_keys):
        if pressed_keys[pygame.K_UP]:
            self.vector = (0, -self.speed)
        if pressed_keys[pygame.K_DOWN]:
            self.vector = (0, self.speed)
        if pressed_keys[pygame.K_LEFT]:
            self.vector = (-self.speed, 0)
        if pressed_keys[pygame.K_RIGHT]:
            self.vector = (self.speed, 0)
        #newpos = self.calcnewpos(self.rect, self.vector)
        #self.rect = newpos
        self.rect.move_ip(*self.vector)
        self.display()

    def calcnewpos(self, rect, vector):
        (angle,z) = vector
        (dx,dy) = (z*math.cos(angle), z*math.sin(angle))
        return rect.move(dx,dy)

    @property
    def sprite(self):
        return self.image

    def display(self):
        self.screen.blit(self.image, self.rect)
