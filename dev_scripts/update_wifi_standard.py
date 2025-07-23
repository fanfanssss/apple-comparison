#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import csv
import datetime
import os

# 文件路径
csv_file = 'iPhone数据表.csv'
json_file = 'public/data/iphone_refined.json'

# 创建备份
backup_timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
backup_file = f'{json_file}.bak.{backup_timestamp}'

# 读取CSV数据，提取WiFi标准信息
wifi_data = {}
with open(csv_file, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        phone_id = row['ID']
        wifi_standard = row.get('WiFi标准', '-')
        if wifi_standard and wifi_standard.strip():
            wifi_data[phone_id] = wifi_standard
        else:
            wifi_data[phone_id] = '-'

# 读取JSON数据
with open(json_file, 'r', encoding='utf-8') as f:
    iphone_data = json.load(f)

# 创建备份
with open(backup_file, 'w', encoding='utf-8') as f:
    json.dump(iphone_data, f, ensure_ascii=False, indent=2)
    print(f'已创建备份文件: {backup_file}')

# 更新JSON数据中的WiFi标准
updated_count = 0
for phone in iphone_data:
    phone_id = phone.get('id')
    if phone_id in wifi_data:
        phone['wifiStandard'] = wifi_data[phone_id]
        updated_count += 1

# 保存更新后的JSON数据
with open(json_file, 'w', encoding='utf-8') as f:
    json.dump(iphone_data, f, ensure_ascii=False, indent=2)

print(f'更新完成! 已为 {updated_count} 个iPhone型号添加或更新WiFi标准信息')
