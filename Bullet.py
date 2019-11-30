import pygame as pg

class Bullet(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([5,10])
        self.image.fill(black)
        self.rect = self.image.get_rect()
        self.speed = 5

    def trajectory(selfself):
        self.rect.y -= self.speed