import pygame
from math import ceil


class Screen():
    def __init__(self, x: int, y: int):
        # กำหนดการแบ่งหน้าจอ
        self.MAX_X = x
        self.MAX_Y = y
        # ตั้งค่าให้เต็มจอเป็นค่าเริ่มต้น
        self.set_fullscreen_mode()

    def set_fullscreen_mode(self):
        # ตั้งค่าโหมดการแสดงผลเป็นเต็มหน้าจอ
        self.window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # ตรวจจับความละเอียดหน้าจอปัจจุบัน
        self.__get_screen_info()
        # แบ่งหน้าจออกเป็น grid
        self.__set_axis()

    def set_screen(self, width: int, height: int):
        # ตั้งค่าโหมดการแสดงผลเป็นค่าที่กำหนด
        self.window = pygame.display.set_mode((width, height))
        # ตรวจจับความละเอียดหน้าจอปัจจุบัน
        self.__get_screen_info()
        # แบ่งหน้าจออกเป็น grid
        self.__set_axis()

    def pack_x(self, box_x: int) -> int:
        return self.__resize2x(box_x)
    
    def pack_y(self, box_y: int) -> int:
        return self.__resize2y(box_y)
    
    def width(self, scale: int) -> int:
        return self.__resize2x(scale)
    
    def height(self, scale: int) -> int:
        return self.__resize2y(scale)
    
    def __resize2x(self, scale: int):
        scale = min(self.MAX_X, scale)
        scale = max(scale, 0)
        return ceil(self.x_axis * scale)
    
    def __resize2y(self, scale: int):
        scale = min(self.MAX_Y, scale)
        scale = max(scale, 0)
        return ceil(self.y_axis * scale)

    def __set_axis(self):
        self.x_axis = self.SCREEN_WIDTH / self.MAX_X
        self.y_axis = self.SCREEN_HEIGHT / self.MAX_Y

    def __get_screen_info(self):
        screen_info = pygame.display.Info()
        self.SCREEN_WIDTH = screen_info.current_w
        self.SCREEN_HEIGHT = screen_info.current_h


class Button():
    def __init__(self, 
                 text: str, 
                 font_size: int, 
                 color_text: tuple, 
                 color_button: tuple, 
                 radius=20, 
                 font=None):
        self.text = text
        self.font = pygame.font.SysFont(font, font_size) if font else pygame.font.SysFont(None, font_size)
        self.text_surface = self.font.render(text, True, color_text)
        self.set_button()
        self.color_button = color_button
        self.color_text = color_text
        self.radius = radius
        # สถานะทั้งหมดได้แก่ "normal", "hover", "pressed"
        self.state = "normal"  

    def show(self, 
             screen_draw: pygame.Surface, 
             width_button: int, 
             height_button: int, 
             x: int, y: int):
        self.set_button(width_button, height_button, x, y)
        button_color = self.color_button
        text_color = self.color_text
        
        # เมื่อเมาส์ลอยอยู่เหนือปุ่ม
        if self.state == "hover":
            button_color = [min(255, c + 120) for c in self.color_button] # ทำให้ปุ่มสว่างขึ้น
            text_color = [min(255, c + 20) for c in self.color_text]
        
        pygame.draw.rect(screen_draw, button_color, self.button, 0, self.radius)
        screen_draw.blit(self.font.render(self.text, True, text_color), self.text_rect)

    def set_button(self, 
                   width_button: int,
                   height_button: int, 
                   x: int, y: int):
        self.text_rect = self.text_surface.get_rect(center=(x+(width_button/2), y+(height_button/2)))
        self.button = pygame.Rect(x, y, width_button, height_button)
    
    def click(self, event):
        if event.type == pygame.MOUSEMOTION:
            if self.button.collidepoint(event.pos):
                self.state = "hover"
            else:
                self.state = "normal"
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if self.button.collidepoint(event.pos):
                self.state = "pressed"
                return True  # ส่งคืนค่าว่ากดปุ่มแล้ว
        elif event.type == pygame.MOUSEBUTTONUP:
            if self.state == "pressed":
                self.state = "normal"
        return False


class Text():
    def __init__(self, 
                 text_default: str, 
                 size_text: int, 
                 color_text: tuple, 
                 font=None):
        # สร้างออบเจกต์ Text สำหรับแสดงข้อความบนหน้าจอ
        self.text = text_default
        self.size_text = size_text
        self.color_text = color_text
        self.font = font if font else pygame.font.Font(None, size_text)  # ใช้ฟอนต์เริ่มต้นถ้าไม่ระบุ

    def show(self, 
             screen_draw: pygame.Surface, 
             x: int, y: int,
             text=None,
             center_mode=False):
        if text is not None:
            self.text = text
        text_surface = self.font.render(self.text, True, self.color_text)
        if center_mode:
            text_rect = text_surface.get_rect()  # สร้าง text_rect ก่อน
            text_rect.centerx = x  # กำหนดตำแหน่งกึ่งกลางในแนวแกน x
            text_rect.top = y     # กำหนดตำแหน่ง y ตามที่ต้องการ
        else:
            text_rect = text_surface.get_rect(topleft=(x, y))
        screen_draw.blit(text_surface, text_rect)