import sys
import os

# ตรวจสอบว่าอยู่ใน onefile mode หรือไม่
if getattr(sys, '_MEIPASS', None):
    base_path = sys._MEIPASS
else:
    base_path = os.path.abspath(".")

# สร้าง path ไปยังไฟล์รูป
test = os.path.join(base_path, "Assets", "audio", "test.png")