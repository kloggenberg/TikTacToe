import pygame

# Define a Button class
class Button:
    def __init__(self, x, y, width, height, color, text):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.text = text


    def draw_unclicked(self,window):
        pygame.draw.rect(window, self.color, self.rect)
       
        
    def draw_clicked(self,window):
        pygame.draw.rect(window, self.color, self.rect)
        font = pygame.font.Font(None, 36)
        text = font.render(self.text, True, (0,0,0))
        text_rect = text.get_rect(center=self.rect.center)
        window.blit(text, text_rect)
        
    def draw_hover(self,window,mos_x,mos_y):
        pass