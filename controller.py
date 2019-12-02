import sys
import pygame
import random
from src import Bullet
from src import Enemy
from src import Ship
from srs import Screen

class Controller:
  def __init__(self, width = 800, height = 600):
      pygame.init()
      self.width = width
      self.height = height
      self.screen = pygame.display.set_mode((self.width, self.height))
      self.background = pygame.Surface(self.screen.get_size()).convert()
      pygame.font.init()
      self.enemy = enemy.Enemy("Alien", x, y, 'assets/enemy.png')
      enemy.x = 
      enemy.y = 
      self.Ship = ship.Ship("Defender", 400, 0, 'assets/Ship.png')
      self.all_sprites = pygame.sprite.Group((self.Ship,)+(self.enemy,))  
      self.state = "Game"
      
      #the game intro screen
  def game_intro(self):
      intro = True
      while intro:
        for i in pygame.event.get():
          if event.type == pygame.QUIT:
            sys.exit()
        gameDisplay.fill(white)
        text = pygame.font.Font('freesansbold.ttf', 115)
        TextSurf, TextRect = ('Galaxy Defender', largeText)
        TextRect.center = ((display_width / 2), (display_height / 2))
        gameDisplay.blit(TextSurf, TextRect)
        pygame.display.update()
