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

# 删除所有"紧急SOS"文案
updated_count = 0
for phone in iphone_data:
    # 检查所有可能包含文本的字段
    text_fields = ['specialFeatures', 'specialSoftwareFeatures', 'marketingSlogan']
    
    for field in text_fields:
        if field in phone and phone[field] and isinstance(phone[field], str):
            # 如果字段包含"紧急SOS"
            if "紧急SOS" in phone[field]:
                # 删除"紧急SOS"及其前后可能的标点符号
                new_text = re.sub(r'[，,、]*紧急SOS[，,、]*', '', phone[field])
                # 处理可能出现的多余逗号
                new_text = re.sub(r'[，,、]{2,}', '，', new_text)
                # 处理开头和结尾的逗号
                new_text = new_text.strip('，,、 ')
                
                if new_text != phone[field]:
                    phone[field] = new_text
                    updated_count += 1

# 保存更新后的JSON数据
with open(json_file, 'w', encoding='utf-8') as f:
    json.dump(iphone_data, f, ensure_ascii=False, indent=2)

print(f'更新完成! 已从 {updated_count} 处删除"紧急SOS"文案')
