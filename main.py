import sys
import pygame
import random
import get_image
import get_audio
import framework as fw


# Initialize Pygame
pygame.init()


# Colors
WHITE = (255, 255, 255)
GREY = (198, 198, 198)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
DARK_BLUE = (0, 0, 139)


class Variable():
    def __init__(self):
        self.clock = pygame.time.Clock()
        # ตัวแปรข้อความ
        self.text_normal = fw.Text('', 30, BLACK)
        # ตัวแปรของปุ่ม
        self.btnPlay = fw.Button('play', 20, WHITE, DARK_BLUE)
        self.btnSetting = fw.Button('setting', 20, WHITE, DARK_BLUE)
        self.btnExit = fw.Button('exit', 20, WHITE, RED)
        self.btnPrevious = fw.Button('<', 20, WHITE, DARK_BLUE)
        self.btnNext = fw.Button('>', 20, WHITE, DARK_BLUE)
        # set ค่าเริ่มต้น
        self.set_start()

    def set_start(self):
        pass


def set_screen_size(screen, screen_size, key_btn):
    if screen_size[key_btn] == 'Full Screen':
        screen.set_fullscreen_mode()
    else:
        w = int(screen_size[key_btn].split('x')[0])
        h = int(screen_size[key_btn].split('x')[1])
        screen.set_screen(w, h)

# global variable
screen = fw.Screen(640, 360)
var = Variable()


while True:
    # ตัวแปรสำหรับเข้าแต่ละหน้า
    page_play = False
    page_setting = False
    # ตัวแปรอีเว้น
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:  # Press ESC to exit
                pygame.quit()
                sys.exit()
        elif var.btnPlay.click(event):
            page_play = True
            var.set_start()
        elif var.btnSetting.click(event):
            page_setting = True
        elif var.btnExit.click(event):
            pygame.quit()
            sys.exit()
    
    screen.window.fill(WHITE)
    var.btnPlay.show(screen.window, screen.width(160), screen.height(20), screen.pack_x(240), screen.pack_y(150))
    var.btnSetting.show(screen.window, screen.width(160), screen.height(20), screen.pack_x(240), screen.pack_y(180))
    var.btnExit.show(screen.window, screen.width(160), screen.height(20), screen.pack_x(240), screen.pack_y(210))
    pygame.display.flip()
    var.clock.tick(30)

    key_btn = 0
    while page_setting:
        screen_size = ['Full Screen', '1920x1080', '1280x720', '854x480', '640x360']
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
                page_setting = False
            elif var.btnPrevious.click(event):
                key_btn -= 1
                if key_btn < 0:
                    key_btn = len(screen_size) - 1
                set_screen_size(screen, screen_size, key_btn)
            elif var.btnNext.click(event):
                key_btn += 1
                if key_btn > len(screen_size) - 1:
                    key_btn = 0
                set_screen_size(screen, screen_size, key_btn)
        
        screen.window.fill(WHITE)
        var.text_normal.show(screen.window, screen.pack_x(200), screen.pack_y(135), 'screen size')
        var.text_normal.show(screen.window, screen.pack_x(315), screen.pack_y(135), f'{screen_size[key_btn]}', center_mode=True)
        var.btnPrevious.show(screen.window, screen.width(20), screen.height(20), screen.pack_x(260), screen.pack_y(130))
        var.btnNext.show(screen.window, screen.width(20), screen.height(20), screen.pack_x(350), screen.pack_y(130))
        var.btnExit.show(screen.window, screen.width(100), screen.height(20), screen.pack_x(520), screen.pack_y(10))

        pygame.display.flip()
        var.clock.tick(30)
