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

# 清理系统版本文案
updated_count = 0
for phone in iphone_data:
    # 检查initialOS字段
    if 'initialOS' in phone and phone['initialOS']:
        # 删除"及更高版本"和"可升级至xxx"等文案
        original_text = phone['initialOS']
        
        # 使用正则表达式匹配并删除这些文案
        new_text = re.sub(r'及更高版本', '', original_text)
        new_text = re.sub(r'，可升级至[^，]*', '', new_text)
        new_text = re.sub(r'可升级至[^，]*', '', new_text)
        
        # 如果文本有变化，更新字段
        if new_text != original_text:
            phone['initialOS'] = new_text
            updated_count += 1
    
    # 检查os字段
    if 'os' in phone and phone['os']:
        # 删除"及更高版本"和"可升级至xxx"等文案
        original_text = phone['os']
        
        # 使用正则表达式匹配并删除这些文案
        new_text = re.sub(r'及更高版本', '', original_text)
        new_text = re.sub(r'，可升级至[^，]*', '', new_text)
        new_text = re.sub(r'可升级至[^，]*', '', new_text)
        
        # 如果文本有变化，更新字段
        if new_text != original_text:
            phone['os'] = new_text
            updated_count += 1

# 保存更新后的JSON数据
with open(json_file, 'w', encoding='utf-8') as f:
    json.dump(iphone_data, f, ensure_ascii=False, indent=2)

print(f'更新完成! 已清理 {updated_count} 处系统版本文案')
