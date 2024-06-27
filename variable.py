import pygame
import colors
import get_image
import get_audio
import framework as fw

class Variable():
    def __init__(self, pygame: pygame):
        # ตัวแปรใช้ทั่วไป
        self.user_name = "admin"
        self.clock = pygame.time.Clock()
        # Colors
        self.colors = colors.Colors()
        # ตัวแปรของเพลง
        self.audio_volume_music = 10
        self.audio_volume_efx = 10
        self.audio_background_music = pygame.mixer.Sound(get_audio.debirun_sound)
        self.audio_gacha_efx = pygame.mixer.Sound(get_audio.gacha_sound)
        self.set_audio_volume()
        self.audio_background_music.play(-1)
        # ตัวแปรของปุ่ม
        self.btnExit = fw.Button('ออก', 20, self.colors.WHITE, self.colors.RED)
        
        self.init_page_main_variables()
        self.init_page_setting_variables()
        self.init_page_gacha_variables()

        # set ค่าเริ่มต้น
        self.set_start()

    def init_page_main_variables(self):
        # ตัวแปรหน้า page_main
        # ตัวแปรข้อความ
        self.text_name_game = fw.Text('142 Game', 50, self.colors.BLACK)
        self.text_version = fw.Text('', 30, self.colors.BLACK)
        # ตัวแปรของปุ่ม
        self.btnPlay = fw.ImageButton('', 0, self.colors.WHITE, get_image.btnPlay)
        self.btnGacha = fw.ImageButton('', 0, self.colors.WHITE, get_image.btnGacha)
        self.btnSetting = fw.ImageButton('', 0, self.colors.WHITE, get_image.btnSetting)
        self.btnExitImg = fw.ImageButton('', 0, self.colors.WHITE, get_image.btnExitImg)
        self.btnPrevious = fw.Button('<', 20, self.colors.WHITE, self.colors.DARK_BLUE)
        self.btnNext = fw.Button('>', 20, self.colors.WHITE, self.colors.DARK_BLUE)

    def init_page_setting_variables(self):
        # ตัวแปรหน้า page_setting
        # ตัวแปรของปุ่ม
        self.btnReduce_1_music = fw.Button('-1', 20, self.colors.WHITE, self.colors.DARK_BLUE)
        self.btnIncrease_1_music = fw.Button('+1', 20, self.colors.WHITE, self.colors.DARK_BLUE)
        self.btnReduce_10_music = fw.Button('-10', 20, self.colors.WHITE, self.colors.DARK_BLUE)
        self.btnIncrease_10_music = fw.Button('+10', 20, self.colors.WHITE, self.colors.DARK_BLUE)
        self.btnReduce_1_efx = fw.Button('-1', 20, self.colors.WHITE, self.colors.DARK_BLUE)
        self.btnIncrease_1_efx = fw.Button('+1', 20, self.colors.WHITE, self.colors.DARK_BLUE)
        self.btnReduce_10_efx = fw.Button('-10', 20, self.colors.WHITE, self.colors.DARK_BLUE)
        self.btnIncrease_10_efx = fw.Button('+10', 20, self.colors.WHITE, self.colors.DARK_BLUE)
        # ตัวแปรของ dropdown
        self.dropdownScreen = fw.Dropdown(['Full Screen', '1920x1080', '1280x720', '854x480'], 24, self.colors.WHITE, self.colors.DARK_BLUE)

    def init_page_gacha_variables(self):
        # ตัวแปรหน้า page_gacha
        # ตัวแปรข้อความ
        self.result = 'Random Now!!'
        self.count_gacha = 0
        # ตัวแปรของปุ่ม
        self.btnRandom = fw.Button('สุ่ม 142 gem', 20, self.colors.WHITE, self.colors.GOLD)

    def set_audio_volume(self):
        # audio_music
        audio_volume_music = self.audio_volume_music / 100
        self.audio_background_music.set_volume(audio_volume_music)
        # audio_efx
        audio_volume_efx = self.audio_volume_efx / 100
        self.audio_gacha_efx.set_volume(audio_volume_efx)

    def volume_up_music(self, key):
        self.audio_volume_music = min(100, self.audio_volume_music + key)
        self.set_audio_volume()

    def volume_up_efx(self, key):
        self.audio_volume_efx = min(100, self.audio_volume_efx + key)
        self.set_audio_volume()

    def volume_down_music(self, key):
        self.audio_volume_music = max(0, self.audio_volume_music - key)
        self.set_audio_volume()

    def volume_down_efx(self, key):
        self.audio_volume_efx = max(0, self.audio_volume_efx - key)
        self.set_audio_volume()

    def set_start(self):
        pass
