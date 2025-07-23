#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import datetime
import os
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

# 清理音频功能描述
updated_count = 0
for phone in iphone_data:
    # 检查audioFeatures字段
    if 'audioFeatures' in phone and phone['audioFeatures']:
        original_text = phone['audioFeatures']
        
        # 使用正则表达式匹配并删除扬声器和麦克风的描述
        # 删除扬声器相关描述
        new_text = re.sub(r'立体声扬声器', '', original_text)
        new_text = re.sub(r'双立体声扬声器', '', new_text)
        new_text = re.sub(r'空间音频立体声扬声器', '', new_text)
        new_text = re.sub(r'空间音频扬声器', '', new_text)
        new_text = re.sub(r'扬声器', '', new_text)
        
        # 删除麦克风相关描述
        new_text = re.sub(r'，[^，]*麦克风[^，]*', '', new_text)
        new_text = re.sub(r'^[^，]*麦克风[^，]*，', '', new_text)
        new_text = re.sub(r'^[^，]*麦克风[^，]*$', '', new_text)
        
        # 清理多余的标点符号
        new_text = re.sub(r'，+', '，', new_text)
        new_text = re.sub(r'^，', '', new_text)
        new_text = re.sub(r'，$', '', new_text)
        
        # 如果文本有变化，更新字段
        if new_text != original_text:
            phone['audioFeatures'] = new_text
            updated_count += 1

# 保存更新后的JSON数据
with open(json_file, 'w', encoding='utf-8') as f:
    json.dump(iphone_data, f, ensure_ascii=False, indent=2)

print(f'更新完成! 已清理 {updated_count} 处音频功能描述')
