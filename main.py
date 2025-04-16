import pygame
from pygame import mixer
from DrawBackground import drawBackground
from DrawHealthBar import drawHealthBar
from DrawText import drawText
from fighter import Fighter
mixer.init()
pygame.init()

#creating game window
SCREEN_WIDTH=1000
SCREEN_HEIGHT=600
screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Epic Odessey")


#set frame rate
clock=pygame.time.Clock()
FPS=60

# #defining colours
YELLOW=(255,255,0)
RED=(255,0,0)
WHITE=(255,255,255)

#defining game variables
intro_count=3
last_count_update=pygame.time.get_ticks()
score=[0,0] #player scores[p1,p2]
round_over=False
ROUND_OVER_COOLDOWN=2000

#define fighter variables
WARRIOR_SIZE=162
#screen er satae warrior and wizard er size adjust korar jonno scale use korte hobe
WARRIOR_SCALE=4
WARRIOE_OFFSET=[72,56]

WARRIOR_DATA=[WARRIOR_SIZE,WARRIOR_SCALE,WARRIOE_OFFSET]

WIZARD_SIZE=250
WIZARD_SCALE=3
WIZARD_OFFSET=[112,107]
WIZARD_DATA=[WIZARD_SIZE,WIZARD_SCALE,WIZARD_OFFSET]

#loading music
pygame.mixer.music.load("E:\EpicOddesy\assets\audio\music.mp3")
pygame.mixer.music.set_volume(0.9)
pygame.mixer.music.play(-1,0.0,5000)

sword_fx=pygame.mixer.Sound("E:\EpicOddesy\assets\audio\sword.wav")
sword_fx.set_volume(0.5)

magic_fx=pygame.mixer.Sound("E:\EpicOddesy\assets\audio\magic.wav")
magic_fx.set_volume(0.75)




#load background image

bg_image=pygame.image.load("E:\EpicOddesy\assets\images\background\background.jpg").convert_alpha()


#load spritesheets
warrior_sheet=pygame.image.load("E:\EpicOddesy\assets\images\warrior\warrior.png").convert_alpha()
wizard_sheet=pygame.image.load("E:\EpicOddesy\assets\images\wizard\Sprits\wizard.png").convert_alpha()

victory_img=pygame.image.load("E:\EpicOddesy\assets\images\icons\victory.png").convert_alpha()

#define number of steps in each animation
WARRIOR_ANIMATION_STEPS=[10,8,1,7,7,3,7]
WIZARD_ANIMATION_STEPS=[8,8,1,8,8,3,7]

#defining fonts
count_font=pygame.font.Font("E:\EpicOddesy\assets\fonts\turok.ttf",80)
score_font=pygame.font.Font("E:\EpicOddesy\assets\fonts\turok.ttf",30)

#create two instances of fighters
fighter_1=Fighter(1,200,310,False,WARRIOR_DATA,warrior_sheet,WARRIOR_ANIMATION_STEPS,sword_fx) #This is for fighters location in the screen left side a draw hobe eta
fighter_2=Fighter(2,700,310,True,WIZARD_DATA,wizard_sheet,WIZARD_ANIMATION_STEPS,magic_fx) #eta right side a tai x axist a 700 mane total width 1000-700
#game loop
run=True
background = drawBackground()
draw_test = drawText()
health_bar = drawHealthBar()
while run:
  clock.tick(FPS)
  #draw background
  background.draw(screen,bg_image,SCREEN_WIDTH, SCREEN_HEIGHT)
  #SHOW PLAYER HELATH
  health_bar.draw(screen, fighter_1.health, 20 , 20)
  health_bar.draw(screen,fighter_2.health,580,20)
  draw_test.draw(screen,fighter_1.get_name1()+": "+str(score[0]),score_font,RED,20,60)
  draw_test.draw(screen,fighter_2.get_name2()+": "+str(score[1]),score_font,RED,580,60)
  
  
  #By calling the same method "draw", we are drawing different thing. It is a example of Ploymorphism
  
  #updating countdown
  if intro_count<=0:
    # move fighter
    fighter_1.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter_2,round_over)
    fighter_2.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter_1,round_over)
  else:
    #ddisplay count timer
    draw_test.draw(screen,str(intro_count),count_font,RED,SCREEN_WIDTH/2,SCREEN_HEIGHT/3)
    #update count timer
    if(pygame.time.get_ticks()-last_count_update)>=1000:
      intro_count-=1
      last_count_update=pygame.time.get_ticks()

  #update fighters
  fighter_1.update()
  fighter_2.update()


  #draw fighters
  fighter_1.draw(screen)
  fighter_2.draw(screen)
  #CHECK FOR PLAYER DEFEAT
  if round_over==False:
    if fighter_1.alive==False:
      score[1]+=1
      round_over=True
      round_over_time=pygame.time.get_ticks()

    elif fighter_2.alive==False:
      score[0]+=1
      round_over=True
      round_over_time=pygame.time.get_ticks()

  else:
      #display victory image
      screen.blit(victory_img,(360,150))
      if pygame.time.get_ticks()-round_over_time>ROUND_OVER_COOLDOWN:
        round_over=False
        intro_count=3
          #resetting the game again
        fighter_1 = Fighter(1, 200, 310, False, WARRIOR_DATA, warrior_sheet, WARRIOR_ANIMATION_STEPS,sword_fx)
        fighter_2 = Fighter(2, 700, 310, True, WIZARD_DATA, wizard_sheet, WIZARD_ANIMATION_STEPS,magic_fx)


        #event
  for event in pygame.event.get():
    if event.type==pygame.QUIT:
      run=False



  #update display
  pygame.display.update()



#exit pygame
pygame.quit()
