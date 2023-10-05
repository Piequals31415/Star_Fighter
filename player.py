import pygame
from bullet import Bullet

class Player:

    def __init__(self,master:pygame.Surface) -> None:
        self.master = master
        self.hit_box = pygame.rect.Rect(50,50,50,50)
        self.color = [255,0,0]

        self.cooldown = True
        self.cooldown_timer = 0

        self.shoot_pause = 15

        self.velocity = 5

    def update(self,enemy_list,bullet_list):
        
        keys = pygame.key.get_pressed()

        
        if keys[pygame.K_w]:
            self.hit_box.y -=1 * self.velocity
        if keys[pygame.K_s]:
            self.hit_box.y +=1 * self.velocity
        if keys[pygame.K_a]:
            self.hit_box.x -=1 * self.velocity
        if keys[pygame.K_d]:
            self.hit_box.x +=1 * self.velocity
        if keys[pygame.K_SPACE]:
            bullet_list = self.shoot(bullet_list)


        self.if_hit(enemy_list)
        
        self.draw()

        return bullet_list

    def if_hit(self,enemy_list):
        
        self.color = [255,0,0]

        for enemy in enemy_list:
            if self.hit_box.colliderect(enemy.hit_box):
                self.color = [0,0,255]

        
    def shoot(self,bullet_list):

        if self.cooldown:

            if len(bullet_list) <= 5:

                bullet_list.append(Bullet(self.master,self.hit_box.x+50,self.hit_box.y+25))
                self.cooldown = False
        
        else:
            if self.cooldown_timer <= self.shoot_pause:
                self.cooldown_timer += 1

            else:
                self.cooldown_timer = 0
                self.cooldown = True
        
        return bullet_list



    def draw(self):
        pygame.draw.rect(self.master,self.color,self.hit_box,5)
