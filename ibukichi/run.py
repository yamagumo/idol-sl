# ibukichi/run.py
import os
import sys
from PIL import Image
import time

def main():
    # 設定
    base_dir = os.path.dirname(os.path.abspath(__file__))
    image_filename = "4_20241024153317.png"
    image_path = os.path.join(base_dir, "images", image_filename)
    width, height = 500, 200
    terminal_width = 500
    scroll_speed = 0.05

    if not os.path.exists(image_path):
        print(f"Error: 画像ファイルが見つかりません -> {image_path}")
        sys.exit(1)

    try:
        img = Image.open(image_path).convert("RGBA").resize((width, height))
    except Exception as e:
        print(f"Error: 画像を開けませんでした -> {e}")
        sys.exit(1)

    pixels = img.getdata()
    ascii_chars = "@%#*+=-:. "
    aa_lines = []

    for y in range(height):
        line = ""
        for x in range(width):
            r, g, b, a = pixels[y * width + x]
            if a < 128:
                line += " "
            else:
                brightness = int((r + g + b) / 3)
                char_index = brightness * (len(ascii_chars) - 1) // 255
                line += ascii_chars[char_index]
        aa_lines.append(line)

    max_len = len(aa_lines[0])
    while True:
        for offset in range(max_len + terminal_width):
            os.system("cls" if os.name=="nt" else "clear")
            for line in aa_lines:
                start = max_len - offset
                end = start + terminal_width
                segment = line[start:end] if start >= 0 else line[0:end]
                print(segment.ljust(terminal_width))
            time.sleep(scroll_speed)
