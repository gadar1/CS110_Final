import pygame as pg

class Ship(pg.sprite.Sprite):

    def __init__(self,x,y,img_file):
        pg.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(img_file).convert_alpha()
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.speed = 5
        self.health = 100

    def move_left(self):
        self.rect.x -= self.speed

    def move_right(self):
        self.rect.x += self.speed
