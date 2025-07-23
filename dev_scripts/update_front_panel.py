#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv
import json
import datetime
import os
import re

# 文件路径
csv_file = 'iPhone数据表.csv'
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

# 创建ID到JSON对象的映射
iphone_map = {phone['id']: phone for phone in iphone_data}

# 读取CSV数据
updated_count = 0
with open(csv_file, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        iphone_id = row['ID']
        
        if iphone_id in iphone_map:
            phone = iphone_map[iphone_id]
            updated = False
            
            # 提取前面板信息
            if 'materials' in row and row['materials']:
                # 使用正则表达式提取前面板信息
                front_panel_match = re.search(r'Ceramic Shield\s*(?:前面板|前玻璃)', row['materials'])
                if front_panel_match:
                    phone['frontPanel'] = front_panel_match.group(0)
                    updated = True
                elif 'frontPanel' not in phone:
                    # 如果没有找到匹配，设置为"-"
                    phone['frontPanel'] = "-"
                    updated = True
            
            if updated:
                updated_count += 1

# 保存更新后的JSON数据
with open(json_file, 'w', encoding='utf-8') as f:
    json.dump(iphone_data, f, ensure_ascii=False, indent=2)

print(f'更新完成! 已更新 {updated_count} 个iPhone型号的前面板信息')
