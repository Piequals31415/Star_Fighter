import pygame
import math

class Bullet:

    def __init__(self,master,x,y) -> None:
        self.master = master
        self.__y = y
        self.hit_box = pygame.rect.Rect(x,y,10,10)
        self.color = (255,255,255)
        self.velocity = 10

    def update(self):
        
        self.hit_box.x += self.velocity
        
        y = math.sin(self.hit_box.x/50)

        self.hit_box.y = self.__y + y*20

        self.draw()

    def draw(self):
        pygame.draw.rect(self.master,self.color,self.hit_box)
