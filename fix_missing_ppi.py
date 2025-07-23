#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import datetime

# 文件路径
json_file = 'public/data/iphone_refined.json'

# 创建备份
backup_timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
backup_file = f'{json_file}.bak.{backup_timestamp}'

# 手动设置的PPI值映射
ppi_mapping = {
    'iphone-15-pro-max': 460,
    'iphone-15-pro': 460,
    'iphone-15-plus': 458,
    'iphone-15': 460,
    'iphone-16-pro-max': 460,
    'iphone-16-pro': 460,
    'iphone-16-plus': 458,
    'iphone-16': 460,
    'iphone-16e': 460
}

# 读取JSON数据
with open(json_file, 'r', encoding='utf-8') as f:
    iphone_data = json.load(f)

# 创建备份
with open(backup_file, 'w', encoding='utf-8') as f:
    json.dump(iphone_data, f, ensure_ascii=False, indent=2)
    print(f'已创建备份文件: {backup_file}')

# 手动添加或修正缺失的PPI值
updated_count = 0
for phone in iphone_data:
    phone_id = phone.get('id')
    if phone_id in ppi_mapping:
        phone['displayPpi'] = ppi_mapping[phone_id]
        updated_count += 1
        print(f"已为 {phone.get('name', phone_id)} 手动设置PPI值: {ppi_mapping[phone_id]}")

# 保存更新后的JSON数据
with open(json_file, 'w', encoding='utf-8') as f:
    json.dump(iphone_data, f, ensure_ascii=False, indent=2)

print(f'更新完成! 已为 {updated_count} 个iPhone型号手动修正displayPpi字段')
