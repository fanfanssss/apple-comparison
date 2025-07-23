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

# 需要更新为3D Touch的iPhone型号
iphone_models_3d_touch = [
    'iphone-xr',
    'iphone-xs',
    'iphone-xs-max',
    'iphone-x',
    'iphone-8-plus',
    'iphone-8',
    'iphone-7',
    'iphone-7-plus',
    'iphone-6s',
    'iphone-6s-plus'
]

# 计数器
updated_count = 0

# 处理每个iPhone型号
for phone in iphone_data:
    phone_id = phone.get('id', '')
    
    # 检查是否为需要更新的型号
    if phone_id in iphone_models_3d_touch:
        # 更新触控技术为3D Touch
        old_value = phone.get('touchTechnology', '-')
        phone['touchTechnology'] = "3D Touch"
        updated_count += 1
        print(f"更新 {phone.get('name', phone_id)} 的触控技术: {old_value} -> 3D Touch")

# 保存更新后的JSON数据
with open(json_file, 'w', encoding='utf-8') as f:
    json.dump(iphone_data, f, ensure_ascii=False, indent=2)

print(f'更新完成! 已更新 {updated_count} 个iPhone型号的触控技术为"3D Touch"')
