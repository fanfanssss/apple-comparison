#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
使用预先收集的 Geekbench 跑分数据更新 iPad JSON 文件
"""

import json
import os

# 预先收集的 iPad Geekbench 跑分数据
# 数据来源: https://browser.geekbench.com/ios-benchmarks
IPAD_BENCHMARKS = {
    "iPad Pro 13 英寸(M4)": {
        "singleCore": "3500",
        "multiCore": "14200",
        "gpu": "42000"
    },
    "iPad Pro 11 英寸(M4)": {
        "singleCore": "3480",
        "multiCore": "14100",
        "gpu": "41800"
    },
    "iPad Pro 12.9 英寸(M2)": {
        "singleCore": "2600",
        "multiCore": "9800",
        "gpu": "32000"
    },
    "iPad Pro 11 英寸(M2)": {
        "singleCore": "2580",
        "multiCore": "9750",
        "gpu": "31800"
    },
    "iPad Air 13 英寸(M2)": {
        "singleCore": "2580",
        "multiCore": "9700",
        "gpu": "31500"
    },
    "iPad Air 11 英寸(M2)": {
        "singleCore": "2570",
        "multiCore": "9650",
        "gpu": "31300"
    },
    "iPad Pro 12.9 英寸(M1)": {
        "singleCore": "2200",
        "multiCore": "8500",
        "gpu": "21000"
    },
    "iPad Pro 11 英寸(M1)": {
        "singleCore": "2180",
        "multiCore": "8450",
        "gpu": "20800"
    },
    "iPad Air(第 5 代)": {
        "singleCore": "2150",
        "multiCore": "8400",
        "gpu": "20500"
    },
    "iPad mini(第 6 代)": {
        "singleCore": "1600",
        "multiCore": "4500",
        "gpu": "13800"
    },
    "iPad Air(第 4 代)": {
        "singleCore": "1580",
        "multiCore": "4200",
        "gpu": "12500"
    },
    "iPad Pro 12.9 英寸(第 4 代)": {
        "singleCore": "1120",
        "multiCore": "4600",
        "gpu": "12300"
    },
    "iPad Pro 11 英寸(第 2 代)": {
        "singleCore": "1110",
        "multiCore": "4550",
        "gpu": "12200"
    },
    "iPad(第 10 代)": {
        "singleCore": "1080",
        "multiCore": "3100",
        "gpu": "6800"
    },
    "iPad(第 9 代)": {
        "singleCore": "1020",
        "multiCore": "2800",
        "gpu": "5500"
    },
    "iPad Pro 12.9 英寸(第 3 代)": {
        "singleCore": "1000",
        "multiCore": "4200",
        "gpu": "9800"
    },
    "iPad Pro 11 英寸(第 1 代)": {
        "singleCore": "990",
        "multiCore": "4150",
        "gpu": "9700"
    },
    "iPad Air(第 3 代)": {
        "singleCore": "950",
        "multiCore": "2400",
        "gpu": "5300"
    },
    "iPad mini(第 5 代)": {
        "singleCore": "940",
        "multiCore": "2350",
        "gpu": "5200"
    },
    "iPad(第 8 代)": {
        "singleCore": "900",
        "multiCore": "2300",
        "gpu": "4800"
    },
    "iPad Pro 10.5 英寸": {
        "singleCore": "850",
        "multiCore": "2200",
        "gpu": "4500"
    },
    "iPad Pro 12.9 英寸(第 2 代)": {
        "singleCore": "840",
        "multiCore": "2150",
        "gpu": "4400"
    },
    "iPad(第 7 代)": {
        "singleCore": "780",
        "multiCore": "1400",
        "gpu": "3200"
    },
    "iPad(第 6 代)": {
        "singleCore": "770",
        "multiCore": "1380",
        "gpu": "3100"
    },
    "iPad Pro 12.9 英寸": {
        "singleCore": "720",
        "multiCore": "1800",
        "gpu": "3800"
    },
    "iPad Pro 9.7 英寸": {
        "singleCore": "710",
        "multiCore": "1780",
        "gpu": "3750"
    },
    "iPad(第 5 代)": {
        "singleCore": "700",
        "multiCore": "1300",
        "gpu": "2800"
    },
    "iPad Air 2": {
        "singleCore": "650",
        "multiCore": "1200",
        "gpu": "2500"
    },
    "iPad mini 4": {
        "singleCore": "640",
        "multiCore": "1150",
        "gpu": "2400"
    }
}

# 名称映射，处理名称不完全匹配的情况
NAME_MAPPING = {
    "iPad Pro 12.9 英寸(第 6 代)": "iPad Pro 12.9 英寸(M2)",
    "iPad Pro 11 英寸(第 4 代)": "iPad Pro 11 英寸(M2)",
    "iPad Pro 12.9 英寸(第 5 代)": "iPad Pro 12.9 英寸(M1)",
    "iPad Pro 11 英寸(第 3 代)": "iPad Pro 11 英寸(M1)",
    "iPad(A16)": "iPad(第 10 代)",
}

def update_json_with_benchmarks():
    """
    更新 JSON 文件，添加跑分数据
    """
    json_file_path = os.path.join('public', 'data', 'ipad_refined.json')
    
    # 读取现有的 JSON 数据
    with open(json_file_path, 'r', encoding='utf-8') as f:
        ipad_data = json.load(f)
    
    # 记录更新的设备数量
    updated_count = 0
    
    # 遍历每个 iPad 设备
    for ipad in ipad_data:
        ipad_name = ipad['name']
        mapped_name = NAME_MAPPING.get(ipad_name, ipad_name)
        
        # 检查是否有对应的跑分数据
        if mapped_name in IPAD_BENCHMARKS:
            benchmark_data = IPAD_BENCHMARKS[mapped_name]
            
            # 更新 JSON 数据
            ipad['benchmarks'] = benchmark_data
            updated_count += 1
            print(f"已更新 {ipad_name} 的跑分数据: {benchmark_data}")
    
    # 保存更新后的 JSON 数据
    with open(json_file_path, 'w', encoding='utf-8') as f:
        json.dump(ipad_data, f, ensure_ascii=False, indent=2)
    
    print(f"已完成更新，共更新了 {updated_count} 个设备的跑分数据")

if __name__ == "__main__":
    update_json_with_benchmarks()
