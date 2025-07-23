#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import datetime

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

# 需要更新的iPhone 12系列型号
iphone12_models = [
    'iphone-12',
    'iphone-12-mini',
    'iphone-12-pro',
    'iphone-12-pro-max'
]

# 计数器
updated_count = 0

# 处理每个iPhone型号
for phone in iphone_data:
    phone_id = phone.get('id', '')
    
    # 检查是否为iPhone 12系列
    if phone_id in iphone12_models:
        # 更新前面板材质为超瓷晶面板
        old_value = phone.get('frontPanel', '-')
        phone['frontPanel'] = "超瓷晶面板"
        updated_count += 1
        print(f"更新 {phone.get('name', phone_id)} 的前面板材质: {old_value} -> 超瓷晶面板")

# 保存更新后的JSON数据
with open(json_file, 'w', encoding='utf-8') as f:
    json.dump(iphone_data, f, ensure_ascii=False, indent=2)

print(f'更新完成! 已更新 {updated_count} 个iPhone 12系列的前面板材质为"超瓷晶面板"')
