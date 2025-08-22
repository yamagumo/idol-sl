#!/usr/bin/env python3
import os
import sys
from PIL import Image


# 設定


# run.py のあるディレクトリを基準
base_dir = os.path.dirname(os.path.abspath(__file__))

# images フォルダに置いたファイル名
image_filename = "4_20241024153317.png" # imagesに置いたpngファイル

# 画像の絶対パス
image_path = os.path.join(base_dir, "images", image_filename)

# AA変換用のサイズ
width, height = 500, 200          # AA化サイズ
terminal_width = 500            # スクロール幅
scroll_speed = 0.1             # スクロール速度（秒）


# 画像読み込み


if not os.path.exists(image_path):
    print(f"Error: 画像ファイルが見つかりません -> {image_path}")
    sys.exit(1)

try:
    img = Image.open(image_path).convert("RGBA").resize((width, height))
except Exception as e:
    print(f"Error: 画像を開けませんでした -> {e}")
    sys.exit(1)

# ===========================
# ここから AA変換処理
# （サンプルとしてRGBA→文字列簡易表示）
# ===========================

pixels = img.getdata()
ascii_chars = "@%#*+=-:. "  # 明るさに応じて変える文字

aa_lines = []
for y in range(height):
    line = ""
    for x in range(width):
        r, g, b, a = pixels[y * width + x]
        if a < 128:  # 透過は空白
            line += " "
        else:
            # 明るさ計算
            brightness = int((r + g + b) / 3)
            char_index = brightness * (len(ascii_chars) - 1) // 255
            line += ascii_chars[char_index]
    aa_lines.append(line)


# 右から左にスクロール表示


import time
import shutil

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
