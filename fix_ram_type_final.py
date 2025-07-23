#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import re

def fix_ram_type():
    """修复iPad JSON文件中的内存规格信息，只保留类型（如LPDDR5X）"""
    json_file = '/Users/aron/CascadeProjects/apple-comparison/public/data/ipad_refined.json'
    
    with open(json_file, 'r', encoding='utf-8') as f:
        ipad_data = json.load(f)
    
    fixed_count = 0
    
    # 内存类型映射表
    ram_type_map = {
        'M4': 'LPDDR5X',
        'M3': 'LPDDR5',
        'M2': 'LPDDR5',
        'M1': 'LPDDR4X',
        'A17': 'LPDDR5',
        'A16': 'LPDDR5',
        'A15': 'LPDDR4X',
        'A14': 'LPDDR4X',
        'A13': 'LPDDR4X',
        'A12': 'LPDDR4X',
        'A11': 'LPDDR4',
        'A10': 'LPDDR4',
        'A9': 'LPDDR3',
        'A8': 'LPDDR3',
        'A7': 'LPDDR2',
        'A6': 'LPDDR2',
        'A5': 'LPDDR2',
        'A4': 'LPDDR'
    }
    
    for ipad in ipad_data:
        if 'ramType' in ipad:
            original_type = ipad['ramType']
            
            # 提取内存类型，只保留LPDDR部分和X后缀
            if 'LPDDR5X' in original_type:
                fixed_type = 'LPDDR5X'
            elif 'LPDDR5' in original_type:
                fixed_type = 'LPDDR5'
            elif 'LPDDR4X' in original_type:
                fixed_type = 'LPDDR4X'
            elif 'LPDDR4' in original_type:
                fixed_type = 'LPDDR4'
            elif 'LPDDR3' in original_type:
                fixed_type = 'LPDDR3'
            elif 'LPDDR2' in original_type:
                fixed_type = 'LPDDR2'
            elif 'LPDDR' in original_type:
                fixed_type = 'LPDDR'
            else:
                # 如果无法从ramType中提取，尝试从处理器推断
                processor = ipad.get('processor', '')
                fixed_type = None
                
                for chip, ram_type in ram_type_map.items():
                    if chip in processor:
                        fixed_type = ram_type
                        break
                
                if not fixed_type:
                    # 默认值
                    fixed_type = 'LPDDR'
            
            if fixed_type != original_type:
                ipad['ramType'] = fixed_type
                fixed_count += 1
                print(f"已修复: {ipad['name']} -> 内存规格: {original_type} -> {fixed_type}")
        else:
            # 如果没有ramType字段，根据处理器推断
            processor = ipad.get('processor', '')
            fixed_type = None
            
            for chip, ram_type in ram_type_map.items():
                if chip in processor:
                    fixed_type = ram_type
                    break
            
            if fixed_type:
                ipad['ramType'] = fixed_type
                fixed_count += 1
                print(f"已添加: {ipad['name']} -> 内存规格: {fixed_type} (基于处理器)")
    
    # 保存修复后的数据
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(ipad_data, f, ensure_ascii=False, indent=2)
    
    print(f"\n总共修复了 {fixed_count} 个iPad型号的内存规格信息")

if __name__ == "__main__":
    print("开始修复iPad内存规格数据...")
    fix_ram_type()
    print("\n处理完成!")
