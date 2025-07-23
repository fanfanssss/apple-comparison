#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import csv
import re
import datetime

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

# 从CSV文件读取材质信息
csv_materials = {}
with open(csv_file, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        phone_id = row.get('ID', '')
        materials_str = row.get('materials', '')
        if phone_id and materials_str:
            csv_materials[phone_id] = materials_str

# 从materials字段提取材质信息的函数
def extract_materials_from_description(materials_str):
    result = {}
    
    # 提取前面板材质
    front_panel_match = re.search(r'(超瓷晶面板二代|超瓷晶面板|Ceramic Shield 2|Ceramic Shield|玻璃)前', materials_str)
    if front_panel_match:
        result['frontPanel'] = front_panel_match.group(1)
    
    # 提取中框材质
    frame_match = re.search(r'(钛金属|不锈钢|铝合金|塑料)中框', materials_str)
    if frame_match:
        result['frameMaterial'] = frame_match.group(1)
    
    # 提取背板材质
    back_match = re.search(r'(磨砂玻璃|玻璃|铝合金|塑料)背', materials_str)
    if back_match:
        result['backPanelMaterial'] = back_match.group(1)
    
    return result

# 计数器
updated_count = {
    'frontPanel': 0,
    'frameMaterial': 0,
    'backPanelMaterial': 0
}

# 处理每个iPhone型号
for phone in iphone_data:
    phone_id = phone.get('id', '')
    
    # 检查是否有CSV中的材质信息
    if phone_id in csv_materials:
        materials_str = csv_materials[phone_id]
        materials_from_csv = extract_materials_from_description(materials_str)
        
        # 更新前面板材质
        if ('frontPanel' not in phone or not phone['frontPanel'] or phone['frontPanel'] == '-') and 'frontPanel' in materials_from_csv:
            phone['frontPanel'] = materials_from_csv['frontPanel']
            updated_count['frontPanel'] += 1
            print(f"从CSV提取 {phone.get('name', phone_id)} 的前面板材质: {phone['frontPanel']}")
        
        # 更新中框材质
        if ('frameMaterial' not in phone or not phone['frameMaterial'] or phone['frameMaterial'] == '-') and 'frameMaterial' in materials_from_csv:
            phone['frameMaterial'] = materials_from_csv['frameMaterial']
            updated_count['frameMaterial'] += 1
            print(f"从CSV提取 {phone.get('name', phone_id)} 的中框材质: {phone['frameMaterial']}")
        
        # 更新背板材质
        if ('backPanelMaterial' not in phone or not phone['backPanelMaterial'] or phone['backPanelMaterial'] == '-') and 'backPanelMaterial' in materials_from_csv:
            phone['backPanelMaterial'] = materials_from_csv['backPanelMaterial']
            updated_count['backPanelMaterial'] += 1
            print(f"从CSV提取 {phone.get('name', phone_id)} 的背板材质: {phone['backPanelMaterial']}")

# 保存更新后的JSON数据
with open(json_file, 'w', encoding='utf-8') as f:
    json.dump(iphone_data, f, ensure_ascii=False, indent=2)

print(f'更新完成! 已从CSV补充 {updated_count["frontPanel"]} 个前面板材质, {updated_count["frameMaterial"]} 个中框材质, {updated_count["backPanelMaterial"]} 个背板材质')
