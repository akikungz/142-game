import sys
import math
import pygame
import framework as fw
from variable import Variable
import random

# เพิ่มคลาส Card
class Card(fw.ImageButton):
    def __init__(self, 
                 image_path: str, 
                 back_image_path: str, 
                 x: int, y: int, 
                 width: int, height: int):
        super().__init__("", 0, (0,0,0), image_path)
        self.image_path = image_path
        self.front_image = pygame.image.load(image_path).convert_alpha()
        self.back_image = pygame.image.load(back_image_path).convert_alpha()
        self.rect = pygame.Rect(x, y, width, height)
        self.is_flipped = False
        self.is_matched = False
        self.flip_progress = 0
        self.flip_speed = 10

    def flip(self):
        if not self.is_matched:
            self.is_flipped = not self.is_flipped
            self.flip_progress = 0

    def update(self):
        if self.flip_progress < 180:
            self.flip_progress += self.flip_speed

    def draw(self, screen):
        if self.is_matched:
            return

        if self.flip_progress < 90:
            angle = self.flip_progress
            image = self.back_image if not self.is_flipped else self.front_image
        else:
            angle = 180 - self.flip_progress
            image = self.front_image if self.is_flipped else self.back_image

        scaled_width = int(self.rect.width * abs(math.cos(math.radians(angle))))
        scaled_image = pygame.transform.scale(image, (scaled_width, self.rect.height))
        screen.blit(scaled_image, (self.rect.x + (self.rect.width - scaled_width) // 2, self.rect.y))

# เพิ่มคลาส MatchingGame
class MatchingGame:
    def __init__(self, 
                 screen: fw.Screen, 
                 card_images, back_image, 
                 rows: int, cols: int):
        self.screen = screen
        self.screen_window = screen.window
        self.card_images = card_images * 2  # สร้างคู่ของการ์ดแต่ละใบ
        random.shuffle(self.card_images)
        self.back_image = back_image
        self.rows = rows
        self.cols = cols
        self.flip_time = 0
        self.cards = []
        self.selected_cards = []
        self.create_cards()

    def create_cards(self):
        margin = self.screen.width(10)  # ระยะห่างระหว่างการ์ด
        card_width = (self.screen_window.get_width() - (self.cols + 1) * margin) // self.cols
        card_height = (self.screen_window.get_height() - (self.rows + 1) * margin) // self.rows
        for i in range(self.rows):
            for j in range(self.cols):
                x = margin + j * (card_width + margin)
                y = margin + i * (card_height + margin)
                image_path = self.card_images[i * self.cols + j]
                card = Card(image_path, self.back_image, x, y, card_width, card_height)
                self.cards.append(card)

    def handle_events(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if len(self.selected_cards) == 2:
                # ถ้ามีการ์ดที่เปิดอยู่แล้ว 2 ใบ ให้พลิกกลับก่อน
                self.flip_back_cards()
            
            for card in self.cards:
                if card.rect.collidepoint(event.pos) and not card.is_flipped and not card.is_matched:
                    self.flip_card(card)
                    break  # ออกจากลูปหลังจากพลิกการ์ดแล้ว

    def flip_back_cards(self):
        for card in self.selected_cards:
            if not card.is_matched:
                card.flip()
        self.selected_cards = []

    def flip_card(self, card):
        # เช็คว่ามีการ์ดที่ถูกเลือกแล้วน้อยกว่า 2 ใบหรือไม่
        if len(self.selected_cards) < 2:
            card.flip()
            self.selected_cards.append(card)
            # ถ้ามีการ์ดที่ถูกเลือก 2 ใบแล้ว เริ่มจับเวลา
            if len(self.selected_cards) == 2:
                self.flip_time = pygame.time.get_ticks()
                self.check_match()

    def update(self):
        current_time = pygame.time.get_ticks()
        for card in self.cards:
            card.update()

        # ถ้ามีการ์ดที่เปิดอยู่ 2 ใบและไม่ตรงกัน ให้พลิกกลับหลังจาก 1 วินาที
        if len(self.selected_cards) == 2:
            if not self.selected_cards[0].is_matched and (current_time - self.flip_time > 1000):  # 1000 ms = 1 วินาที
                self.flip_back_cards()

    def check_match(self):
        if len(self.selected_cards) == 2:
            if self.selected_cards[0].image_path == self.selected_cards[1].image_path:
                for card in self.selected_cards:
                    card.is_matched = True
                print("Match found!")
            else:
                print("No match")
            # ไม่ต้องพลิกการ์ดกลับที่นี่ จะให้ฟังก์ชัน update จัดการพลิกกลับ


    def draw(self):
        self.screen_window.fill((255, 255, 255))  # พื้นหลังสีขาว
        for card in self.cards:
            card.draw(self.screen_window)

    def is_game_over(self):
        return all(card.is_matched for card in self.cards)

# ฟังก์ชันหลักของเกม
def main(pygame: pygame, 
         var: Variable, 
         screen: fw.Screen):

    game = MatchingGame(screen, var.card_images, var.back_image, 2, 6)

    running = True
    while running:
        current_time = pygame.time.get_ticks()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # Press ESC to exit
                    pygame.quit()
                    sys.exit()
            elif var.btnBack.click(event):
                running = False
            else:
                game.handle_events(event)

        game.update()
        game.draw()
        var.btnBack.show(screen.window, screen.width(20), screen.height(20), screen.pack_x(10), screen.pack_y(10))

        if game.is_game_over():
            print("Congratulations! You've matched all cards!")
            running = False

        pygame.display.flip()
        var.clock.tick(30)
