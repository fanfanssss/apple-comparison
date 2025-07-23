#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import os

def update_ipad_air_m3_baseband():
    """更新iPad Air M3系列的基带信息为Qualcomm X65M"""
    
    # 读取JSON文件
    json_file = '/Users/aron/CascadeProjects/apple-comparison/public/data/ipad_refined.json'
    
    with open(json_file, 'r', encoding='utf-8') as f:
        ipad_data = json.load(f)
    
    # 需要更新的iPad型号
    target_models = [
        "iPad Air 13 英寸(M3)",
        "iPad Air 11 英寸(M3)"
    ]
    
    updated_count = 0
    
    # 遍历所有iPad型号
    for ipad in ipad_data:
        ipad_name = ipad['name']
        
        # 检查是否是需要更新的型号
        if ipad_name in target_models:
            # 更新基带信息
            ipad['baseband'] = "Qualcomm X65M"
            updated_count += 1
            print(f"已更新: {ipad_name} 的基带信息为 Qualcomm X65M")
    
    # 保存更新后的数据
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(ipad_data, f, ensure_ascii=False, indent=2)
    
    print(f"\n总共更新了 {updated_count} 个iPad型号的基带信息")

if __name__ == "__main__":
    print("开始更新iPad Air M3系列的基带信息...\n")
    update_ipad_air_m3_baseband()
    print("\n处理完成!")
