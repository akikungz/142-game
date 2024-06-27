import sys
import pygame
import framework as fw
from variable import Variable
import randomGacha as gacha

def main(page_gacha_run: bool, 
         pygame: pygame, 
         var: Variable, 
         screen: object) -> bool:
    # ดึงข้อมูลจาก db
    gacha_calculator = gacha.GachaCalculator(var.user_name)
    bannerName = "Rate-Up Debirun"
    # ตัวแปรในการนับจำนวนครั้ง
    var.count_gacha = 142 - int(gacha_calculator.getUserDetail(var.user_name, bannerName)[0]['NumberRoll'])
    # ----
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
            var.audio_gacha_efx.play()
            var.count_gacha += 1
            result = gacha_calculator.multiple_pulls(bannerName, 1)
            Name = result[0]['Name']
            TierName = result[0]['TierName']
            var.result = f'คุณสุ่มได้ {Name} ระดับ {TierName}'
    
    # text
    text_gacha_result = fw.Text(f'{var.result}', 30, var.colors.BLACK)
    text_gacha_count = fw.Text(f'เหลืออีก {var.count_gacha} ครั้งจะการันตี', 30, var.colors.BLACK)
    text_gem = fw.Text(f'gem : {format(gacha_calculator.get_user_gem(var.user_name), ",")}', 30, var.colors.BLACK)
    
    screen.window.fill(var.colors.WHITE)
    text_gem.show(screen.window, screen.pack_x(500), screen.pack_y(10) ,center_mode=True)
    text_gacha_count.show(screen.window, screen.pack_x(320), screen.pack_y(135) ,center_mode=True)
    text_gacha_result.show(screen.window, screen.pack_x(320), screen.pack_y(165) ,center_mode=True)
    var.btnRandom.show(screen.window, screen.width(160), screen.height(20), screen.pack_x(240), screen.pack_y(210))
    var.btnExit.show(screen.window, screen.width(160), screen.height(20), screen.pack_x(240), screen.pack_y(240))

    pygame.display.flip()
    var.clock.tick(30)
    return page_gacha_run
