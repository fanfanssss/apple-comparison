#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import csv
import datetime
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

# 从CSV文件读取材质信息
csv_materials = {}
with open(csv_file, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        phone_id = row.get('ID', '')
        materials_str = row.get('materials', '')
        if phone_id and materials_str:
            # 直接解析材质字符串
            materials_info = {}
            
            # 尝试提取前面板材质
            if "前玻璃" in materials_str:
                materials_info['frontPanel'] = "玻璃"
            elif "前面板" in materials_str:
                materials_info['frontPanel'] = "玻璃"
            elif "超瓷晶面板" in materials_str:
                materials_info['frontPanel'] = "超瓷晶面板"
            elif "Ceramic Shield" in materials_str:
                materials_info['frontPanel'] = "超瓷晶面板"
            
            # 尝试提取中框材质
            if "铝合金中框" in materials_str:
                materials_info['frameMaterial'] = "铝合金"
            elif "不锈钢中框" in materials_str:
                materials_info['frameMaterial'] = "不锈钢"
            elif "钛金属中框" in materials_str:
                materials_info['frameMaterial'] = "钛金属"
            elif "塑料" in materials_str:
                materials_info['frameMaterial'] = "塑料"
            
            # 尝试提取背板材质
            if "磨砂玻璃背板" in materials_str:
                materials_info['backPanelMaterial'] = "磨砂玻璃"
            elif "玻璃背板" in materials_str:
                materials_info['backPanelMaterial'] = "玻璃"
            elif "铝合金背板" in materials_str or "铝合金后壳" in materials_str:
                materials_info['backPanelMaterial'] = "铝合金"
            elif "塑料背板" in materials_str or "塑料后壳" in materials_str:
                materials_info['backPanelMaterial'] = "塑料"
            
            csv_materials[phone_id] = materials_info

# 手动添加一些已知的材质信息
manual_materials = {
    "iphone-1": {"frontPanel": "玻璃", "frameMaterial": "铝合金", "backPanelMaterial": "铝合金"},
    "iphone-3g": {"frontPanel": "玻璃", "frameMaterial": "塑料", "backPanelMaterial": "塑料"},
    "iphone-3gs": {"frontPanel": "玻璃", "frameMaterial": "塑料", "backPanelMaterial": "塑料"},
    "iphone-4": {"frontPanel": "玻璃", "frameMaterial": "不锈钢", "backPanelMaterial": "玻璃"},
    "iphone-4s": {"frontPanel": "玻璃", "frameMaterial": "不锈钢", "backPanelMaterial": "玻璃"},
    "iphone-5": {"frontPanel": "玻璃", "frameMaterial": "铝合金", "backPanelMaterial": "铝合金"},
    "iphone-5c": {"frontPanel": "玻璃", "frameMaterial": "塑料", "backPanelMaterial": "塑料"},
    "iphone-5s": {"frontPanel": "玻璃", "frameMaterial": "铝合金", "backPanelMaterial": "铝合金"},
    "iphone-6": {"frontPanel": "玻璃", "frameMaterial": "铝合金", "backPanelMaterial": "铝合金"},
    "iphone-6-plus": {"frontPanel": "玻璃", "frameMaterial": "铝合金", "backPanelMaterial": "铝合金"},
    "iphone-6s": {"frontPanel": "玻璃", "frameMaterial": "铝合金", "backPanelMaterial": "铝合金"},
    "iphone-6s-plus": {"frontPanel": "玻璃", "frameMaterial": "铝合金", "backPanelMaterial": "铝合金"},
    "iphone-7": {"frontPanel": "玻璃", "frameMaterial": "铝合金", "backPanelMaterial": "铝合金"},
    "iphone-7-plus": {"frontPanel": "玻璃", "frameMaterial": "铝合金", "backPanelMaterial": "铝合金"},
    "iphone-8": {"frontPanel": "玻璃", "frameMaterial": "铝合金", "backPanelMaterial": "玻璃"},
    "iphone-8-plus": {"frontPanel": "玻璃", "frameMaterial": "铝合金", "backPanelMaterial": "玻璃"},
    "iphone-x": {"frontPanel": "玻璃", "frameMaterial": "不锈钢", "backPanelMaterial": "玻璃"},
    "iphone-xs": {"frontPanel": "玻璃", "frameMaterial": "不锈钢", "backPanelMaterial": "玻璃"},
    "iphone-xs-max": {"frontPanel": "玻璃", "frameMaterial": "不锈钢", "backPanelMaterial": "玻璃"},
    "iphone-xr": {"frontPanel": "玻璃", "frameMaterial": "铝合金", "backPanelMaterial": "玻璃"},
    "iphone-11": {"frontPanel": "玻璃", "frameMaterial": "铝合金", "backPanelMaterial": "玻璃"},
    "iphone-11-pro": {"frontPanel": "玻璃", "frameMaterial": "不锈钢", "backPanelMaterial": "磨砂玻璃"},
    "iphone-11-pro-max": {"frontPanel": "玻璃", "frameMaterial": "不锈钢", "backPanelMaterial": "磨砂玻璃"},
    "iphone-se-1": {"frontPanel": "玻璃", "frameMaterial": "铝合金", "backPanelMaterial": "铝合金"},
    "iphone-se-2": {"frontPanel": "玻璃", "frameMaterial": "铝合金", "backPanelMaterial": "玻璃"},
    "iphone-se-3": {"frontPanel": "玻璃", "frameMaterial": "铝合金", "backPanelMaterial": "玻璃"}
}

# 合并CSV和手动材质信息
for phone_id, materials in manual_materials.items():
    if phone_id not in csv_materials:
        csv_materials[phone_id] = materials
    else:
        # 补充CSV中缺失的字段
        for field, value in materials.items():
            if field not in csv_materials[phone_id]:
                csv_materials[phone_id][field] = value

# 计数器
updated_count = {
    'frontPanel': 0,
    'frameMaterial': 0,
    'backPanelMaterial': 0
}

# 处理每个iPhone型号
for phone in iphone_data:
    phone_id = phone.get('id', '')
    
    # 检查是否有材质信息
    if phone_id in csv_materials:
        materials_info = csv_materials[phone_id]
        
        # 更新前面板材质
        if ('frontPanel' not in phone or not phone['frontPanel'] or phone['frontPanel'] == '-') and 'frontPanel' in materials_info:
            phone['frontPanel'] = materials_info['frontPanel']
            updated_count['frontPanel'] += 1
            print(f"更新 {phone.get('name', phone_id)} 的前面板材质: {phone['frontPanel']}")
        
        # 更新中框材质
        if ('frameMaterial' not in phone or not phone['frameMaterial'] or phone['frameMaterial'] == '-') and 'frameMaterial' in materials_info:
            phone['frameMaterial'] = materials_info['frameMaterial']
            updated_count['frameMaterial'] += 1
            print(f"更新 {phone.get('name', phone_id)} 的中框材质: {phone['frameMaterial']}")
        
        # 更新背板材质
        if ('backPanelMaterial' not in phone or not phone['backPanelMaterial'] or phone['backPanelMaterial'] == '-') and 'backPanelMaterial' in materials_info:
            phone['backPanelMaterial'] = materials_info['backPanelMaterial']
            updated_count['backPanelMaterial'] += 1
            print(f"更新 {phone.get('name', phone_id)} 的背板材质: {phone['backPanelMaterial']}")

# 保存更新后的JSON数据
with open(json_file, 'w', encoding='utf-8') as f:
    json.dump(iphone_data, f, ensure_ascii=False, indent=2)

print(f'更新完成! 已补充 {updated_count["frontPanel"]} 个前面板材质, {updated_count["frameMaterial"]} 个中框材质, {updated_count["backPanelMaterial"]} 个背板材质')
