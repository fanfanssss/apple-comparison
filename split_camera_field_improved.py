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

# 定义更精确的正则表达式模式
main_camera_pattern = r'主摄[:：]\s*([^+＋]+)'
ultra_wide_pattern = r'超广角[:：]\s*([^+＋]+)'
telephoto_pattern = r'长焦[:：]\s*([^+＋]+)'

# 计数器
updated_count = 0
failed_count = 0

# 处理每个iPhone型号
for phone in iphone_data:
    if 'camera' in phone:
        camera_text = phone['camera']
        updated = False
        
        # 提取主摄像头信息
        main_camera_match = re.search(main_camera_pattern, camera_text)
        if main_camera_match:
            phone['mainCamera'] = main_camera_match.group(1).strip()
            updated = True
        
        # 提取超广角摄像头信息
        ultra_wide_match = re.search(ultra_wide_pattern, camera_text)
        if ultra_wide_match:
            phone['ultraWideCamera'] = ultra_wide_match.group(1).strip()
            updated = True
        
        # 提取长焦摄像头信息
        telephoto_match = re.search(telephoto_pattern, camera_text)
        if telephoto_match:
            phone['telephotoCamera'] = telephoto_match.group(1).strip()
            updated = True
        
        if updated:
            updated_count += 1
        else:
            failed_count += 1
            print(f"无法解析 {phone.get('name', phone.get('id'))} 的摄像头信息: {camera_text}")

# 保存更新后的JSON数据
with open(json_file, 'w', encoding='utf-8') as f:
    json.dump(iphone_data, f, ensure_ascii=False, indent=2)

print(f'更新完成! 已为 {updated_count} 个iPhone型号拆分camera字段，{failed_count} 个型号解析失败')
