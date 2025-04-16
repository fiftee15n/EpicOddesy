import pygame
from move import move
from task import Task
class Fighter(Task, move): #inheritance
    def __init__(self,player,x,y,flip,data,sprite_sheet,animation_steps,sound):
        #-
        self.__name1= "Sword-Man" #Used private variable: Encpasulation 
        self.__name2= "Wizard"
        
        self.player=player
        self.size=data[0]
        self.image_scale=data[1]
        self.offset=data[2]
        self.flip=flip
        self.animation_list=self.load_images(sprite_sheet,animation_steps)
        self.action=0 #0:idle 1:run 2:jump 3:attack1 4:attack2 #5:hit #6:death
        self.frame_index=0
        self.image=self.animation_list[self.action][self.frame_index]
        self.update_time=pygame.time.get_ticks()
        self.rect=pygame.Rect((x,y,80,180)) #rectangle draw korte screen a
        self.vel_y=0
        self.running=False
        self.jump=False
        self.attacking=False
        self.attack_type=0
        
        self.attack_cooldown=0
        self.attack_sound=sound
        self.hit=False
        

        self.health=100
        self.alive=True
        
    # Getter for __name1 : encapsulation
    def get_name1(self):
        return self.__name1

    # Getter for __name2 : encapsulation
    def get_name2(self):
        return self.__name2
    
    def load_images(self,sprite_sheet,animation_steps):
        #extracting images from spritesheet
        animation_list=[]
        for y, animation in enumerate(animation_steps):
            temp_img_list=[]
            for x in range(animation):
                temp_img=sprite_sheet.subsurface(x*self.size,y*self.size,self.size,self.size)

                temp_img_list.append(pygame.transform.scale(temp_img,(self.size*self.image_scale,self.size*self.image_scale)))
            animation_list.append(temp_img_list)

        return animation_list
    
    #define animation updates
    def update(self):
        #check what action the player is performing
        if self.health<=0:
            self.health=0
            self.alive=False
            self.update_action(6)
        elif self.hit==True:
            self.update_action(5)
        elif self.attacking==True:
            if self.attack_type==1:
                self.update_action(3)
            elif self.attack_type==2:
                self.update_action(4)
        elif self.jump==True:
            self.update_action(2)
        elif self.running==True:
            self.update_action(1)
            #action jokon 1 hobe tokon list er modde index 1 er animation gulo load nibe 
        else:
            self.update_action(0)
        animation_cooldown=50
        #update image
        self.image=self.animation_list[self.action][self.frame_index]
        #check if enough time have passed since the last update
        if pygame.time.get_ticks()-self.update_time>animation_cooldown:
            self.frame_index+=1           
            self.update_time=pygame.time.get_ticks()

        #check if the animation has finished
        if self.frame_index>=len(self.animation_list[self.action]):
            #if the player is dead then end  of animation
            if self.alive==False:
                self.frame_index=len(self.animation_list[self.action])-1
            else:
                self.frame_index=0
            #check if the attack was excuted
                if self.action==3 or self.action==4:
                    self.attacking=False
                    self.attack_cooldown=20
                #check if damage was taken
                if self.action==5:
                    self.hit=False
                    #if the player was in the middle of an attack,then the attack is stopped
                    self.attacking=False
                    self.attack_cooldown=20
                
            

    def attack(self,target):
        if self.attack_cooldown==0:
            #execute attack
            self.attacking=True
            self.attack_sound.play()
            #creating attacking rectangtle so that program can determine weather the opponent is under reach or not
            attacking_rect=pygame.Rect(self.rect.centerx-(2*self.rect.width*self.flip),self.rect.y,2*self.rect.width,self.rect.height)
            if attacking_rect.colliderect(target.rect):
                target.health-=10
                target.hit=True

            
            # pygame.draw.rect(surface,(0,255,0),attacking_rect)
#warrior /wizard sheet a sob row te same number of image nai thats why the program will get index out of bound error during running the nested for loop in the load_image function
#this issue will be handled by update_action function
    def update_action(self,new_action):
        #check if the new action is different to the previous one
        if new_action!=self.action:
            self.action=new_action

        #updating the animation settings
            self.frame_index=0
            self.update_time=pygame.time.get_ticks()


        
        
        
        
    def draw(self,surface):
        img=pygame.transform.flip(self.image,self.flip,False)
        # pygame.draw.rect(surface,(255,0,0),self.rect) #red colour er rectangle asbe as an fighter as akon o fighter image load kori nai
        surface.blit(img,(self.rect.x-(self.offset[0]*self.image_scale),self.rect.y-(self.offset[1]*self.image_scale)))