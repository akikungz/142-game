import base64
from PIL import Image
from io import BytesIO


def load_image(base64_data):
    """แปลงไฟล์ base64 กลับเป็นรูปภาพ โดยใช้ขนาดและโหมดสีจากไฟล์"""
    try:
        width = base64_data['width']
        height = base64_data['height']
        color_mode = base64_data['color_mode']
        width, height = int(width), int(height)
        base64_string = base64_data['base64']

        binary_data = base64.b64decode(base64_string)
        img = Image.frombytes(color_mode, (width, height), binary_data)
        img_bytes = BytesIO()
        img.save(img_bytes, format="PNG")  # หรือ format อื่นที่เหมาะสม
        img_bytes.seek(0)  # ย้อนกลับไปที่จุดเริ่มต้นของ BytesIO

        return img_bytes
    except (FileNotFoundError, OSError, ValueError) as e:
        print(f"Error: {e}")


# from picture import img1
# image1 = load_image(img1.img)
# from picture import img2
# image2 = load_image(img2.img)

