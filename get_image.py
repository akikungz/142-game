import sys
import os

# ตรวจสอบว่าอยู่ใน onefile mode หรือไม่
if getattr(sys, '_MEIPASS', None):
    base_path = sys._MEIPASS
else:
    base_path = os.path.abspath(".")

# สร้าง path ไปยังไฟล์รูป
# icon game
icon = os.path.join(base_path, "Assets", "icon.png")
# ปุ่มต่าง ๆ
btnPlay = os.path.join(base_path, "Assets", "picture", "button", "btnPlay.png")
btnGacha = os.path.join(base_path, "Assets", "picture", "button", "btnGacha.png")
btnSetting = os.path.join(base_path, "Assets", "picture", "button", "btnSetting.png")
btnExit = os.path.join(base_path, "Assets", "picture", "button", "btnExit.png")
btnBack = os.path.join(base_path, "Assets", "picture", "button", "btnBack.png")
# gacha banner
banner_AMI = os.path.join(base_path, "Assets", "picture", "gacha",  "banner", "banner_AMI.png")
banner_Ashyra = os.path.join(base_path, "Assets", "picture", "gacha",  "banner", "banner_Ashyra.png")
banner_Debirun = os.path.join(base_path, "Assets", "picture", "gacha",  "banner", "banner_Debirun.png")
banner_MildR = os.path.join(base_path, "Assets", "picture", "gacha",  "banner", "banner_Mild-R.png")
banner_Tsururu = os.path.join(base_path, "Assets", "picture", "gacha",  "banner", "banner_Tsururu.png")
banner_Xonebu = os.path.join(base_path, "Assets", "picture", "gacha",  "banner", "banner_Xonebu.png")
# Assets Background
gem = os.path.join(base_path, "Assets", "picture", "background",  "gem.png")
text_area = os.path.join(base_path, "Assets", "picture", "background",  "text_area.png")