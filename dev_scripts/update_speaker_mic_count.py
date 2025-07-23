#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import csv
import datetime
import os
import re

# 文件路径
json_file = 'public/data/iphone_refined.json'
csv_file = 'iPhone数据表.csv'

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

# 从CSV读取扬声器数量和麦克风数量
speaker_mic_data = {}
with open(csv_file, 'r', encoding='utf-8') as f:
    csv_reader = csv.DictReader(f)
    for row in csv_reader:
        phone_id = row.get('ID', '')
        speaker_count = row.get('扬声器数量', '')
        mic_count = row.get('麦克风数量', '')
        
        if phone_id:
            speaker_mic_data[phone_id] = {
                'speakers': speaker_count if speaker_count else '-',
                'microphoneCount': mic_count if mic_count else '-'
            }

# 更新JSON数据
speakers_updated = 0
mic_updated = 0

for phone in iphone_data:
    phone_id = phone.get('id', '')
    
    if phone_id in speaker_mic_data:
        # 更新扬声器数量
        speaker_count = speaker_mic_data[phone_id]['speakers']
        if speaker_count != '-':
            phone['speakers'] = f"{speaker_count}个扬声器"
            speakers_updated += 1
        
        # 更新或添加麦克风数量
        mic_count = speaker_mic_data[phone_id]['microphoneCount']
        if mic_count != '-':
            phone['microphoneCount'] = f"{mic_count}个麦克风"
            mic_updated += 1

# 保存更新后的JSON数据
with open(json_file, 'w', encoding='utf-8') as f:
    json.dump(iphone_data, f, ensure_ascii=False, indent=2)

print(f'更新完成! 已更新 {speakers_updated} 个iPhone型号的扬声器数量，{mic_updated} 个iPhone型号的麦克风数量')
