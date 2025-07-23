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

# 材质信息参考表 - 根据iPhone型号和发布年份提供默认值
material_reference = {
    # 最新型号
    "iphone-16-pro": {"frontPanel": "超瓷晶面板二代", "frameMaterial": "钛金属", "backPanelMaterial": "磨砂玻璃"},
    "iphone-16-pro-max": {"frontPanel": "超瓷晶面板二代", "frameMaterial": "钛金属", "backPanelMaterial": "磨砂玻璃"},
    "iphone-16": {"frontPanel": "超瓷晶面板二代", "frameMaterial": "铝合金", "backPanelMaterial": "玻璃"},
    "iphone-16-plus": {"frontPanel": "超瓷晶面板二代", "frameMaterial": "铝合金", "backPanelMaterial": "玻璃"},
    "iphone-16e": {"frontPanel": "超瓷晶面板", "frameMaterial": "铝合金", "backPanelMaterial": "玻璃"},
    
    # iPhone 15系列
    "iphone-15-pro": {"frontPanel": "超瓷晶面板", "frameMaterial": "钛金属", "backPanelMaterial": "磨砂玻璃"},
    "iphone-15-pro-max": {"frontPanel": "超瓷晶面板", "frameMaterial": "钛金属", "backPanelMaterial": "磨砂玻璃"},
    "iphone-15": {"frontPanel": "超瓷晶面板", "frameMaterial": "铝合金", "backPanelMaterial": "玻璃"},
    "iphone-15-plus": {"frontPanel": "超瓷晶面板", "frameMaterial": "铝合金", "backPanelMaterial": "玻璃"},
    
    # iPhone 14系列
    "iphone-14-pro": {"frontPanel": "超瓷晶面板", "frameMaterial": "不锈钢", "backPanelMaterial": "磨砂玻璃"},
    "iphone-14-pro-max": {"frontPanel": "超瓷晶面板", "frameMaterial": "不锈钢", "backPanelMaterial": "磨砂玻璃"},
    "iphone-14": {"frontPanel": "超瓷晶面板", "frameMaterial": "铝合金", "backPanelMaterial": "玻璃"},
    "iphone-14-plus": {"frontPanel": "超瓷晶面板", "frameMaterial": "铝合金", "backPanelMaterial": "玻璃"},
    
    # iPhone 13系列
    "iphone-13-pro": {"frontPanel": "超瓷晶面板", "frameMaterial": "不锈钢", "backPanelMaterial": "磨砂玻璃"},
    "iphone-13-pro-max": {"frontPanel": "超瓷晶面板", "frameMaterial": "不锈钢", "backPanelMaterial": "磨砂玻璃"},
    "iphone-13": {"frontPanel": "超瓷晶面板", "frameMaterial": "铝合金", "backPanelMaterial": "玻璃"},
    "iphone-13-mini": {"frontPanel": "超瓷晶面板", "frameMaterial": "铝合金", "backPanelMaterial": "玻璃"},
    
    # iPhone 12系列
    "iphone-12-pro": {"frontPanel": "超瓷晶面板", "frameMaterial": "不锈钢", "backPanelMaterial": "磨砂玻璃"},
    "iphone-12-pro-max": {"frontPanel": "超瓷晶面板", "frameMaterial": "不锈钢", "backPanelMaterial": "磨砂玻璃"},
    "iphone-12": {"frontPanel": "超瓷晶面板", "frameMaterial": "铝合金", "backPanelMaterial": "玻璃"},
    "iphone-12-mini": {"frontPanel": "超瓷晶面板", "frameMaterial": "铝合金", "backPanelMaterial": "玻璃"},
    
    # iPhone 11系列
    "iphone-11-pro": {"frontPanel": "玻璃", "frameMaterial": "不锈钢", "backPanelMaterial": "磨砂玻璃"},
    "iphone-11-pro-max": {"frontPanel": "玻璃", "frameMaterial": "不锈钢", "backPanelMaterial": "磨砂玻璃"},
    "iphone-11": {"frontPanel": "玻璃", "frameMaterial": "铝合金", "backPanelMaterial": "玻璃"},
    
    # iPhone X系列
    "iphone-xs": {"frontPanel": "玻璃", "frameMaterial": "不锈钢", "backPanelMaterial": "玻璃"},
    "iphone-xs-max": {"frontPanel": "玻璃", "frameMaterial": "不锈钢", "backPanelMaterial": "玻璃"},
    "iphone-xr": {"frontPanel": "玻璃", "frameMaterial": "铝合金", "backPanelMaterial": "玻璃"},
    "iphone-x": {"frontPanel": "玻璃", "frameMaterial": "不锈钢", "backPanelMaterial": "玻璃"},
    
    # iPhone 8系列
    "iphone-8": {"frontPanel": "玻璃", "frameMaterial": "铝合金", "backPanelMaterial": "玻璃"},
    "iphone-8-plus": {"frontPanel": "玻璃", "frameMaterial": "铝合金", "backPanelMaterial": "玻璃"},
    
    # iPhone 7系列
    "iphone-7": {"frontPanel": "玻璃", "frameMaterial": "铝合金", "backPanelMaterial": "铝合金"},
    "iphone-7-plus": {"frontPanel": "玻璃", "frameMaterial": "铝合金", "backPanelMaterial": "铝合金"},
    
    # iPhone 6系列
    "iphone-6s": {"frontPanel": "玻璃", "frameMaterial": "铝合金", "backPanelMaterial": "铝合金"},
    "iphone-6s-plus": {"frontPanel": "玻璃", "frameMaterial": "铝合金", "backPanelMaterial": "铝合金"},
    "iphone-6": {"frontPanel": "玻璃", "frameMaterial": "铝合金", "backPanelMaterial": "铝合金"},
    "iphone-6-plus": {"frontPanel": "玻璃", "frameMaterial": "铝合金", "backPanelMaterial": "铝合金"},
    
    # iPhone SE系列
    "iphone-se-3": {"frontPanel": "玻璃", "frameMaterial": "铝合金", "backPanelMaterial": "玻璃"},
    "iphone-se-2": {"frontPanel": "玻璃", "frameMaterial": "铝合金", "backPanelMaterial": "玻璃"},
    "iphone-se-1": {"frontPanel": "玻璃", "frameMaterial": "铝合金", "backPanelMaterial": "铝合金"},
    
    # 早期iPhone
    "iphone-5s": {"frontPanel": "玻璃", "frameMaterial": "铝合金", "backPanelMaterial": "铝合金"},
    "iphone-5c": {"frontPanel": "玻璃", "frameMaterial": "塑料", "backPanelMaterial": "塑料"},
    "iphone-5": {"frontPanel": "玻璃", "frameMaterial": "铝合金", "backPanelMaterial": "铝合金"},
    "iphone-4s": {"frontPanel": "玻璃", "frameMaterial": "不锈钢", "backPanelMaterial": "玻璃"},
    "iphone-4": {"frontPanel": "玻璃", "frameMaterial": "不锈钢", "backPanelMaterial": "玻璃"},
    "iphone-3gs": {"frontPanel": "玻璃", "frameMaterial": "塑料", "backPanelMaterial": "塑料"},
    "iphone-3g": {"frontPanel": "玻璃", "frameMaterial": "塑料", "backPanelMaterial": "塑料"},
    "iphone-1": {"frontPanel": "玻璃", "frameMaterial": "铝合金", "backPanelMaterial": "铝合金"}
}

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
    
    # 尝试从materials字段提取材质信息
    materials_from_desc = {}
    if 'materials' in phone and phone['materials']:
        materials_from_desc = extract_materials_from_description(phone['materials'])
    
    # 获取参考材质信息
    reference_materials = material_reference.get(phone_id, {})
    
    # 补充前面板材质
    if ('frontPanel' not in phone or not phone['frontPanel'] or phone['frontPanel'] == '-'):
        if 'frontPanel' in materials_from_desc:
            phone['frontPanel'] = materials_from_desc['frontPanel']
            updated_count['frontPanel'] += 1
            print(f"从materials字段提取 {phone.get('name', phone_id)} 的前面板材质: {phone['frontPanel']}")
        elif phone_id in reference_materials and 'frontPanel' in reference_materials:
            phone['frontPanel'] = reference_materials['frontPanel']
            updated_count['frontPanel'] += 1
            print(f"为 {phone.get('name', phone_id)} 添加前面板材质: {phone['frontPanel']}")
    
    # 补充中框材质
    if ('frameMaterial' not in phone or not phone['frameMaterial'] or phone['frameMaterial'] == '-'):
        if 'frameMaterial' in materials_from_desc:
            phone['frameMaterial'] = materials_from_desc['frameMaterial']
            updated_count['frameMaterial'] += 1
            print(f"从materials字段提取 {phone.get('name', phone_id)} 的中框材质: {phone['frameMaterial']}")
        elif phone_id in reference_materials and 'frameMaterial' in reference_materials:
            phone['frameMaterial'] = reference_materials['frameMaterial']
            updated_count['frameMaterial'] += 1
            print(f"为 {phone.get('name', phone_id)} 添加中框材质: {phone['frameMaterial']}")
    
    # 补充背板材质
    if ('backPanelMaterial' not in phone or not phone['backPanelMaterial'] or phone['backPanelMaterial'] == '-'):
        if 'backPanelMaterial' in materials_from_desc:
            phone['backPanelMaterial'] = materials_from_desc['backPanelMaterial']
            updated_count['backPanelMaterial'] += 1
            print(f"从materials字段提取 {phone.get('name', phone_id)} 的背板材质: {phone['backPanelMaterial']}")
        elif phone_id in reference_materials and 'backPanelMaterial' in reference_materials:
            phone['backPanelMaterial'] = reference_materials['backPanelMaterial']
            updated_count['backPanelMaterial'] += 1
            print(f"为 {phone.get('name', phone_id)} 添加背板材质: {phone['backPanelMaterial']}")

# 保存更新后的JSON数据
with open(json_file, 'w', encoding='utf-8') as f:
    json.dump(iphone_data, f, ensure_ascii=False, indent=2)

print(f'更新完成! 已补充 {updated_count["frontPanel"]} 个前面板材质, {updated_count["frameMaterial"]} 个中框材质, {updated_count["backPanelMaterial"]} 个背板材质')
