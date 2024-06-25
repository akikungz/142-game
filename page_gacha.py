import sys
import pygame
import random
import framework as fw
from variable import Variable

def main(page_gacha_run: bool, 
         pygame: pygame, 
         var: Variable, 
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
        "SSR": 142,   # ความน่าจะเป็น 1.42%
        "SR": 1858,   # ความน่าจะเป็น 18.58%
        "R": 3000,    # ความน่าจะเป็น 30%
        "N": 5000    # ความน่าจะเป็น 50%
    }

    # สร้างตัวเลขสุ่มระหว่าง 1 ถึง 10,000
    # ตัวเลขนี้จะใช้เป็นตัวตัดสินว่าเราจะได้ไอเทมระดับใด
    roll = random.randint(1, 10_000)

    # ตรวจสอบว่าตัวเลขสุ่มที่ได้อยู่ในช่วงความน่าจะเป็นของระดับใด
    cumulative_probability = 0  # ตัวแปรเก็บความน่าจะเป็นสะสม
    for rarity, probability in probabilities.items():
        cumulative_probability += probability 
        # ถ้าตัวเลขสุ่มน้อยกว่าหรือเท่ากับความน่าจะเป็นสะสม
        # แสดงว่าเราสุ่มได้ไอเทมระดับนั้น
        if roll <= cumulative_probability:
            return rarity
