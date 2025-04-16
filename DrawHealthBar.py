import pygame
from draw import draw

class drawHealthBar(draw):  #inheritance
    def __init__(self):
        self.YELLOW=(255,255,0)
        self.RED=(255,0,0)
        self.WHITE=(255,255,255)
    def draw(self,screen,health,x,y):
        ratio=health/100
        pygame.draw.rect(screen,self.WHITE,(x-2,y-2,404,34))
        pygame.draw.rect(screen,self.RED,(x,y,400,30))
        pygame.draw.rect(screen,self.YELLOW,(x,y,400*ratio,30))