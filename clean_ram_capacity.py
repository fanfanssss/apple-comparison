#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import re

def clean_ram_capacity():
    """清理iPad JSON文件中的内存容量信息，只保留容量数值，去除LPDDR相关信息"""
    json_file = '/Users/aron/CascadeProjects/apple-comparison/public/data/ipad_refined.json'
    
    with open(json_file, 'r', encoding='utf-8') as f:
        ipad_data = json.load(f)
    
    cleaned_count = 0
    
    for ipad in ipad_data:
        if 'ram' in ipad and isinstance(ipad['ram'], list) and ipad['ram']:
            cleaned_values = []
            
            for ram_value in ipad['ram']:
                # 先检查是否包含LPDDR相关信息
                if 'LPDDR' in ram_value:
                    # 提取容量部分
                    capacity_match = re.search(r'(\d+(?:\.\d+)?)\s*(MB|GB|TB)', ram_value, re.IGNORECASE)
                    if capacity_match:
                        capacity = capacity_match.group(1) + capacity_match.group(2)
                        cleaned_values.append(capacity)
                        print(f"已清理: {ram_value} -> {capacity}")
                    else:
                        # 如果没有找到容量，保留原值
                        cleaned_values.append(ram_value)
                else:
                    # 如果不包含LPDDR，保留原值
                    cleaned_values.append(ram_value)
            
            if cleaned_values != ipad['ram']:
                ipad['ram'] = cleaned_values
                cleaned_count += 1
                print(f"已更新 {ipad['name']} 的内存容量: {ipad['ram']}")
    
    # 保存清理后的数据
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(ipad_data, f, ensure_ascii=False, indent=2)
    
    print(f"\n总共清理了 {cleaned_count} 个iPad型号的内存容量信息")

if __name__ == "__main__":
    print("开始清理iPad内存容量数据...")
    clean_ram_capacity()
    print("\n处理完成!")
