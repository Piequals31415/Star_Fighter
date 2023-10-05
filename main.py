import pygame
from manager import Main

pygame.init()
window_width = 800
window_height = 600
background_color = (0, 0, 0)  

master = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Mein Pygame-Spiel")

clock = pygame.time.Clock()

running = True

game = Main(master)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    master.fill(background_color)

    game.update(event)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()




