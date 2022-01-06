import pygame.image
from settings import alien_image
import random


class Aliens(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(alien_image[random.randint(0, 4)])
