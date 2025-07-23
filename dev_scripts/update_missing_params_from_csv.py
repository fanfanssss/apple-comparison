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
    'displayStandardBrightness': 'screenBrightness',  # 标准亮度
    'displayHdrBrightness': 'screenBrightness',  # HDR亮度（从同一字段提取）
    'displayOutdoorBrightness': 'screenBrightness',  # 户外亮度（从同一字段提取）
    'wiredChargingSpeed': 'charging',  # 有线充电速度
    'wirelessChargingSpeed': 'wireless',  # 无线充电速度
    'bluetoothVersion': '蓝牙',  # 蓝牙版本
    'baseband': 'baseband',  # 基带芯片
    'wifiStandard': 'WiFi标准',  # WiFi标准
    'microphoneCount': '麦克风数量',  # 麦克风数量
    'speakers': '扬声器数量'  # 扬声器数量
}

# 提取亮度信息的函数
def extract_brightness(brightness_str):
    result = {}
    if not brightness_str:
        return result
    
    # 提取标准亮度
    std_match = re.search(r'标准亮度[：:]\s*(\d+)尼特', brightness_str)
    if std_match:
        result['displayStandardBrightness'] = f"{std_match.group(1)}尼特"
    
    # 提取HDR亮度
    hdr_match = re.search(r'HDR峰值亮度[：:]\s*(\d+)尼特', brightness_str)
    if hdr_match:
        result['displayHdrBrightness'] = f"{hdr_match.group(1)}尼特"
    
    # 提取户外亮度
    outdoor_match = re.search(r'户外亮度[：:]\s*(\d+)尼特', brightness_str)
    if outdoor_match:
        result['displayOutdoorBrightness'] = f"{outdoor_match.group(1)}尼特"
    
    # 如果只有一个亮度值，可能是最大亮度
    max_match = re.search(r'最大亮度[：:]\s*(\d+)尼特', brightness_str)
    if max_match and 'displayStandardBrightness' not in result:
        result['displayStandardBrightness'] = f"{max_match.group(1)}尼特"
    
    return result

# 提取充电信息的函数
def extract_charging_info(charging_str):
    result = {}
    if not charging_str:
        return result
    
    # 提取有线充电速度
    wired_match = re.search(r'最高(\d+)W有线快充', charging_str)
    if wired_match:
        result['wiredChargingSpeed'] = f"{wired_match.group(1)}W"
    
    return result

# 提取无线充电信息的函数
def extract_wireless_info(wireless_str):
    result = {}
    if not wireless_str:
        return result
    
    # 提取无线充电类型
    if "MagSafe" in wireless_str:
        result['wirelessChargingSpeed'] = "MagSafe"
    elif "Qi" in wireless_str:
        result['wirelessChargingSpeed'] = "Qi"
    
    return result

# 提取蓝牙版本的函数
def extract_bluetooth_version(bluetooth_str):
    if not bluetooth_str:
        return None
    
    # 提取蓝牙版本
    bt_match = re.search(r'蓝牙(\d+\.\d+)', bluetooth_str)
    if bt_match:
        return bt_match.group(1)
    
    return None

# 计数器
updated_count = {field: 0 for field in param_mappings.keys()}

# 处理每个iPhone型号
for phone in iphone_data:
    phone_id = phone.get('id', '')
    
    # 更新iPhone 16e的制程工艺
    if phone_id == 'iphone-16e' and ('processTechnology' not in phone or not phone['processTechnology'] or phone['processTechnology'] == '-'):
        phone['processTechnology'] = "台积电第二代3纳米"
        print(f"已更新 iPhone 16e 的制程工艺为: 台积电第二代3纳米")
    
    # 检查是否有CSV中的参数信息
    if phone_id in csv_params:
        csv_row = csv_params[phone_id]
        
        # 处理亮度信息
        if 'screenBrightness' in csv_row:
            brightness_info = extract_brightness(csv_row['screenBrightness'])
            for field, value in brightness_info.items():
                if field not in phone or not phone[field] or phone[field] == '-':
                    phone[field] = value
                    updated_count[field] += 1
                    print(f"从CSV补充 {phone.get('name', phone_id)} 的{field}: {value}")
        
        # 处理充电信息
        if 'charging' in csv_row:
            charging_info = extract_charging_info(csv_row['charging'])
            for field, value in charging_info.items():
                if field not in phone or not phone[field] or phone[field] == '-':
                    phone[field] = value
                    updated_count[field] += 1
                    print(f"从CSV补充 {phone.get('name', phone_id)} 的{field}: {value}")
        
        # 处理无线充电信息
        if 'wireless' in csv_row:
            wireless_info = extract_wireless_info(csv_row['wireless'])
            for field, value in wireless_info.items():
                if field not in phone or not phone[field] or phone[field] == '-':
                    phone[field] = value
                    updated_count[field] += 1
                    print(f"从CSV补充 {phone.get('name', phone_id)} 的{field}: {value}")
        
        # 处理蓝牙版本
        if '蓝牙' in csv_row:
            bt_version = extract_bluetooth_version(csv_row['蓝牙'])
            if bt_version and ('bluetoothVersion' not in phone or not phone['bluetoothVersion'] or phone['bluetoothVersion'] == '-'):
                phone['bluetoothVersion'] = bt_version
                updated_count['bluetoothVersion'] += 1
                print(f"从CSV补充 {phone.get('name', phone_id)} 的蓝牙版本: {bt_version}")
        
        # 处理基带芯片
        if 'baseband' in csv_row and csv_row['baseband'] and ('baseband' not in phone or not phone['baseband'] or phone['baseband'] == '-'):
            phone['baseband'] = csv_row['baseband']
            updated_count['baseband'] += 1
            print(f"从CSV补充 {phone.get('name', phone_id)} 的基带芯片: {csv_row['baseband']}")
        
        # 处理WiFi标准
        if 'WiFi标准' in csv_row and csv_row['WiFi标准'] and ('wifiStandard' not in phone or not phone['wifiStandard'] or phone['wifiStandard'] == '-'):
            phone['wifiStandard'] = csv_row['WiFi标准']
            updated_count['wifiStandard'] += 1
            print(f"从CSV补充 {phone.get('name', phone_id)} 的WiFi标准: {csv_row['WiFi标准']}")
        
        # 处理麦克风数量
        if '麦克风数量' in csv_row and csv_row['麦克风数量'] and ('microphoneCount' not in phone or not phone['microphoneCount'] or phone['microphoneCount'] == '-'):
            phone['microphoneCount'] = f"{csv_row['麦克风数量']}个麦克风"
            updated_count['microphoneCount'] += 1
            print(f"从CSV补充 {phone.get('name', phone_id)} 的麦克风数量: {csv_row['麦克风数量']}个麦克风")
        
        # 处理扬声器数量
        if '扬声器数量' in csv_row and csv_row['扬声器数量'] and ('speakers' not in phone or not phone['speakers'] or phone['speakers'] == '-'):
            phone['speakers'] = f"{csv_row['扬声器数量']}个扬声器"
            updated_count['speakers'] += 1
            print(f"从CSV补充 {phone.get('name', phone_id)} 的扬声器数量: {csv_row['扬声器数量']}个扬声器")

# 保存更新后的JSON数据
with open(json_file, 'w', encoding='utf-8') as f:
    json.dump(iphone_data, f, ensure_ascii=False, indent=2)

# 打印更新统计
print("\n更新完成!")
print(f"已更新 iPhone 16e 的制程工艺为: 台积电第二代3纳米")
for field, count in updated_count.items():
    print(f"已从CSV补充 {count} 个iPhone型号的{field}字段")
