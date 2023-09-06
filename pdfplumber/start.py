#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""pdfplumber

Plumb a PDF for detailed information about each char, rectangle, and line.
Plus: Table extraction and visual debugging.
"""

import pdfplumber

# 提取pdf文件中的表格数据
with pdfplumber.open('./files/csrc.pdf') as pdf:
    page_num = 0  # 页数
    line_num = 0  # 行数

    for page in pdf.pages:
        page_num += 1
        print('---------- Page {} ----------'.format(page_num))

        # 抽取表格数据
        lines = page.extract_table()

        for line in lines[1:]:  # 去掉行头
            line_num += 1
            print('Line', line_num, line)
