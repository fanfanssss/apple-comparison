#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv
import json
import datetime
import os
import re

# 文件路径
csv_file = 'iPhone数据表.csv'
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

# 创建ID到JSON对象的映射
iphone_map = {phone['id']: phone for phone in iphone_data}

# 读取CSV数据
updated_count = 0
with open(csv_file, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        iphone_id = row['ID']
        
        if iphone_id in iphone_map:
            phone = iphone_map[iphone_id]
            updated = False
            
            # 1. 芯片性能数据
            if 'chipPerformance' in row and row['chipPerformance']:
                # 提取单核和多核跑分
                single_core_match = re.search(r'单核跑分[：:]\s*(\d+)', row['chipPerformance'])
                multi_core_match = re.search(r'多核跑分[：:]\s*(\d+)', row['chipPerformance'])
                
                if not 'cpuPerformance' in phone:
                    phone['cpuPerformance'] = {}
                
                if single_core_match:
                    phone['cpuPerformance']['singleCore'] = single_core_match.group(1)
                    updated = True
                
                if multi_core_match:
                    phone['cpuPerformance']['multiCore'] = multi_core_match.group(1)
                    updated = True
            
            # 2. GPU性能
            if 'gpuPerformance' in row and row['gpuPerformance'] and not phone.get('gpuPerformance'):
                phone['gpuPerformance'] = row['gpuPerformance']
                updated = True
            
            # 3. 充电信息
            if 'charging' in row and row['charging']:
                # 提取有线充电速度
                wired_match = re.search(r'(\d+W)有线', row['charging'])
                if wired_match and not phone.get('wiredChargingSpeed'):
                    phone['wiredChargingSpeed'] = wired_match.group(1)
                    updated = True
                
                # 提取无线充电速度
                wireless_match = re.search(r'(\d+W)\s*MagSafe|(\d+W)\s*Qi', row['charging'])
                if wireless_match and not phone.get('wirelessChargingSpeed'):
                    phone['wirelessChargingSpeed'] = wireless_match.group(1) or wireless_match.group(2)
                    updated = True
            
            # 4. 无线充电技术
            if 'wireless' in row and row['wireless']:
                if not phone.get('wirelessChargingTech'):
                    phone['wirelessChargingTech'] = row['wireless']
                    updated = True
            
            # 5. 材料信息
            if 'materials' in row and row['materials'] and not phone.get('materials'):
                phone['materials'] = row['materials']
                updated = True
            
            # 6. 卫星功能
            if 'satelliteFeatures' in row and row['satelliteFeatures'] and not phone.get('satelliteFeatures'):
                phone['satelliteFeatures'] = row['satelliteFeatures']
                updated = True
            
            # 7. 基带芯片
            if 'baseband' in row and row['baseband'] and not phone.get('baseband'):
                phone['baseband'] = row['baseband']
                updated = True
            
            # 8. 营销口号
            if 'marketingSlogan' in row and row['marketingSlogan'] and not phone.get('marketingSlogan'):
                phone['marketingSlogan'] = row['marketingSlogan']
                updated = True
            
            # 9. 技术规格链接
            if 'techSpecs' in row and row['techSpecs'] and not phone.get('technicalSpecsLink'):
                phone['technicalSpecsLink'] = row['techSpecs']
                updated = True
            
            # 10. 防水等级
            if 'waterResistance' in row and row['waterResistance'] and not phone.get('waterResistance'):
                phone['waterResistance'] = row['waterResistance']
                updated = True
            
            # 11. 安全功能
            if 'security' in row and row['security'] and not phone.get('security'):
                phone['security'] = row['security']
                updated = True
            
            # 12. 传感器
            if 'sensors' in row and row['sensors'] and not phone.get('sensors'):
                phone['sensors'] = row['sensors']
                updated = True
            
            # 13. 接口类型
            if 'ports' in row and row['ports'] and not phone.get('ports'):
                phone['ports'] = row['ports']
                updated = True
            
            # 14. 音频功能
            if 'audioFeatures' in row and row['audioFeatures'] and not phone.get('audioFeatures'):
                phone['audioFeatures'] = row['audioFeatures']
                updated = True
            
            # 15. 视频播放时间
            if 'batteryLife' in row and row['batteryLife']:
                video_match = re.search(r'视频播放[：:]\s*最长(\d+)小时', row['batteryLife'])
                if video_match and not phone.get('videoPlaybackTime'):
                    phone['videoPlaybackTime'] = f"{video_match.group(1)}小时"
                    updated = True
                
                # 音频播放时间
                audio_match = re.search(r'音频播放[：:]\s*最长(\d+)小时', row['batteryLife'])
                if audio_match and not phone.get('audioPlaybackTime'):
                    phone['audioPlaybackTime'] = f"{audio_match.group(1)}小时"
                    updated = True
            
            if updated:
                updated_count += 1

# 保存更新后的JSON数据
with open(json_file, 'w', encoding='utf-8') as f:
    json.dump(iphone_data, f, ensure_ascii=False, indent=2)

print(f'更新完成! 已更新 {updated_count} 个iPhone型号的缺失参数信息')
