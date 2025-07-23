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

# 计数器
updated_count = 0

# 处理每个iPhone型号
for phone in iphone_data:
    # 检查所有可能包含"Ceramic Shield"的字段
    fields_to_check = ['frontPanel', 'materials', 'displayTechnology']
    
    for field in fields_to_check:
        if field in phone and isinstance(phone[field], str):
            # 替换"Ceramic Shield 2"为"超瓷晶面板二代"
            if "Ceramic Shield 2" in phone[field]:
                phone[field] = phone[field].replace("Ceramic Shield 2", "超瓷晶面板二代")
                updated_count += 1
            # 替换"Ceramic Shield"为"超瓷晶面板"（确保不会替换已经替换过的"超瓷晶面板二代"中的部分文本）
            elif "Ceramic Shield" in phone[field]:
                phone[field] = phone[field].replace("Ceramic Shield", "超瓷晶面板")
                updated_count += 1

# 保存更新后的JSON数据
with open(json_file, 'w', encoding='utf-8') as f:
    json.dump(iphone_data, f, ensure_ascii=False, indent=2)

print(f'更新完成! 已替换 {updated_count} 处"Ceramic Shield"相关文本')
