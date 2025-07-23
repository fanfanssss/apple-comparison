#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import os

def update_ipad_benchmarks():
    """更新iPad Air 13 英寸(M3)和iPad mini A17 Pro的基准测试分数"""
    
    # 读取JSON文件
    json_file = '/Users/aron/CascadeProjects/apple-comparison/public/data/ipad_refined.json'
    
    with open(json_file, 'r', encoding='utf-8') as f:
        ipad_data = json.load(f)
    
    # 定义需要更新的基准测试分数
    benchmark_updates = {
        "iPad Air 13 英寸(M3)": {
            "singleCore": "3144",
            "multiCore": "11780",
            "gpu": "44487"
        },
        "iPad mini(A17 Pro)": {
            "singleCore": "2962",
            "multiCore": "7338",
            "gpu": "25777"
        }
    }
    
    updated_count = 0
    
    # 遍历所有iPad型号
    for ipad in ipad_data:
        ipad_name = ipad['name']
        
        # 检查是否是需要更新的型号
        if ipad_name in benchmark_updates:
            # 确保benchmarks字段存在
            if 'benchmarks' not in ipad:
                ipad['benchmarks'] = {}
            
            # 更新基准测试分数
            ipad['benchmarks']['singleCore'] = benchmark_updates[ipad_name]['singleCore']
            ipad['benchmarks']['multiCore'] = benchmark_updates[ipad_name]['multiCore']
            ipad['benchmarks']['gpu'] = benchmark_updates[ipad_name]['gpu']
            
            updated_count += 1
            print(f"已更新 {ipad_name} 的基准测试分数:")
            print(f"  - 单核: {benchmark_updates[ipad_name]['singleCore']}")
            print(f"  - 多核: {benchmark_updates[ipad_name]['multiCore']}")
            print(f"  - GPU: {benchmark_updates[ipad_name]['gpu']}")
    
    # 保存更新后的数据
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(ipad_data, f, ensure_ascii=False, indent=2)
    
    print(f"\n总共更新了 {updated_count} 个iPad型号的基准测试分数")

if __name__ == "__main__":
    print("开始更新iPad Air 13 英寸(M3)和iPad mini A17 Pro的基准测试分数...\n")
    update_ipad_benchmarks()
    print("\n处理完成!")
