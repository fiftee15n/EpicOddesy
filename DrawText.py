from draw import draw

class drawText(draw):  #inheritance
    def draw(self,screen,text,font,text_col,x,y):
        # screen = self.screen
        # text = self.text
        # font = self.font
        # text_col = self.text_col
        # x = self.x
        # y = self.y
        img=font.render(text,True,text_col)
        screen.blit(img,(x,y))