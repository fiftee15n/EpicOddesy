import pygame
class move:
     def move(self,screen_width,screen_height,surface,target,round_over):
        SPEED=10 #hOW QUICKLY THE PLAYERS MOVE AROUND THE SCREEN

        GRAVITY=2
        dx=0    #Movement trace korar jonno with keys  
        dy=0
        self.running=False #by default False thakbe untill the keys for movement not pressed
        self.attack_type=0

        
        #key presses
        key=pygame.key.get_pressed()
        #can only perform other actions if not currently attacking
        if self.attacking==False and self.alive==True and round_over==False:
            #check player1 controls
                if self.player==1:
                    
                    #movement left and right will be done by a and d   WASD for player 1 and arrow keys for player 2
                    if key[pygame.K_a]:
                        dx=-SPEED   #if A is pressed player will go to the left thats why speed will be at negative direction
                        self.running=True
        
                    if key[pygame.K_d]:
                        dx=SPEED #positive or right side
                        self.running=True
        
                    #jumping
                    if key[pygame.K_w] and self.jump==False:
                        self.vel_y=-30
                        self.jump=True
                    #ATTACK
                    if key[pygame.K_r] or key[pygame.K_t]:
                        self.attack(target)
                        #determine which attack type was used
                        if key[pygame.K_r]:
                            self.attack_type=1
                        if key[pygame.K_t]:
                            self.attack_type = 2
                # check player2 controls
                if self.player == 2:
        
                    # movement left and right will be done by a and d   WASD for player 1 and arrow keys for player 2
                    if key[pygame.K_LEFT]:
                        dx = -SPEED  # if A is pressed player will go to the left thats why speed will be at negative direction
                        self.running = True
        
                    if key[pygame.K_RIGHT]:
                        dx = SPEED  # positive or right side
                        self.running = True
        
                    # jumping
                    if key[pygame.K_UP] and self.jump == False:
                        self.vel_y = -30
                        self.jump = True
                    # ATTACK
                    if key[pygame.K_o] or key[pygame.K_p]:
                        self.attack( target)
                        # determine which attack type was used
                        if key[pygame.K_o]:
                            self.attack_type = 1
                        if key[pygame.K_p]:
                            self.attack_type = 2
                          
        #APPLY GRAVITY
        self.vel_y+=GRAVITY
        dy+=self.vel_y
        #ENSOURING THE BOUNDARY
        if self.rect.left+dx<0:
            dx=0-self.rect.left
        if self.rect.right+dx>screen_width:
            dx=screen_width-self.rect.right

        if self.rect.bottom+dy>screen_height-110:
            self.vel_y=0
            self.jump=False
            dy=screen_height-110-self.rect.bottom

        #ensure player face each other
        if target.rect.centerx>self.rect.centerx:
            self.flip=False
        else:
            self.flip=True
            
            
        #applying attack cooldown
        if self.attack_cooldown>0:
            self.attack_cooldown-=1
            

                
        #updating player position according to pressed key
        self.rect.x+=dx
        self.rect.y+=dy
