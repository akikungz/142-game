import sys
import math
import pygame
import framework as fw
from variable import Variable
import random

# เพิ่มคลาส Card
class Card(pygame.sprite.Sprite):
    def __init__(self, 
                 front_image: pygame.Surface, 
                 back_image: pygame.Surface, 
                 x: int, y: int, 
                 width: int, height: int):
        super().__init__()  # เรียกใช้ constructor ของคลาสแม่ (Sprite)
        self.front_image = front_image
        self.back_image = back_image
        self.image = self.front_image  # ตั้งค่าภาพเริ่มต้นให้กับ sprite
        self.rect = pygame.Rect(x, y, width, height)
        # ตรวจสอบหากการ์ดเปิดอยู่จะเป็น True
        self.is_flipped = True
        self.is_matched = False
        self.flip_progress = 0
        self.flip_speed = 10

    def flip(self):
        if not self.is_matched:
            self.is_flipped = not self.is_flipped
            self.flip_progress = 0

    def update(self):
        # ทำการหมุนการ์ดถ้า flip_progress < 180
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

        # คำนวณขนาดของการ์ด
        scaled_width = int(self.rect.width * abs(math.cos(math.radians(angle))))
        scaled_image = pygame.transform.scale(image, (scaled_width, self.rect.height))
        screen.blit(scaled_image, (self.rect.x + (self.rect.width - scaled_width) // 2, self.rect.y))

# เพิ่มคลาส MatchingGame
class MatchingGame:
    def __init__(self, 
                 screen: fw.Screen, 
                 card_images: list, 
                 back_image: pygame.Surface, 
                 rows: int, cols: int):
        self.screen = screen
        self.screen_window = screen.window
        self.card_images = card_images * 2  # สร้างคู่ของการ์ดแต่ละใบ
        random.shuffle(self.card_images)
        self.back_image = back_image
        self.rows = rows
        self.cols = cols
        self.flip_time = 0
        # การ์ดทั้งหมด
        self.cards: pygame.sprite.Group[Card] = pygame.sprite.Group()
        # การ์ดที่กำลังถูกเลือกอยู่ หรือการ์ดที่เปิดอยู่ ณ ตอนนั้น
        self.selected_cards: pygame.sprite.Group[Card] = pygame.sprite.Group()
        # จับเวลาเมื่อเริ่มเกม
        self.initial_display_time = 2000  # 2 วินาที
        self.start_time = pygame.time.get_ticks()
        self.initial_display = True
        # จับเวลาเมื่อ card match
        self.match_display_time = 1000  # 1 วินาที
        self.match_time = []
        self.matched_cards: pygame.sprite.Group[Card] = pygame.sprite.Group()
        self.create_cards()

    def create_cards(self):
        margin = self.screen.width(10)  # ระยะห่างระหว่างการ์ด
        card_width = (self.screen_window.get_width() - (self.cols + 1) * margin) // self.cols
        card_height = (self.screen_window.get_height() - (self.rows + 1) * margin) // self.rows
        for i in range(self.rows):
            for j in range(self.cols):
                x = margin + j * (card_width + margin)
                y = margin + i * (card_height + margin)
                front_image = self.card_images[i * self.cols + j]
                card = Card(front_image, self.back_image, x, y, card_width, card_height)
                self.cards.add(card)

    def flip_back_cards(self):
        for card in self.selected_cards:
            if not card.is_matched:
                card.flip()
        self.selected_cards.empty()

    def flip_card(self, card):
        if not card.is_flipped and not card.is_matched:
            card.flip()
            self.selected_cards.add(card)
            # ถ้ามีการ์ดที่ถูกเลือก 2 ใบแล้ว และไม่มีการ์ดที่ match กันอยู่ เริ่มจับเวลา
            if len(self.selected_cards) == 2 and len(self.matched_cards) == 0:
                self.flip_time = pygame.time.get_ticks()

    def update(self):
        current_time = pygame.time.get_ticks()
        
        # เมื่อเริ่มเกมให้เปิดการ์ดทั้งหมดในระยะเวลาหนึ่งเพื่อให้ผู้เล่นจดจำการ์ด
        if self.initial_display:
            if current_time - self.start_time > self.initial_display_time:
                self.initial_display = False
                for card in self.cards:
                    card.flip()
        
        # สำหรับแสดงผลการ์ดให้หมุน
        self.cards.update()

        # จัดการการแสดงผลกับการ์ดที่ match กัน
        if len(self.matched_cards) > 0:
            if current_time - self.match_time[0] > self.match_display_time:
                # ทำการเปลี่ยนสถานะของการ์ดให้เป็น matched
                for card in list(self.matched_cards)[:2]:
                    card.is_matched = True
                    self.matched_cards.remove(card)
                # ลบเวลาการ match ของการ์ดที่ได้ทำการจับคู่
                self.match_time = self.match_time[1:]
                # สร้าง Group ชั่วคราวเพื่อเก็บการ์ดที่ไม่ถูก match
                temp_selected_cards = pygame.sprite.Group()
                for card in self.selected_cards:
                    if not card.is_matched:
                        temp_selected_cards.add(card)
                # อัปเดตกลุ่มการ์ดที่ถูกเลือกด้วยการ์ดที่ไม่ถูก match
                self.selected_cards = temp_selected_cards

        # ถ้ามีการ์ดที่เปิดอยู่มากกว่า 2 ใบและไม่ตรงกัน ให้พลิกกลับหลังจาก 1 วินาที
        if len(self.selected_cards) > 2:
            # เก็บการ์ดที่เกิน 2 ใบในกลุ่ม selected_cards
            cards_to_flip = list(self.selected_cards)[:-2]
            for card in cards_to_flip:
                if not card.is_matched:
                    card.flip()
                    self.selected_cards.remove(card)
        # ถ้ามีการ์ดที่เปิดอยู่ 2 ใบและไม่มีการ์ดที่ match กัน
        elif len(self.selected_cards) == 2 and len(self.matched_cards) == 0:
            # ถ้าเวลาผ่านไปมากกว่า 1 วินาที ให้พลิกการ์ดกลับ
            if current_time - self.flip_time > 1000:  # 1000 ms = 1 วินาที
                self.flip_back_cards()

    def check_match(self):
        if len(self.selected_cards) == 2:
            selected_cards_list = list(self.selected_cards)
            if selected_cards_list[0].front_image == selected_cards_list[1].front_image:
                for card in selected_cards_list:
                    self.matched_cards.add(card)
                self.match_time.append(pygame.time.get_ticks())
                self.selected_cards.empty()
                print("Match found!")
            else:
                print("No match")


    def draw(self):
        for card in self.cards:
            card.draw(self.screen_window)
        for card in self.matched_cards:
            card.draw(self.screen_window)

    def is_game_over(self):
        return all(card.is_matched for card in self.cards)

    def handle_events(self, event: pygame.event.Event):
        if self.initial_display:
            return
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            for card in self.cards:
                if card.rect.collidepoint(event.pos):
                    self.flip_card(card)
                    self.check_match()
                    break  # ออกจากลูปหลังจากพลิกการ์ดแล้ว
# ฟังก์ชันหลักของเกม
def main(pygame: pygame, 
         var: Variable, 
         screen: fw.Screen):

    game = MatchingGame(screen, var.card_images, var.back_image, 2, 6)

    running = True
    while running:
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

        screen.window.fill(var.colors.WHITE)
        game.update()
        game.draw()
        var.btnBack.show(screen.window, screen.width(20), screen.height(20), screen.pack_x(10), screen.pack_y(10))

        if game.is_game_over():
            print("Congratulations! You've matched all cards!")
            running = False

        pygame.display.flip()
        var.clock.tick(30)