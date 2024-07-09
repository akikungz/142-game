import sys
import math
import pygame
import framework as fw
from variable import Variable
import character
import random

# ฟังก์ชันหลักของเกม
def main(pygame: pygame, 
         var: Variable, 
         screen: fw.Screen):
    
    var.set_start()
    player = character.Player(screen, 60, 80)
    var.all_sprites.add(player)

    running = True
    while running:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # Press ESC to exit
                    pygame.quit()
                    sys.exit()
            elif var.btnBack.click(event):
                running = False

        screen.window.fill(var.colors.WHITE)
        
        player.update(var, events)
        player.magic_sprites.update()
        var.all_sprites.draw(screen.window)

        var.btnBack.show(screen.window, screen.width(20), screen.height(20), screen.pack_x(10), screen.pack_y(10))

        pygame.display.flip()
        var.clock.tick(30)