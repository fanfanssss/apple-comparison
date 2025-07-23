#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import datetime
import os

# 文件路径
json_file = 'public/data/iphone_refined.json'

# 创建备份
backup_timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
backup_file = f'{json_file}.bak.{backup_timestamp}'

# 读取JSON数据
with open(json_file, 'r', encoding='utf-8') as f:
    iphone_data = json.load(f)

# 创建备份
with open(backup_file, 'w', encoding='utf-8') as f:
    json.dump(iphone_data, f, ensure_ascii=False, indent=2)
    print(f'已创建备份文件: {backup_file}')

# 更新iPhone 16e的PPI值
updated = False
for phone in iphone_data:
    if phone.get('id') == 'iphone-16e':
        # 添加displayPpi字段
        phone['displayPpi'] = 460
        updated = True
        print(f"已为iPhone 16e添加PPI值: 460")
        break

if not updated:
    print("未找到iPhone 16e型号")

# 保存更新后的JSON数据
with open(json_file, 'w', encoding='utf-8') as f:
    json.dump(iphone_data, f, ensure_ascii=False, indent=2)

if updated:
    print('更新完成!')
