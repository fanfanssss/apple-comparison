#!/usr/bin/env python3
import json

# 读取JSON文件
with open('public/data/ipad_refined.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 需要更新的iPad型号ID列表
ipad_ids = [
    'ipad-ipad-10',  # iPad第10代
    'ipad-ipad-9',   # iPad第9代
    'ipad-ipad-8',   # iPad第8代
    'ipad-ipad-6',   # iPad第6代
    'ipad-ipad-5'    # iPad第5代
]

# 更新计数器
updated_count = 0

# 遍历所有iPad数据
for ipad in data:
    # 仅处理指定ID的iPad
    if ipad.get('id') in ipad_ids:
        # 更新名称为双语格式
        if isinstance(ipad.get('name'), str):
            name_zh = ipad['name']
            # 提取代数数字并创建英文名称
            gen_num = ''.join(filter(str.isdigit, name_zh))
            name_en = f"iPad ({gen_num}th generation)"
            ipad['name'] = {
                'zh-CN': name_zh,
                'en-US': name_en
            }
            
        # 更新batteryLife为双语格式
        if isinstance(ipad.get('batteryLife'), str):
            battery_life_zh = ipad['batteryLife']
            # 创建英文版本
            if '蜂窝网络' in battery_life_zh:
                battery_life_en = "Wi-Fi web browsing: 10h Cellular web browsing: 9h"
            else:
                battery_life_en = "Wi-Fi web browsing: 10h"
            
            ipad['batteryLife'] = {
                'zh-CN': battery_life_zh,
                'en-US': battery_life_en
            }
            
        # 更新audioFeatures为双语格式
        if isinstance(ipad.get('audioFeatures'), str):
            audio_features_zh = ipad['audioFeatures']
            # 创建英文版本
            if '×2' in audio_features_zh:
                audio_features_en = "2 microphones + 2 speakers"
            else:
                audio_features_en = "1 microphone + 1 speaker"
                
            ipad['audioFeatures'] = {
                'zh-CN': audio_features_zh,
                'en-US': audio_features_en
            }
            
        updated_count += 1
        print(f"已更新: {ipad.get('id')} - {ipad.get('name', {}).get('zh-CN', 'Unknown')}")

print(f"总共更新了 {updated_count} 个 iPad 型号的双语字段")

# 写回JSON文件
with open('public/data/ipad_refined.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    
print("数据已保存到 public/data/ipad_refined.json")
