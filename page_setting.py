import sys
import pygame

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
        # elif var.btnPrevious.click(event):
        #     key_btn -= 1
        #     if key_btn < 0:
        #         key_btn = len(screen_size) - 1
        #     set_screen_size(screen, screen_size, key_btn)
        # elif var.btnNext.click(event):
        #     key_btn += 1
        #     if key_btn > len(screen_size) - 1:
        #         key_btn = 0
        #     set_screen_size(screen, screen_size, key_btn)

        if var.dropdownScreen.handle_event(event):
            selected_option = var.dropdownScreen.selected_option
            if selected_option == 'Full Screen':
                screen.set_fullscreen_mode()
            else:
                w, h = map(int, selected_option.split('x'))
                screen.set_screen(w, h)
    
    screen.window.fill(var.colors.WHITE)
    var.text_normal.show(screen.window, screen.pack_x(200), screen.pack_y(135), 'screen size')
    var.dropdownScreen.show(screen.window, screen.width(100), screen.height(20), screen.pack_x(300), screen.pack_y(130))
    # var.btnPrevious.show(screen.window, screen.width(20), screen.height(20), screen.pack_x(260), screen.pack_y(130))
    # var.btnNext.show(screen.window, screen.width(20), screen.height(20), screen.pack_x(350), screen.pack_y(130))
    var.btnExit.show(screen.window, screen.width(100), screen.height(20), screen.pack_x(520), screen.pack_y(10))

    pygame.display.flip()
    var.clock.tick(30)
    return page_setting_run