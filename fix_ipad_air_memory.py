#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import os
import re

def fix_ipad_air_memory():
    """修复iPad Air系列的内存容量和内存规格信息"""
    
    # 读取JSON文件
    json_file = '/Users/aron/CascadeProjects/apple-comparison/public/data/ipad_refined.json'
    
    with open(json_file, 'r', encoding='utf-8') as f:
        ipad_data = json.load(f)
    
    # 定义正确的内存信息
    memory_specs = {
        "iPad Air 13 英寸(M3)": {"ram": "8GB", "ramType": "LPDDR5", "storage": ["128GB", "256GB", "512GB", "1TB"]},
        "iPad Air 11 英寸(M3)": {"ram": "8GB", "ramType": "LPDDR5", "storage": ["128GB", "256GB", "512GB", "1TB"]},
        "iPad Air 13 英寸(M2)": {"ram": "8GB", "ramType": "LPDDR5", "storage": ["128GB", "256GB", "512GB", "1TB"]},
        "iPad Air 11 英寸(M2)": {"ram": "8GB", "ramType": "LPDDR5", "storage": ["128GB", "256GB", "512GB", "1TB"]},
        "iPad Air(第 5 代)": {"ram": "8GB", "ramType": "LPDDR4X", "storage": ["64GB", "256GB"]},
        "iPad Air(第 4 代)": {"ram": "4GB", "ramType": "LPDDR4X", "storage": ["64GB", "256GB"]},
        "iPad Air(第 3 代)": {"ram": "3GB", "ramType": "LPDDR4X", "storage": ["64GB", "256GB"]},
        "iPad Air 2": {"ram": "2GB", "ramType": "LPDDR3", "storage": ["16GB", "32GB", "64GB", "128GB"]},
        "iPad Air": {"ram": "1GB", "ramType": "LPDDR3", "storage": ["16GB", "32GB", "64GB", "128GB"]}
    }
    
    updated_count = 0
    
    # 遍历所有iPad型号
    for ipad in ipad_data:
        ipad_name = ipad['name']
        
        # 只处理iPad Air系列
        if not ('iPad Air' in ipad_name or 'iPad air' in ipad_name):
            continue
            
        # 检查是否是需要更新的型号
        for model_name, specs in memory_specs.items():
            # 使用精确匹配，避免错误更新
            if model_name == ipad_name or (
                # 处理可能的名称变体
                (model_name in ipad_name and 
                 ('M3' in model_name and 'M3' in ipad_name) or
                 ('M2' in model_name and 'M2' in ipad_name) or
                 ('第 5 代' in model_name and '第 5 代' in ipad_name) or
                 ('第 4 代' in model_name and '第 4 代' in ipad_name) or
                 ('第 3 代' in model_name and '第 3 代' in ipad_name) or
                 ('Air 2' in model_name and 'Air 2' in ipad_name) or
                 (model_name == 'iPad Air' and ipad_name == 'iPad Air')
                )
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
                print(f"已更新: {ipad_name}")
                print(f"  - 内存容量: {specs['ram']}")
                print(f"  - 内存类型: {specs['ramType']}")
                print(f"  - 存储选项: {', '.join(specs['storage'])}")
                break
    
    # 保存更新后的数据
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(ipad_data, f, ensure_ascii=False, indent=2)
    
    print(f"\n总共更新了 {updated_count} 个iPad Air型号的内存信息")

if __name__ == "__main__":
    print("开始修复iPad Air系列的内存容量和内存规格信息...\n")
    fix_ipad_air_memory()
    print("\n处理完成!")
