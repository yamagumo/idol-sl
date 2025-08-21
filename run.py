import os
import time
from PIL import Image, ImageEnhance
import numpy as np

# --- 設定 ---
image_path = "images/tD_bP_dsKZ5Sbo_Z_aR7KGlN5E9AIHUbywDE6vpHWdE-removebg-preview.png"  # 立ち絵のパス（透過PNG推奨）
width, height = 300, 200          # AA化サイズ（大きめ推奨）
terminal_width = 500            # スクロール幅
scroll_speed = 0.05             # スクロール速度（秒）

# --- 文字セット（濃淡多め） ---
ascii_chars = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/|()1{}[]?-_+~<>i!lI;:,""^`'. "
num_chars = len(ascii_chars)

# --- 画像読み込み（RGBA対応） ---
img = Image.open(image_path).convert("RGBA").resize((width, height))
alpha = np.array(img.getchannel('A'))  # 透明度チャンネル
luminance = ImageEnhance.Contrast(img.convert("L")).enhance(2.0)  # 明度強調
pixels = np.array(luminance)

# --- ピクセルを文字に変換（透明部分は空白に） ---
aa_lines = []
for y in range(height):
    line = ""
    for x in range(width):
        if alpha[y, x] < 10:  # 透明度が低いピクセルは空白に
            line += " "
        else:
            char_index = int(pixels[y, x] / 255 * (num_chars-1))
            line += ascii_chars[char_index]
    aa_lines.append(line)

# --- 横スクロール表示（右→左） ---
max_len = len(aa_lines[0])
while True:
    for offset in range(max_len + terminal_width):
        os.system("cls" if os.name=="nt" else "clear")
        for line in aa_lines:
            # 右から左にずれるようにインデックス計算
            start = max_len - offset
            end = start + terminal_width
            # 負の範囲に入る部分は空白で埋める
            segment = line[start:end] if start >= 0 else line[0:end]
            print(segment.ljust(terminal_width))
        time.sleep(scroll_speed)

