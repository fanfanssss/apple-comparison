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
    
    for ipad in ipad_data:
        if 'ramType' in ipad:
            original_type = ipad['ramType']
            # 提取内存类型，去除容量数字
            ram_type_match = re.search(r'(LPDDR\w+)', original_type)
            if ram_type_match:
                fixed_type = ram_type_match.group(1)
                if fixed_type != original_type:
                    ipad['ramType'] = fixed_type
                    fixed_count += 1
                    print(f"已修复: {ipad['name']} -> 内存规格: {original_type} -> {fixed_type}")
            else:
                # 如果没有找到LPDDR模式，根据处理器推断
                if 'M4' in ipad.get('processor', ''):
                    ipad['ramType'] = 'LPDDR5X'
                    fixed_count += 1
                    print(f"已推断: {ipad['name']} -> 内存规格: {original_type} -> LPDDR5X (基于 M4 处理器)")
                elif 'M3' in ipad.get('processor', ''):
                    ipad['ramType'] = 'LPDDR5'
                    fixed_count += 1
                    print(f"已推断: {ipad['name']} -> 内存规格: {original_type} -> LPDDR5 (基于 M3 处理器)")
                elif 'M2' in ipad.get('processor', ''):
                    ipad['ramType'] = 'LPDDR5'
                    fixed_count += 1
                    print(f"已推断: {ipad['name']} -> 内存规格: {original_type} -> LPDDR5 (基于 M2 处理器)")
                elif 'M1' in ipad.get('processor', ''):
                    ipad['ramType'] = 'LPDDR4X'
                    fixed_count += 1
                    print(f"已推断: {ipad['name']} -> 内存规格: {original_type} -> LPDDR4X (基于 M1 处理器)")
                elif 'A14' in ipad.get('processor', '') or 'A15' in ipad.get('processor', '') or 'A16' in ipad.get('processor', '') or 'A17' in ipad.get('processor', ''):
                    ipad['ramType'] = 'LPDDR4X'
                    fixed_count += 1
                    print(f"已推断: {ipad['name']} -> 内存规格: {original_type} -> LPDDR4X (基于 A14-A17 处理器)")
                elif 'A12' in ipad.get('processor', '') or 'A13' in ipad.get('processor', ''):
                    ipad['ramType'] = 'LPDDR4X'
                    fixed_count += 1
                    print(f"已推断: {ipad['name']} -> 内存规格: {original_type} -> LPDDR4X (基于 A12-A13 处理器)")
                elif 'A10' in ipad.get('processor', '') or 'A11' in ipad.get('processor', ''):
                    ipad['ramType'] = 'LPDDR4'
                    fixed_count += 1
                    print(f"已推断: {ipad['name']} -> 内存规格: {original_type} -> LPDDR4 (基于 A10-A11 处理器)")
                elif 'A8' in ipad.get('processor', '') or 'A9' in ipad.get('processor', ''):
                    ipad['ramType'] = 'LPDDR3'
                    fixed_count += 1
                    print(f"已推断: {ipad['name']} -> 内存规格: {original_type} -> LPDDR3 (基于 A8-A9 处理器)")
                elif 'A5' in ipad.get('processor', '') or 'A6' in ipad.get('processor', '') or 'A7' in ipad.get('processor', ''):
                    ipad['ramType'] = 'LPDDR2'
                    fixed_count += 1
                    print(f"已推断: {ipad['name']} -> 内存规格: {original_type} -> LPDDR2 (基于 A5-A7 处理器)")
                elif 'A4' in ipad.get('processor', ''):
                    ipad['ramType'] = 'LPDDR'
                    fixed_count += 1
                    print(f"已推断: {ipad['name']} -> 内存规格: {original_type} -> LPDDR (基于 A4 处理器)")
        
        # 特殊处理第一代iPad和iPad 2
        if ipad.get('id') == 'ipad-ipad':
            ipad['ramType'] = 'LPDDR'
            fixed_count += 1
            print(f"已特殊设置: {ipad['name']} -> 内存规格: LPDDR")
        elif ipad.get('id') == 'ipad-ipad-2':
            ipad['ramType'] = 'LPDDR2'
            fixed_count += 1
            print(f"已特殊设置: {ipad['name']} -> 内存规格: LPDDR2")
    
    # 保存修复后的数据
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(ipad_data, f, ensure_ascii=False, indent=2)
    
    print(f"\n总共修复了 {fixed_count} 个iPad型号的内存规格信息")

if __name__ == "__main__":
    print("开始修复iPad内存规格数据...")
    fix_ram_type()
    print("\n处理完成!")
