#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import os
import re

def fix_ipad_memory_specs():
    """修复iPad mini和iPad Standard系列的内存规格、内存容量和存储容量信息"""
    
    # 读取JSON文件
    json_file = '/Users/aron/CascadeProjects/apple-comparison/public/data/ipad_refined.json'
    
    with open(json_file, 'r', encoding='utf-8') as f:
        ipad_data = json.load(f)
    
    # 定义正确的内存信息
    memory_specs = {
        # iPad mini 系列
        "iPad mini(A17 Pro)": {"ram": "8GB", "ramType": "LPDDR5", "storage": ["128GB", "256GB", "512GB"]},
        "iPad mini(第 6 代)": {"ram": "4GB", "ramType": "LPDDR4X", "storage": ["64GB", "256GB"]},
        "iPad mini(第 5 代)": {"ram": "3GB", "ramType": "LPDDR4X", "storage": ["64GB", "256GB"]},
        "iPad mini 4": {"ram": "2GB", "ramType": "LPDDR3", "storage": ["16GB", "32GB", "64GB", "128GB"]},
        "iPad mini 3": {"ram": "1GB", "ramType": "LPDDR3", "storage": ["16GB", "64GB", "128GB"]},
        "iPad mini 2": {"ram": "1GB", "ramType": "LPDDR3", "storage": ["16GB", "32GB", "64GB", "128GB"]},
        "iPad mini": {"ram": "512MB", "ramType": "DDR2", "storage": ["16GB", "32GB", "64GB"]},
        
        # iPad Standard 系列
        "iPad(A16)": {"ram": "6GB", "ramType": "LPDDR5", "storage": ["128GB", "256GB", "512GB"]},
        "iPad(第 10 代)": {"ram": "4GB", "ramType": "LPDDR4X", "storage": ["64GB", "256GB"]},
        "iPad(第 9 代)": {"ram": "3GB", "ramType": "LPDDR4X", "storage": ["64GB", "256GB"]},
        "iPad(第 8 代)": {"ram": "3GB", "ramType": "LPDDR4X", "storage": ["32GB", "128GB"]},
        "iPad(第 7 代)": {"ram": "3GB", "ramType": "LPDDR4", "storage": ["32GB", "128GB"]},
        "iPad(第 6 代)": {"ram": "2GB", "ramType": "LPDDR4", "storage": ["32GB", "128GB"]},
        "iPad(第 5 代)": {"ram": "2GB", "ramType": "LPDDR4", "storage": ["32GB", "128GB"]},
        "iPad(第 4 代)": {"ram": "1GB", "ramType": "LPDDR2", "storage": ["16GB", "32GB", "64GB", "128GB"]},
        "iPad(第 3 代)": {"ram": "1GB", "ramType": "LPDDR2", "storage": ["16GB", "32GB", "64GB"]},
        "iPad 2": {"ram": "512MB", "ramType": "DDR2", "storage": ["16GB", "32GB", "64GB"]},
        "iPad": {"ram": "256MB", "ramType": "DDR", "storage": ["16GB", "32GB", "64GB"]}
    }
    
    updated_count = 0
    mini_count = 0
    standard_count = 0
    
    # 遍历所有iPad型号
    for ipad in ipad_data:
        ipad_name = ipad['name']
        
        # 检查是否是需要更新的型号
        for model_name, specs in memory_specs.items():
            # 精确匹配iPad mini系列
            if ('iPad mini' in ipad_name and 'iPad mini' in model_name) and (
                (model_name == ipad_name) or
                ('A17 Pro' in model_name and 'A17 Pro' in ipad_name) or
                ('第 6 代' in model_name and '第 6 代' in ipad_name) or
                ('第 5 代' in model_name and '第 5 代' in ipad_name) or
                ('mini 4' in model_name and 'mini 4' in ipad_name) or
                ('mini 3' in model_name and 'mini 3' in ipad_name) or
                ('mini 2' in model_name and 'mini 2' in ipad_name) or
                (model_name == 'iPad mini' and ipad_name == 'iPad mini')
            ):
                # 更新内存容量
                if 'ram' in specs:
                    ipad['ram'] = specs['ram']
                
                # 更新内存类型
                if 'ramType' in specs:
                    ipad['ramType'] = specs['ramType']
                
                # 更新存储容量选项
                if 'storage' in specs:
                    ipad['storage'] = specs['storage']
                
                updated_count += 1
                mini_count += 1
                print(f"已更新 iPad mini 系列: {ipad_name}")
                print(f"  - 内存容量: {specs['ram']}")
                print(f"  - 内存类型: {specs['ramType']}")
                print(f"  - 存储选项: {', '.join(specs['storage'])}")
                break
            
            # 精确匹配iPad Standard系列
            elif ('iPad mini' not in ipad_name and 'iPad Air' not in ipad_name and 'iPad Pro' not in ipad_name) and (
                'iPad' in ipad_name and 'iPad' in model_name
            ) and (
                (model_name == ipad_name) or
                ('A16' in model_name and 'A16' in ipad_name) or
                ('第 10 代' in model_name and '第 10 代' in ipad_name) or
                ('第 9 代' in model_name and '第 9 代' in ipad_name) or
                ('第 8 代' in model_name and '第 8 代' in ipad_name) or
                ('第 7 代' in model_name and '第 7 代' in ipad_name) or
                ('第 6 代' in model_name and '第 6 代' in ipad_name) or
                ('第 5 代' in model_name and '第 5 代' in ipad_name) or
                ('第 4 代' in model_name and '第 4 代' in ipad_name) or
                ('第 3 代' in model_name and '第 3 代' in ipad_name) or
                ('iPad 2' in model_name and 'iPad 2' in ipad_name) or
                (model_name == 'iPad' and ipad_name == 'iPad')
            ):
                # 更新内存容量
                if 'ram' in specs:
                    ipad['ram'] = specs['ram']
                
                # 更新内存类型
                if 'ramType' in specs:
                    ipad['ramType'] = specs['ramType']
                
                # 更新存储容量选项
                if 'storage' in specs:
                    ipad['storage'] = specs['storage']
                
                updated_count += 1
                standard_count += 1
                print(f"已更新 iPad Standard 系列: {ipad_name}")
                print(f"  - 内存容量: {specs['ram']}")
                print(f"  - 内存类型: {specs['ramType']}")
                print(f"  - 存储选项: {', '.join(specs['storage'])}")
                break
    
    # 保存更新后的数据
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(ipad_data, f, ensure_ascii=False, indent=2)
    
    print(f"\n总共更新了 {updated_count} 个iPad型号的内存信息")
    print(f"其中 iPad mini 系列: {mini_count} 个")
    print(f"其中 iPad Standard 系列: {standard_count} 个")

if __name__ == "__main__":
    print("开始修复iPad mini和iPad Standard系列的内存规格、内存容量和存储容量信息...\n")
    fix_ipad_memory_specs()
    print("\n处理完成!")
