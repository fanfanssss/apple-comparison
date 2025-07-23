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

# 定义正则表达式模式来提取光学变焦信息
zoom_pattern = r'(\d+(?:\.\d+)?)倍光学变焦'

# 计数器
added_count = 0
already_exists_count = 0
no_zoom_count = 0

# 处理每个iPhone型号
for phone in iphone_data:
    # 如果已经有opticalZoom字段，跳过
    if 'opticalZoom' in phone and phone['opticalZoom']:
        already_exists_count += 1
        continue
    
    # 尝试从telephotoCamera字段提取
    zoom_info = None
    if 'telephotoCamera' in phone and phone['telephotoCamera']:
        zoom_match = re.search(zoom_pattern, phone['telephotoCamera'])
        if zoom_match:
            zoom_info = f"{zoom_match.group(1)}倍"
    
    # 如果telephotoCamera中没有找到，尝试从camera字段提取
    if not zoom_info and 'camera' in phone and phone['camera']:
        zoom_match = re.search(zoom_pattern, phone['camera'])
        if zoom_match:
            zoom_info = f"{zoom_match.group(1)}倍"
    
    # 如果找到了光学变焦信息，添加到JSON中
    if zoom_info:
        phone['opticalZoom'] = zoom_info
        added_count += 1
        print(f"为 {phone.get('name', phone.get('id'))} 添加光学变焦: {zoom_info}")
    else:
        # 根据iPhone型号设置默认值
        if 'telephotoCamera' in phone and phone['telephotoCamera']:
            # 有长焦镜头但未提取到变焦倍率的情况
            phone['opticalZoom'] = "有（未知倍率）"
            added_count += 1
            print(f"为 {phone.get('name', phone.get('id'))} 添加默认光学变焦: 有（未知倍率）")
        else:
            # 没有长焦镜头的情况
            phone['opticalZoom'] = "无"
            added_count += 1
            print(f"为 {phone.get('name', phone.get('id'))} 添加默认光学变焦: 无")
            no_zoom_count += 1

# 保存更新后的JSON数据
with open(json_file, 'w', encoding='utf-8') as f:
    json.dump(iphone_data, f, ensure_ascii=False, indent=2)

print(f'更新完成! 已为 {added_count} 个iPhone型号添加opticalZoom字段')
print(f'其中 {no_zoom_count} 个型号没有光学变焦功能，设置为"无"')
print(f'{already_exists_count} 个型号已有opticalZoom字段，保持不变')
