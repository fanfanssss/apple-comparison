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
            # 匹配如 LPDDR5X256G, LPDDR4X64, LPDDR432G 等格式
            ram_type_match = re.match(r'(LPDDR\d*X?)', original_type)
            
            if ram_type_match:
                fixed_type = ram_type_match.group(1)
                if fixed_type != original_type:
                    ipad['ramType'] = fixed_type
                    fixed_count += 1
                    print(f"已修复: {ipad['name']} -> 内存规格: {original_type} -> {fixed_type}")
    
    # 保存修复后的数据
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(ipad_data, f, ensure_ascii=False, indent=2)
    
    print(f"\n总共修复了 {fixed_count} 个iPad型号的内存规格信息")

if __name__ == "__main__":
    print("开始修复iPad内存规格数据...")
    fix_ram_type()
    print("\n处理完成!")
