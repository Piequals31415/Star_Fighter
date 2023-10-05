from player import Player
from enemy import Enemy
import pygame

class Main:

    def __init__(self,master:pygame.Surface) -> None:
        self.master = master
        self.player = Player(master)
        self.enemy_list = [Enemy(master,600,300),Enemy(master,600,100),Enemy(master,600,500)]
        self.bullet_list = []

    def update(self,event):
        


        self.update_enemy()
        self.update_bullets()
        self.bullet_list = self.player.update(self.enemy_list,self.bullet_list)


    def update_enemy(self):
        for enemy in self.enemy_list:
            enemy.update()

    def update_bullets(self):
        for index, bullet in enumerate(self.bullet_list):
            if bullet.hit_box.x >= 800:
                del self.bullet_list[index]

            for index_enemy,enemy in enumerate(self.enemy_list):
                if enemy.hit_box.colliderect(bullet.hit_box):
                    del self.bullet_list[index]
                    del self.enemy_list[index_enemy]

            bullet.update()