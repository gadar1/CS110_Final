import pygame
import random
import math

class Enemy(pygame.sprite.Sprite):
    def __init__(self, name, x, y, img_file):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(img_file).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.direction = "right"
        self.speed = 5
        self.closer = False

    def update(self):
        if self.direction = "right" and self.rect.x < 750:
            self.rect.x += self.speed

        elif self.direction = "right" and self.rect.x >= 750:
            self.rect.x = 750
            self.closer = True
            self.direction = "left"

        elif self.direction = "left" and self.rect.x > 50:
            self.rect.x -= self.speed

        elif self.direction = "left" and self.rect.x <= 50:
            self.rext.x = 50
            self.closer = True
            self.direction = "right"

    def movingCloser(self):
        if self.closer = True:
            self.rect.y += 20
            self.closer = False