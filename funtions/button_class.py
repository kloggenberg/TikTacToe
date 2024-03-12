import pygame

# Define a Button class
class Button:
    def __init__(self, x, y, width, height,name):
        self.rect = pygame.Rect(x, y, width, height)
        self.name = name
        self.state = False
        self.text = ""
        
        
    def change_state(self):
        self.state = True

    def draw_rect(self,window,mouse_x,mouse_y):
        if self.state:
            pygame.draw.rect(window, (0,0,255), self.rect,0,10)
        elif self.rect.collidepoint(mouse_x,mouse_y):
            pygame.draw.rect(window, (255,0,0), self.rect,0,10)
        else:
            pygame.draw.rect(window, (0,255,0), self.rect,0,10)

    def draw_unclicked(self,window):
        pygame.draw.rect(window, (0,255,0), self.rect,0,10)
       
        
    def draw_clicked(self,window):
        pygame.draw.rect(window, self.color, self.rect)
        font = pygame.font.Font(None, 36)
        text = font.render(self.text, True, (0,0,0))
        text_rect = text.get_rect(center=self.rect.center)
        window.blit(text, text_rect)

        
    def check_click(self,mouse_x,mouse_y):
        if self.rect.collidepoint(mouse_x,mouse_y):
            self.state = True
            