import base64
from io import BytesIO

def load_audio(base64_string):
    """แปลง Base64 กลับเป็นไฟล์เสียง"""
    try:
        # ถอดรหัส base64
        sound_bytes = base64.b64decode(base64_string)
        # สร้าง BytesIO object
        sound = BytesIO(sound_bytes)

        return sound
    except Exception as e:
        print(f"Error loading sound: {e}")
        return None


# from audio import audio1
# audio1 = load_audio(audio1.audio)
