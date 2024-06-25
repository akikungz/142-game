import sys
import pygame
import framework as fw
from variable import Variable

def main(page_setting_run: bool, 
         pygame: pygame, 
         var: Variable, 
         screen: object) -> bool:
    
    # ตัวแปร text ในหน้า setting
    text_screen_size = fw.Text('screen size : ', 30, var.colors.BLACK)
    text_audio = fw.Text('audio : ', 30, var.colors.BLACK)
    text_audio_volume = fw.Text(f'{var.audio_volume} %', 30, var.colors.BLACK)

    # page_setting
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:  # Press ESC to exit
                pygame.quit()
                sys.exit()
        elif var.dropdownScreen.handle_event(event):
            selected_option = var.dropdownScreen.selected_option
            if selected_option == 'Full Screen':
                screen.set_fullscreen_mode()
            else:
                w, h = map(int, selected_option.split('x'))
                screen.set_screen(w, h)
        elif var.btnExit.click(event):
            page_setting_run = False
        elif var.btnReduce_1.click(event):
            var.volume_down(1)
        elif var.btnIncrease_1.click(event):
            var.volume_up(1)
        elif var.btnReduce_10.click(event):
            var.volume_down(10)
        elif var.btnIncrease_10.click(event):
            var.volume_up(10)
    
    # เคลียร์หน้าจอให้เป็นสีขาว
    screen.window.fill(var.colors.WHITE)
    # จัดวางปุ่มและตัวหนังสือ
    text_screen_size.show(screen.window, screen.pack_x(200), screen.pack_y(130))
    text_audio.show(screen.window, screen.pack_x(200), screen.pack_y(160))
    var.btnReduce_1.show(screen.window, screen.width(20), screen.height(20), screen.pack_x(260), screen.pack_y(160))
    var.btnReduce_10.show(screen.window, screen.width(20), screen.height(20), screen.pack_x(290), screen.pack_y(160))
    text_audio_volume.show(screen.window, screen.pack_x(350), screen.pack_y(160) ,center_mode=True)
    var.btnIncrease_1.show(screen.window, screen.width(20), screen.height(20), screen.pack_x(380), screen.pack_y(160))
    var.btnIncrease_10.show(screen.window, screen.width(20), screen.height(20), screen.pack_x(410), screen.pack_y(160))
    var.dropdownScreen.show(screen.window, screen.width(100), screen.height(20), screen.pack_x(300), screen.pack_y(130))
    var.btnExit.show(screen.window, screen.width(100), screen.height(20), screen.pack_x(520), screen.pack_y(10))

    pygame.display.flip()
    var.clock.tick(30)
    return page_setting_run