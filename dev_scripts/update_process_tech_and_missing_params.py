#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import csv
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

# 更新iPhone 16e的制程工艺
iphone16e_updated = False
for phone in iphone_data:
    if phone.get('id') == 'iphone-16e':
        phone['processTechnology'] = "台积电第二代3纳米"
        iphone16e_updated = True
        print(f"已更新 iPhone 16e 的制程工艺为: 台积电第二代3纳米")
        break

if not iphone16e_updated:
    print("未找到 iPhone 16e 型号")

# 从CSV文件读取参数信息
csv_params = {}
with open(csv_file, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        phone_id = row.get('ID', '')
        if phone_id:
            csv_params[phone_id] = row

# 需要从CSV补充的参数字段映射
param_mappings = {
    'processTechnology': 'process',  # 制程工艺
    'displayStandardBrightness': 'brightness',  # 标准亮度
    'displayHdrBrightness': 'hdr_brightness',  # HDR亮度
    'displayOutdoorBrightness': 'outdoor_brightness',  # 户外亮度
    'wiredChargingSpeed': 'wired_charging',  # 有线充电速度
    'wirelessChargingSpeed': 'wireless_charging',  # 无线充电速度
    'bluetoothVersion': 'bluetooth',  # 蓝牙版本
    'baseband': 'baseband'  # 基带芯片
}

# 计数器
updated_count = {field: 0 for field in param_mappings.keys()}

# 处理每个iPhone型号
for phone in iphone_data:
    phone_id = phone.get('id', '')
    
    # 检查是否有CSV中的参数信息
    if phone_id in csv_params:
        csv_row = csv_params[phone_id]
        
        # 遍历需要补充的参数
        for json_field, csv_field in param_mappings.items():
            # 检查JSON中是否缺失该字段或为空值
            if (json_field not in phone or not phone[json_field] or phone[json_field] == '-') and csv_field in csv_row and csv_row[csv_field]:
                phone[json_field] = csv_row[csv_field]
                updated_count[json_field] += 1
                print(f"从CSV补充 {phone.get('name', phone_id)} 的{json_field}: {csv_row[csv_field]}")

# 保存更新后的JSON数据
with open(json_file, 'w', encoding='utf-8') as f:
    json.dump(iphone_data, f, ensure_ascii=False, indent=2)

# 打印更新统计
print("\n更新完成!")
print(f"已更新 iPhone 16e 的制程工艺" if iphone16e_updated else "未找到 iPhone 16e 型号")
for field, count in updated_count.items():
    print(f"已从CSV补充 {count} 个iPhone型号的{field}字段")
