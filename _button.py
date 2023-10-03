import pygame
class Button:
    def __init__(self, window,txt, pos,dim=None):
        self.window=window
        self.text = txt
        self.pos = pos
        self.dim=dim
        if(dim==None):self.dim=(150,40)
        self.button = pygame.rect.Rect((self.pos[0], self.pos[1]), self.dim)

    def draw(self):
        pygame.draw.rect(self.window, 'light yellow', self.button, 0, 5)
        pygame.draw.rect(self.window, 'light yellow', [self.pos[0], self.pos[1], self.dim[0],self.dim[1]], 5, 5)
        font=myfont = pygame.font.SysFont("monospace", 14)
        text2=font.render(self.text,True,'green')

        self.window.blit(text2, (self.pos[0] + 12, self.pos[1] + 12))

    def check_clicked(self):
        if self.button.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            return True
        else:
            return False
