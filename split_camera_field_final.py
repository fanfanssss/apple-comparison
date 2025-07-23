#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import re
import datetime

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

# 计数器
updated_count = 0
failed_count = 0

# 处理每个iPhone型号
for phone in iphone_data:
    if 'camera' in phone:
        camera_text = phone['camera']
        updated = False
        
        # 通用模式：提取摄像头信息
        # 尝试多种可能的格式
        
        # 格式1: "主摄：4800万像素 (f/1.78光圈) + ..."
        if "主摄：" in camera_text or "主摄:" in camera_text:
            parts = re.split(r'[+＋]\s*', camera_text)
            for part in parts:
                if "主摄" in part:
                    phone['mainCamera'] = part.strip()
                    updated = True
                elif "超广角" in part:
                    phone['ultraWideCamera'] = part.strip()
                    updated = True
                elif "长焦" in part:
                    phone['telephotoCamera'] = part.strip()
                    updated = True
        
        # 格式2: "4800万像素主摄 (f/1.78光圈) + ..."
        elif "万像素主摄" in camera_text or "万像素广角" in camera_text:
            parts = re.split(r'[+＋]\s*', camera_text)
            for part in parts:
                if "主摄" in part or ("广角" in part and "超广角" not in part):
                    phone['mainCamera'] = part.strip()
                    updated = True
                elif "超广角" in part:
                    phone['ultraWideCamera'] = part.strip()
                    updated = True
                elif "长焦" in part:
                    phone['telephotoCamera'] = part.strip()
                    updated = True
        
        # 格式3: "1200万像素主摄 (f/1.8光圈)" - 单摄像头
        elif "万像素主摄" in camera_text and "+" not in camera_text and "＋" not in camera_text:
            phone['mainCamera'] = camera_text
            updated = True
        
        # 格式4: "双1200万像素主摄 (f/1.8光圈) + 长焦 (f/2.8光圈，2倍光学变焦)"
        elif "双" in camera_text and "主摄" in camera_text and "长焦" in camera_text:
            parts = camera_text.split("+")
            if len(parts) >= 1:
                phone['mainCamera'] = parts[0].strip()
                updated = True
            if len(parts) >= 2:
                phone['telephotoCamera'] = parts[1].strip()
                updated = True
        
        if updated:
            updated_count += 1
        else:
            # 如果上述模式都不匹配，使用更简单的模式
            parts = re.split(r'[+＋]\s*', camera_text)
            
            # 如果只有一个部分，假设它是主摄像头
            if len(parts) == 1:
                phone['mainCamera'] = parts[0].strip()
                updated = True
            # 如果有两个部分，假设第一个是主摄像头，第二个是超广角或长焦
            elif len(parts) == 2:
                phone['mainCamera'] = parts[0].strip()
                if "超广角" in parts[1]:
                    phone['ultraWideCamera'] = parts[1].strip()
                else:
                    phone['telephotoCamera'] = parts[1].strip()
                updated = True
            # 如果有三个部分，假设它们分别是主摄像头、超广角和长焦
            elif len(parts) == 3:
                phone['mainCamera'] = parts[0].strip()
                phone['ultraWideCamera'] = parts[1].strip()
                phone['telephotoCamera'] = parts[2].strip()
                updated = True
            
            if updated:
                updated_count += 1
            else:
                failed_count += 1
                print(f"无法解析 {phone.get('name', phone.get('id'))} 的摄像头信息: {camera_text}")

# 保存更新后的JSON数据
with open(json_file, 'w', encoding='utf-8') as f:
    json.dump(iphone_data, f, ensure_ascii=False, indent=2)

print(f'更新完成! 已为 {updated_count} 个iPhone型号拆分camera字段，{failed_count} 个型号解析失败')
