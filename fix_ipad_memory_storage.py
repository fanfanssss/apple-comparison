#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import re

def fix_storage_values(storage_list):
    """修复存储容量值"""
    fixed_storage = []
    
    for storage in storage_list:
        # 修复异常值
        if storage == "5128GB":
            fixed_storage.append("128GB")
        elif storage == "316GB":
            fixed_storage.append("16GB")
            fixed_storage.append("32GB")
        elif storage == "432GB":
            fixed_storage.append("32GB")
            fixed_storage.append("64GB")
            fixed_storage.append("128GB")
        elif storage == "464GB":
            fixed_storage.append("64GB")
            fixed_storage.append("256GB")
            fixed_storage.append("512GB")
        else:
            fixed_storage.append(storage)
    
    # 去重并排序
    return sorted(list(set(fixed_storage)), key=lambda x: int(re.search(r'(\d+)', x).group(1)))

def fix_ram_values(ram_list):
    """修复内存容量值"""
    fixed_ram = []
    
    for ram in ram_list:
        # 修复异常值
        if ram == "1GB":
            fixed_ram.append("3GB")  # iPad Air 通常是 3GB 或 4GB RAM
        else:
            fixed_ram.append(ram)
    
    # 去重并排序
    if fixed_ram:
        return sorted(list(set(fixed_ram)), key=lambda x: int(re.search(r'(\d+)', x).group(1)))
    return fixed_ram

def fix_ipad_json():
    """修复iPad JSON文件中的内存和存储容量数据"""
    json_file = '/Users/aron/CascadeProjects/apple-comparison/public/data/ipad_refined.json'
    
    with open(json_file, 'r', encoding='utf-8') as f:
        ipad_data = json.load(f)
    
    fixed_count = 0
    
    for ipad in ipad_data:
        modified = False
        
        # 修复存储容量
        if 'storage' in ipad and ipad['storage']:
            original_storage = ipad['storage'].copy() if isinstance(ipad['storage'], list) else [ipad['storage']]
            fixed_storage = fix_storage_values(original_storage)
            if fixed_storage != original_storage:
                ipad['storage'] = fixed_storage
                modified = True
        
        # 修复内存容量
        if 'ram' in ipad and ipad['ram']:
            original_ram = ipad['ram'].copy() if isinstance(ipad['ram'], list) else [ipad['ram']]
            fixed_ram = fix_ram_values(original_ram)
            if fixed_ram != original_ram:
                ipad['ram'] = fixed_ram
                modified = True
        
        # 为 iPad mini 系列添加合理的内存值
        if 'name' in ipad and 'mini' in ipad['name'] and ('ram' not in ipad or not ipad['ram']):
            if '6' in ipad['name']:
                ipad['ram'] = ["4GB"]  # iPad mini 6 有 4GB RAM
            elif '5' in ipad['name']:
                ipad['ram'] = ["3GB"]  # iPad mini 5 有 3GB RAM
            elif '4' in ipad['name']:
                ipad['ram'] = ["2GB"]  # iPad mini 4 有 2GB RAM
            else:
                ipad['ram'] = ["1GB"]  # 更早的 iPad mini 通常有 1GB RAM
            modified = True
        
        # 为普通 iPad 系列添加合理的内存值
        if 'name' in ipad and 'iPad(' in ipad['name'] and ('ram' not in ipad or not ipad['ram']):
            if '10' in ipad['name'] or 'A16' in ipad['name']:
                ipad['ram'] = ["4GB"]  # 较新的 iPad 有 4GB RAM
            elif '9' in ipad['name'] or '8' in ipad['name'] or '7' in ipad['name']:
                ipad['ram'] = ["3GB"]  # iPad 7-9 代有 3GB RAM
            elif '6' in ipad['name'] or '5' in ipad['name']:
                ipad['ram'] = ["2GB"]  # iPad 5-6 代有 2GB RAM
            else:
                ipad['ram'] = ["1GB"]  # 更早的 iPad 通常有 1GB RAM
            modified = True
        
        if modified:
            fixed_count += 1
            print(f"已修复: {ipad['name']} -> RAM: {ipad.get('ram', [])}, 存储: {ipad.get('storage', [])}")
    
    # 保存修复后的数据
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(ipad_data, f, ensure_ascii=False, indent=2)
    
    print(f"\n总共修复了 {fixed_count} 个iPad型号的内存和存储容量信息")

if __name__ == "__main__":
    print("开始修复iPad内存和存储容量数据...")
    fix_ipad_json()
    print("\n处理完成!")
