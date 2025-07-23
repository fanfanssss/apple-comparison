#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import os

def update_specific_links():
    """更新特定iPad Pro型号的技术规格链接"""
    
    # 定义需要更新的链接
    specific_links = {
        "iPad Pro 12.9 英寸(第 3 代)": "https://support.apple.com/zh-cn/111979",
        "iPad Pro 11 英寸(第 2 代)": "https://support.apple.com/zh-cn/118452",
        "iPad Pro 12.9 英寸(第 4 代)": "https://support.apple.com/zh-cn/111977",
        "iPad Pro 11 英寸(第 3 代)": "https://support.apple.com/zh-cn/111897",
        "iPad Pro 12.9 英寸(第 5 代)": "https://support.apple.com/zh-cn/111896",
        "iPad Pro 11 英寸(第 4 代)": "https://support.apple.com/zh-cn/111842",
        "iPad Pro 12.9 英寸(第 6 代)": "https://support.apple.com/zh-cn/111841",
        "iPad Pro 11 英寸(M4)": "https://support.apple.com/zh-cn/119892"
    }
    
    # 读取JSON文件
    json_file = '/Users/aron/CascadeProjects/apple-comparison/public/data/ipad_refined.json'
    
    with open(json_file, 'r', encoding='utf-8') as f:
        ipad_data = json.load(f)
    
    updated_count = 0
    
    # 遍历所有iPad型号
    for ipad in ipad_data:
        ipad_name = ipad['name']
        
        # 检查是否是需要更新的型号
        for model_name, link_url in specific_links.items():
            # 使用部分匹配，因为名称可能有细微差异
            if model_name in ipad_name:
                # 更新链接
                ipad['technicalSpecsLink'] = {
                    'text': '技术规格',
                    'url': link_url
                }
                updated_count += 1
                print(f"已更新: {ipad_name} -> 技术规格链接: {link_url}")
                break
    
    # 保存更新后的数据
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(ipad_data, f, ensure_ascii=False, indent=2)
    
    print(f"\n总共更新了 {updated_count} 个iPad型号的技术规格链接")

if __name__ == "__main__":
    print("开始更新特定iPad Pro型号的技术规格链接...")
    update_specific_links()
    print("\n处理完成!")
