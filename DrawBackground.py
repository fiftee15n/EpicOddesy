import pygame
from draw import draw

class drawBackground(draw):  #inheritance
    def draw(self,screen,bg_image,SCREEN_WIDTH, SCREEN_HEIGHT):
        scaled_bg = pygame.transform.scale(bg_image,(SCREEN_WIDTH, SCREEN_HEIGHT))
        #my image was bigger than the screen thats why used transform.scale to scale the image
        screen.blit(scaled_bg,(0,0))