#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import datetime
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

# 删除接口类型描述中的"最高"两个字
updated_count = 0
for phone in iphone_data:
    if 'ports' in phone and phone['ports']:
        if '最高' in phone['ports']:
            phone['ports'] = phone['ports'].replace('最高', '')
            updated_count += 1

# 保存更新后的JSON数据
with open(json_file, 'w', encoding='utf-8') as f:
    json.dump(iphone_data, f, ensure_ascii=False, indent=2)

print(f'更新完成! 已从 {updated_count} 个iPhone型号的接口类型描述中删除"最高"两个字')
