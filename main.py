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
        # ตัวแปรของปุ่ม
        self.btnPlay = fw.Button('play', 20, WHITE, DARK_BLUE)
        self.btnSetting = fw.Button('setting', 20, WHITE, DARK_BLUE)
        self.btnExit = fw.Button('exit', 20, WHITE, RED)
        self.btnFullscreen = fw.Button('Fullscreen', 20, WHITE, DARK_BLUE)
        self.btn1080P = fw.Button('1920x1080', 20, WHITE, DARK_BLUE)
        self.btn720P = fw.Button('1280x720', 20, WHITE, DARK_BLUE)
        self.btn480P = fw.Button('854x480', 20, WHITE, DARK_BLUE)
        self.btn360P = fw.Button('640x360', 20, WHITE, DARK_BLUE)
        # set ค่าเริ่มต้น
        self.set_start()

    def set_start(self):
        pass


# global variable
screen = fw.Screen(640, 360)
var = Variable()


while True:
    # ตัวแปรสำหรับเข้าแต่ละหน้า
    page_play = False
    page_setting = False
    # ตัวแปลอีเว้น
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

    while page_setting:
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
            elif var.btnFullscreen.click(event):
                screen.set_fullscreen_mode()
            elif var.btn1080P.click(event):
                screen.set_screen(1920, 1080)
            elif var.btn720P.click(event):
                screen.set_screen(1280, 720)
            elif var.btn480P.click(event):
                screen.set_screen(854, 480)
            elif var.btn360P.click(event):
                screen.set_screen(640, 360)

        screen.window.fill(WHITE)
        var.btnFullscreen.show(screen.window, screen.width(160), screen.height(20), screen.pack_x(240), screen.pack_y(100))
        var.btn1080P.show(screen.window, screen.width(160), screen.height(20), screen.pack_x(240), screen.pack_y(130))
        var.btn720P.show(screen.window, screen.width(160), screen.height(20), screen.pack_x(240), screen.pack_y(160))
        var.btn480P.show(screen.window, screen.width(160), screen.height(20), screen.pack_x(240), screen.pack_y(190))
        var.btn360P.show(screen.window, screen.width(160), screen.height(20), screen.pack_x(240), screen.pack_y(220))
        var.btnExit.show(screen.window, screen.width(100), screen.height(20), screen.pack_x(520), screen.pack_y(10))

        pygame.display.flip()
        var.clock.tick(30)
