#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import datetime
import re

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

# 从displayTechnology中提取PPI值并添加displayPpi字段
updated_count = 0
for phone in iphone_data:
    if 'displayTechnology' in phone and phone['displayTechnology']:
        # 使用正则表达式匹配PPI值
        ppi_match = re.search(r'(\d+)ppi', phone['displayTechnology'])
        if ppi_match:
            ppi_value = int(ppi_match.group(1))
            phone['displayPpi'] = ppi_value
            updated_count += 1
        else:
            # 如果没有找到PPI值，设置为"-"
            phone['displayPpi'] = "-"
            print(f"警告: 无法从 {phone.get('name', '未知型号')} 的displayTechnology中提取PPI值")

# 保存更新后的JSON数据
with open(json_file, 'w', encoding='utf-8') as f:
    json.dump(iphone_data, f, ensure_ascii=False, indent=2)

print(f'更新完成! 已为 {updated_count} 个iPhone型号添加displayPpi字段')
