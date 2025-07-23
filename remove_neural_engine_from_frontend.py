#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import datetime

# 文件路径
html_file = 'src/iphone-compare.html'

# 创建备份
backup_timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
backup_file = f'{html_file}.bak.{backup_timestamp}'

# 读取HTML文件内容
with open(html_file, 'r', encoding='utf-8') as f:
    html_content = f.read()

# 创建备份
with open(backup_file, 'w', encoding='utf-8') as f:
    f.write(html_content)
    print(f'已创建备份文件: {backup_file}')

# 查找并移除neuralEngine参数配置
# 使用正则表达式匹配包含neuralEngine的整行
pattern = r'\s*\{\s*key:\s*[\'"]neuralEngine[\'"],[^\}]+\},?\n?'
updated_content = re.sub(pattern, '', html_content)

# 保存更新后的HTML内容
with open(html_file, 'w', encoding='utf-8') as f:
    f.write(updated_content)

print('更新完成! 已从前端代码中移除 neuralEngine 字段的显示')
