#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""pdfplumber

Plumb a PDF for detailed information about each char, rectangle, and line.
Plus: Table extraction and visual debugging.
"""

import pdfplumber

# 提取pdf文件中的表格数据
with pdfplumber.open('./files/background-checks.pdf') as pdf:

    # 获取第一页内容
    page0 = pdf.pages[0]

    # 把第一页内容转换为图片
    img = page0.to_image(resolution=150)

    # 框选图片中的文字
    img.draw_rects(page0.extract_words())

    # 预览图片
    img.show()

    # 保存图片
    img.save('./files/bc0.png')
