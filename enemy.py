import pygame

class Enemy:

    def __init__(self,master,x,y) -> None:
        self.master = master
        self.hit_box = pygame.rect.Rect(x,y,50,50)

    def update(self):
        
        self.draw()        

    def draw(self):
        pygame.draw.rect(self.master,(0,255,0),self.hit_box,5)
