import sys
import pygame
import random
import framework as fw

def main(page_gacha_run: bool, 
         pygame: pygame, 
         var: object, 
         screen: object) -> bool:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:  # Press ESC to exit
                pygame.quit()
                sys.exit()
        elif var.btnExit.click(event):
            page_gacha_run = False
        elif var.btnRandom.click(event):
            var.audio_gacha.play()
            var.count_gacha += 1
            result = gacha_summon()
            var.result = f'You summon an {result}-rank character.'
    
    # text
    text_gacha_result = fw.Text(f'{var.result}', 30, var.colors.BLACK)
    text_gacha_count = fw.Text(f'count : {var.count_gacha}', 30, var.colors.BLACK)
    
    screen.window.fill(var.colors.WHITE)
    text_gacha_count.show(screen.window, screen.pack_x(320), screen.pack_y(135) ,center_mode=True)
    text_gacha_result.show(screen.window, screen.pack_x(320), screen.pack_y(165) ,center_mode=True)
    var.btnRandom.show(screen.window, screen.width(160), screen.height(20), screen.pack_x(240), screen.pack_y(210))
    var.btnExit.show(screen.window, screen.width(160), screen.height(20), screen.pack_x(240), screen.pack_y(240))

    pygame.display.flip()
    var.clock.tick(30)
    return page_gacha_run


def gacha_summon():
    probabilities = {
        "UR": 1.42,
        "SSR": 18.58,
        "SR": 30,
        "R": 50
    }

    # Generate a random number between 0 and 100
    roll = random.random() * 100

    # Determine the rarity based on the roll
    cumulative_probability = 0
    for rarity, probability in probabilities.items():
        cumulative_probability += probability
        if roll <= cumulative_probability:
            return rarity
