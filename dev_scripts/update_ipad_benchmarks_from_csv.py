#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import csv
import os

def update_ipad_benchmarks_from_csv():
    """根据CSV文件更新iPad产品的跑分数据"""
    
    # 读取JSON文件
    json_file = '/Users/aron/CascadeProjects/apple-comparison/public/data/ipad_refined.json'
    csv_file = '/Users/aron/CascadeProjects/apple-comparison/跑分数据表.csv'
    
    with open(json_file, 'r', encoding='utf-8') as f:
        ipad_data = json.load(f)
    
    # 从CSV文件中提取iPad跑分数据
    ipad_benchmarks = {}
    
    # 处理单核跑分
    single_core_scores = {}
    # 处理多核跑分
    multi_core_scores = {}
    # 处理GPU跑分
    gpu_scores = {}
    
    with open(csv_file, 'r', encoding='utf-8') as f:
        csv_reader = csv.reader(f)
        rows = list(csv_reader)
        
        # 跳过标题行
        for i in range(1, len(rows)):
            # 单核跑分
            if rows[i][0].strip() and 'iPad' in rows[i][0]:
                model_name = rows[i][0].strip()
                score = rows[i][1].strip()
                if score:  # 确保分数不为空
                    single_core_scores[model_name] = score
            
            # 多核跑分
            if rows[i][3].strip() and 'iPad' in rows[i][3]:
                model_name = rows[i][3].strip()
                score = rows[i][4].strip()
                if score:  # 确保分数不为空
                    multi_core_scores[model_name] = score
            
            # GPU跑分
            if rows[i][6].strip() and 'iPad' in rows[i][6]:
                model_name = rows[i][6].strip()
                score = rows[i][7].strip()
                if score:  # 确保分数不为空
                    gpu_scores[model_name] = score
    
    # 创建映射表，将CSV中的型号名称映射到JSON中的型号名称
    model_mapping = {
        # iPad Pro系列
        "iPad Pro 13-inch (M4)": "iPad Pro 13 英寸(M4)",
        "iPad Pro 11-inch (M4)": "iPad Pro 11 英寸(M4)",
        "iPad Pro (12.9-inch, 6th generation)": "iPad Pro 12.9 英寸(M2)",
        "iPad Pro (11-inch, 4th generation)": "iPad Pro 11 英寸(M2)",
        "iPad Pro (12.9-inch 5th generation)": "iPad Pro 12.9 英寸(M1)",
        "iPad Pro (11-inch 3rd generation)": "iPad Pro 11 英寸(M1)",
        "iPad Pro 12.9-inch (4th generation)": "iPad Pro 12.9 英寸(A12Z)",
        "iPad Pro 11-inch (2nd generation)": "iPad Pro 11 英寸(A12Z)",
        "iPad Pro (12.9-inch 3rd Generation)": "iPad Pro 12.9 英寸(A12X)",
        "iPad Pro (11-inch)": "iPad Pro 11 英寸(A12X)",
        "iPad Pro (10.5-inch)": "iPad Pro 10.5 英寸",
        
        # iPad Air系列
        "iPad Air 13-inch (M2)": "iPad Air 13 英寸(M2)",
        "iPad Air 11-inch (M2)": "iPad Air 11 英寸(M2)",
        "iPad Air (5th generation)": "iPad Air(M1)",
        "iPad Air (4th generation)": "iPad Air(A14)",
        "iPad Air (3rd generation)": "iPad Air 3",
        
        # iPad mini系列
        "iPad mini (6th generation)": "iPad mini(第 6 代)",
        "iPad mini (5th generation)": "iPad mini(第 5 代)",
        
        # iPad标准系列
        "iPad (9th generation)": "iPad(第 9 代)",
        "iPad (8th generation)": "iPad(第 8 代)"
    }
    
    # 整合所有跑分数据
    for csv_model, json_model in model_mapping.items():
        if csv_model in single_core_scores or csv_model in multi_core_scores or csv_model in gpu_scores:
            ipad_benchmarks[json_model] = {}
            
            if csv_model in single_core_scores:
                ipad_benchmarks[json_model]["singleCore"] = single_core_scores[csv_model]
            
            if csv_model in multi_core_scores:
                ipad_benchmarks[json_model]["multiCore"] = multi_core_scores[csv_model]
            
            if csv_model in gpu_scores:
                ipad_benchmarks[json_model]["gpu"] = gpu_scores[csv_model]
    
    # 更新iPad数据
    updated_count = 0
    
    # 遍历所有iPad型号
    for ipad in ipad_data:
        ipad_name = ipad['name']
        
        # 检查是否是需要更新的型号
        if ipad_name in ipad_benchmarks:
            # 确保benchmarks字段存在
            if 'benchmarks' not in ipad:
                ipad['benchmarks'] = {}
            
            # 更新基准测试分数
            benchmark_updated = False
            
            if "singleCore" in ipad_benchmarks[ipad_name]:
                ipad['benchmarks']['singleCore'] = ipad_benchmarks[ipad_name]['singleCore']
                benchmark_updated = True
            
            if "multiCore" in ipad_benchmarks[ipad_name]:
                ipad['benchmarks']['multiCore'] = ipad_benchmarks[ipad_name]['multiCore']
                benchmark_updated = True
            
            if "gpu" in ipad_benchmarks[ipad_name]:
                ipad['benchmarks']['gpu'] = ipad_benchmarks[ipad_name]['gpu']
                benchmark_updated = True
            
            if benchmark_updated:
                updated_count += 1
                print(f"已更新 {ipad_name} 的基准测试分数:")
                if "singleCore" in ipad_benchmarks[ipad_name]:
                    print(f"  - 单核: {ipad_benchmarks[ipad_name]['singleCore']}")
                if "multiCore" in ipad_benchmarks[ipad_name]:
                    print(f"  - 多核: {ipad_benchmarks[ipad_name]['multiCore']}")
                if "gpu" in ipad_benchmarks[ipad_name]:
                    print(f"  - GPU: {ipad_benchmarks[ipad_name]['gpu']}")
    
    # 保存更新后的数据
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(ipad_data, f, ensure_ascii=False, indent=2)
    
    print(f"\n总共更新了 {updated_count} 个iPad型号的基准测试分数")

if __name__ == "__main__":
    print("开始根据CSV文件更新iPad产品的跑分数据...\n")
    update_ipad_benchmarks_from_csv()
    print("\n处理完成!")
