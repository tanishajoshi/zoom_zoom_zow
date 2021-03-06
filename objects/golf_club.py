import os
import math

import pygame as pg

from resources import Spritesheet


class GolfClub(pg.sprite.Sprite):

    def __init__(self, screen):
        """Initialize the golf club.

        :param screen: The pygame display
        """
        super(GolfClub, self).__init__()
        self.screen = screen
        self.size = 100, 100
        # Set the radius for detecting collisions
        self.radius = 50

        # Set the sprite images
        self.images, self.image_indices = self.get_images()
        self.image_index = 0
        self.set_image()

        # Set the rectangle, or the box where it is drawn
        self.original_bottom_loc = self.screen.get_size()[1] - 60
        self.original_right_loc = self.screen.get_size()[0] / 2 - 5
        self.vector = [0, 0]
        self.power = 30
        self.set_resting()

    def get_images(self):
        """Get all images defined by the spritesheet and return them.

        :return: A list pygame.Surface and index dict
        :rtype: list of pygame.Surface and dict of int: int
        """
        ss = Spritesheet(
            os.path.join(os.getcwd(), 'resources', 'golf_club_sheet.png')
        )
        strip = ss.load_strip((0,0,200,200), 4)
        scaled_strip = []
        for sprite in strip:
            scaled_strip.append(
                pg.transform.scale(sprite, self.size)
            )
        return scaled_strip, {
                0: self.set_resting,
                1: self.set_mid_swing,
                2: self.set_full_swing,
                3: self.set_mid_swing,
                4: self.set_resting,
                5: self.set_followthru
            }

    def set_image(self, image_index=0):
        if image_index is not None and \
           image_index in range(0, len(self.image_indices)):
            self.surf = self.images[image_index]
        if not hasattr(self, 'rect'):
            self.rect = self.surf.get_rect()

    def set_resting(self):
        self.set_image(image_index=0)
        self.rect.right = self.original_right_loc
        self.rect.bottom = self.original_bottom_loc

    def set_mid_swing(self):
        self.set_image(image_index=1)
        self.rect.right = self.original_right_loc - 100
        self.rect.bottom = self.original_bottom_loc

    def set_full_swing(self):
        self.set_image(image_index=2)
        self.rect.right = self.original_right_loc - 110
        self.rect.bottom = self.original_bottom_loc - 120

    def set_followthru(self):
        self.set_image(image_index=3)
        self.rect.right = self.original_right_loc - 110
        self.rect.bottom = self.original_bottom_loc - 120

    def update(self):
        self.display()

    def calcnewpos(self, rect, vector):
        (angle,z) = vector
        (dx,dy) = (z*math.cos(angle), z*math.sin(angle))
        return rect.move(dx,dy)

    @property
    def image(self):
        return self.surf

    def display(self):
        self.screen.blit(self.surf, self.rect)
