import sys
import os

# ตรวจสอบว่าอยู่ใน onefile mode หรือไม่
if getattr(sys, '_MEIPASS', None):
    base_path = sys._MEIPASS
else:
    base_path = os.path.abspath(".")

# สร้าง path ไปยังไฟล์รูป
icon = os.path.join(base_path, "Assets", "icon.png")
btnPlay = os.path.join(base_path, "Assets", "picture", "button", "btnPlay.png")
btnGacha = os.path.join(base_path, "Assets", "picture", "button", "btnGacha.png")
btnSetting = os.path.join(base_path, "Assets", "picture", "button", "btnSetting.png")
btnExitImg = os.path.join(base_path, "Assets", "picture", "button", "btnExitImg.png")