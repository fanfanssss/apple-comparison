#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import re
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

# 定义正则表达式模式来匹配和移除"x倍光学变焦"和逗号
zoom_pattern = r'，\s*\d+(?:\.\d+)?倍光学变焦'

# 计数器
updated_count = 0

# 处理每个iPhone型号
for phone in iphone_data:
    if 'telephotoCamera' in phone and phone['telephotoCamera']:
        original = phone['telephotoCamera']
        # 移除"，x倍光学变焦"部分
        cleaned = re.sub(zoom_pattern, '', phone['telephotoCamera'])
        
        if original != cleaned:
            phone['telephotoCamera'] = cleaned
            updated_count += 1
            print(f"已更新 {phone.get('name', phone.get('id'))} 的长焦摄像头描述:")
            print(f"  原始: {original}")
            print(f"  更新后: {cleaned}")

# 保存更新后的JSON数据
with open(json_file, 'w', encoding='utf-8') as f:
    json.dump(iphone_data, f, ensure_ascii=False, indent=2)

print(f'更新完成! 已清理 {updated_count} 个iPhone型号的长焦摄像头描述')
