import sys
import pygame
import framework as fw

def main(page_setting_run: bool, 
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
            page_setting_run = False
        elif var.btnPrevious.click(event):
            var.volume_down()
        elif var.btnNext.click(event):
            var.volume_up()

        if var.dropdownScreen.handle_event(event):
            selected_option = var.dropdownScreen.selected_option
            if selected_option == 'Full Screen':
                screen.set_fullscreen_mode()
            else:
                w, h = map(int, selected_option.split('x'))
                screen.set_screen(w, h)
    
    # text
    text_screen_size = fw.Text('screen size : ', 30, var.colors.BLACK)
    text_audio = fw.Text('audio : ', 30, var.colors.BLACK)
    text_audio_volume = fw.Text(f'{int(var.audio_volume*10)*10} %', 30, var.colors.BLACK)
    
    screen.window.fill(var.colors.WHITE)
    text_screen_size.show(screen.window, screen.pack_x(200), screen.pack_y(135))
    text_audio.show(screen.window, screen.pack_x(200), screen.pack_y(165))
    var.btnPrevious.show(screen.window, screen.width(20), screen.height(20), screen.pack_x(260), screen.pack_y(160))
    text_audio_volume.show(screen.window, screen.pack_x(320), screen.pack_y(165) ,center_mode=True)
    var.btnNext.show(screen.window, screen.width(20), screen.height(20), screen.pack_x(350), screen.pack_y(160))
    var.dropdownScreen.show(screen.window, screen.width(100), screen.height(20), screen.pack_x(300), screen.pack_y(130))
    var.btnExit.show(screen.window, screen.width(100), screen.height(20), screen.pack_x(520), screen.pack_y(10))

    pygame.display.flip()
    var.clock.tick(30)
    return page_setting_run