import sys
import pygame
import random
import colors
import get_image
import get_audio
import page_setting
import framework as fw


# Initialize Pygame
pygame.init()


class Variable():
    def __init__(self):
        self.clock = pygame.time.Clock()
        # Colors
        self.colors = colors.Colors()
        # ตัวแปรของเพลง
        self.audio_volume = 0.1
        self.audio_background_music = pygame.mixer.Sound(get_audio.debirun_sound)
        self.audio_background_music.set_volume(self.audio_volume)
        self.audio_background_music.play(-1)
        # ตัวแปรข้อความ
        self.text_name_game = fw.Text('142 Game', 50, self.colors.BLACK)
        self.text_normal = fw.Text('', 30, self.colors.BLACK)
        # ตัวแปรของปุ่ม
        self.btnPlay = fw.Button('play', 20, self.colors.WHITE, self.colors.DARK_BLUE)
        self.btnGacha = fw.Button('gacha', 20, self.colors.WHITE, self.colors.DARK_BLUE)
        self.btnSetting = fw.Button('setting', 20, self.colors.WHITE, self.colors.DARK_BLUE)
        self.btnExit = fw.Button('exit', 20, self.colors.WHITE, self.colors.RED)
        self.btnPrevious = fw.Button('<', 20, self.colors.WHITE, self.colors.DARK_BLUE)
        self.btnNext = fw.Button('>', 20, self.colors.WHITE, self.colors.DARK_BLUE)
        # ตัวแปรของ dropdown
        self.dropdownScreen = fw.Dropdown(['Full Screen', '1920x1080', '1280x720', '854x480'], 24, self.colors.WHITE, self.colors.DARK_BLUE)
        # set ค่าเริ่มต้น
        self.set_start()

    def set_start(self):
        pass

    def set_audio_volume(self):
        self.audio_background_music.set_volume(self.audio_volume)

    def volume_up(self):
        self.audio_volume += 0.1
        if self.audio_volume > 1.0:
            self.audio_volume = 1.0
        self.set_audio_volume()

    def volume_down(self):
        self.audio_volume -= 0.1
        if self.audio_volume < 0.0:
            self.audio_volume = 0.0
        self.set_audio_volume()


# global variable
screen = fw.Screen(640, 360)
var = Variable()


while True:
    # ตัวแปรสำหรับเข้าแต่ละหน้า
    page_play_run = False
    page_gacha_run = False
    page_setting_run = False
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
            page_play_run = True
            var.set_start()
        elif var.btnGacha.click(event):
            page_gacha_run = True
        elif var.btnSetting.click(event):
            page_setting_run = True
        elif var.btnExit.click(event):
            pygame.quit()
            sys.exit()
    
    screen.window.fill(var.colors.WHITE)
    var.text_name_game.show(screen.window, screen.pack_x(320), screen.pack_y(120), center_mode=True)
    var.text_normal.show(screen.window, screen.pack_x(600), screen.pack_y(340), 'v.0.0.5', center_mode=True)
    var.btnPlay.show(screen.window, screen.width(160), screen.height(20), screen.pack_x(240), screen.pack_y(150))
    var.btnGacha.show(screen.window, screen.width(160), screen.height(20), screen.pack_x(240), screen.pack_y(180))
    var.btnSetting.show(screen.window, screen.width(160), screen.height(20), screen.pack_x(240), screen.pack_y(210))
    var.btnExit.show(screen.window, screen.width(160), screen.height(20), screen.pack_x(240), screen.pack_y(240))
    pygame.display.flip()
    var.clock.tick(30)

    while page_setting_run:
        page_setting_run = page_setting.main(page_setting_run, pygame, var, screen)
