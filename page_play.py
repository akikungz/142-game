import sys
import pygame
import framework as fw
from variable import Variable

def main(page_play_run: bool, 
         pygame: pygame, 
         var: Variable, 
         screen: fw.Screen) -> bool:
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
            page_play_run = False

    screen.window.fill(var.colors.WHITE)
    var.btnBack.show(screen.window, screen.width(20), screen.height(20), screen.pack_x(10), screen.pack_y(10))

    pygame.display.flip()
    var.clock.tick(30)
    return page_play_run