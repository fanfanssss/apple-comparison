#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import os
import re

def fix_all_tech_specs_links():
    """修复所有iPad型号的技术规格链接"""
    
    # 读取JSON文件
    json_file = '/Users/aron/CascadeProjects/apple-comparison/public/data/ipad_refined.json'
    
    with open(json_file, 'r', encoding='utf-8') as f:
        ipad_data = json.load(f)
    
    # 定义已知正确的链接
    correct_links = {
        # iPad Pro 型号
        "iPad Pro 13 英寸(M4)": "https://support.apple.com/zh-cn/119891",
        "iPad Pro 11 英寸(M4)": "https://support.apple.com/zh-cn/119892",
        "iPad Pro 12.9 英寸(第 6 代)": "https://support.apple.com/zh-cn/111841",
        "iPad Pro 11 英寸(第 4 代)": "https://support.apple.com/zh-cn/111842",
        "iPad Pro 12.9 英寸(第 5 代)": "https://support.apple.com/zh-cn/111896",
        "iPad Pro 11 英寸(第 3 代)": "https://support.apple.com/zh-cn/111897",
        "iPad Pro 12.9 英寸(第 4 代)": "https://support.apple.com/zh-cn/111977",
        "iPad Pro 11 英寸(第 2 代)": "https://support.apple.com/zh-cn/118452",
        "iPad Pro 12.9 英寸(第 3 代)": "https://support.apple.com/zh-cn/111979",
        "iPad Pro 11 英寸(第 1 代)": "https://support.apple.com/zh-cn/111974",
        "iPad Pro 12.9 英寸(第 2 代)": "https://support.apple.com/zh-cn/111964",
        "iPad Pro 10.5 英寸": "https://support.apple.com/zh-cn/111927",
        "iPad Pro 9.7 英寸": "https://support.apple.com/zh-cn/111965",
        "iPad Pro 12.9 英寸": "https://support.apple.com/zh-cn/112024",
        
        # iPad Air 型号
        "iPad Air 13 英寸(M3)": "https://support.apple.com/zh-cn/122242",
        "iPad Air 11 英寸(M3)": "https://support.apple.com/zh-cn/122241",
        "iPad Air 13 英寸(M2)": "https://support.apple.com/zh-cn/119893",
        "iPad Air 11 英寸(M2)": "https://support.apple.com/zh-cn/119894",
        "iPad Air(第 5 代)": "https://support.apple.com/zh-cn/111887",
        "iPad Air(第 4 代)": "https://support.apple.com/zh-cn/111905",
        "iPad Air(第 3 代)": "https://support.apple.com/zh-cn/111939",
        "iPad Air 2": "https://support.apple.com/zh-cn/112017",
        "iPad Air": "https://support.apple.com/zh-cn/112020",
        
        # iPad mini 型号
        "iPad mini(A17 Pro)": "https://support.apple.com/zh-cn/121456",
        "iPad mini(第 6 代)": "https://support.apple.com/zh-cn/111886",
        "iPad mini(第 5 代)": "https://support.apple.com/zh-cn/111904",
        "iPad mini 4": "https://support.apple.com/zh-cn/112002",
        "iPad mini 3": "https://support.apple.com/zh-cn/112018",
        "iPad mini 2": "https://support.apple.com/zh-cn/112019",
        "iPad mini": "https://support.apple.com/zh-cn/111978",
        
        # 标准 iPad 型号
        "iPad(A16)": "https://support.apple.com/zh-cn/122240",
        "iPad(第 10 代)": "https://support.apple.com/zh-cn/111840",
        "iPad(第 9 代)": "https://support.apple.com/zh-cn/111898",
        "iPad(第 8 代)": "https://support.apple.com/zh-cn/118451",
        "iPad(第 7 代)": "https://support.apple.com/zh-cn/111911",
        "iPad(第 6 代)": "https://support.apple.com/zh-cn/111957",
        "iPad(第 5 代)": "https://support.apple.com/zh-cn/111960",
        "iPad(第 4 代)": "https://support.apple.com/zh-cn/111993",
        "iPad(第 3 代)": "https://support.apple.com/zh-cn/111992",
        "iPad 2": "https://support.apple.com/zh-cn/111990",
        "iPad": "https://support.apple.com/zh-cn/112438"
    }
    
    # 默认链接，如果找不到匹配的链接，使用这些
    default_links = {
        'Pro': "https://support.apple.com/zh-cn/ipad-pro",
        'Air': "https://support.apple.com/zh-cn/ipad-air",
        'mini': "https://support.apple.com/zh-cn/ipad-mini",
        'iPad': "https://support.apple.com/zh-cn/ipad"
    }
    
    updated_count = 0
    
    # 遍历所有iPad型号
    for ipad in ipad_data:
        ipad_name = ipad['name']
        
        # 尝试精确匹配
        if ipad_name in correct_links:
            ipad['technicalSpecsLink'] = {
                'text': '技术规格',
                'url': correct_links[ipad_name]
            }
            updated_count += 1
            print(f"已精确匹配: {ipad_name} -> {correct_links[ipad_name]}")
            continue
        
        # 尝试模糊匹配
        matched = False
        for model_name, link in correct_links.items():
            # 使用部分匹配，因为名称可能有细微差异
            if (model_name in ipad_name) or (ipad_name in model_name):
                ipad['technicalSpecsLink'] = {
                    'text': '技术规格',
                    'url': link
                }
                updated_count += 1
                print(f"已模糊匹配: {ipad_name} -> {link} (基于 {model_name})")
                matched = True
                break
        
        if not matched:
            # 如果没有找到匹配的链接，使用默认链接
            default_link = None
            if "Pro" in ipad_name:
                default_link = default_links['Pro']
            elif "Air" in ipad_name:
                default_link = default_links['Air']
            elif "mini" in ipad_name:
                default_link = default_links['mini']
            else:
                default_link = default_links['iPad']
            
            ipad['technicalSpecsLink'] = {
                'text': '技术规格',
                'url': default_link
            }
            updated_count += 1
            print(f"使用默认链接: {ipad_name} -> {default_link}")
    
    # 保存更新后的数据
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(ipad_data, f, ensure_ascii=False, indent=2)
    
    print(f"\n总共更新了 {updated_count} 个iPad型号的技术规格链接")

if __name__ == "__main__":
    print("开始修复所有iPad型号的技术规格链接...\n")
    fix_all_tech_specs_links()
    print("\n处理完成!")
