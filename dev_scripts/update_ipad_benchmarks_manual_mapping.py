#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import csv
import os
import re

def update_ipad_benchmarks_with_manual_mapping():
    """使用手动映射更新所有iPad产品的跑分数据"""
    
    # 读取JSON文件
    json_file = '/Users/aron/CascadeProjects/apple-comparison/public/data/ipad_refined.json'
    csv_file = '/Users/aron/CascadeProjects/apple-comparison/跑分数据表.csv'
    
    with open(json_file, 'r', encoding='utf-8') as f:
        ipad_data = json.load(f)
    
    # 从CSV文件中提取iPad跑分数据
    single_core_scores = {}
    multi_core_scores = {}
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
    
    # 创建JSON中型号名称到CSV中型号名称的精确映射
    json_to_csv_mapping = {
        # iPad Pro系列
        "iPad Pro 13 英寸(M4)": "iPad Pro 13-inch (M4)",
        "iPad Pro 11 英寸(M4)": "iPad Pro 11-inch (M4)",
        "iPad Pro 12.9 英寸(M2)": "iPad Pro (12.9-inch, 6th generation)",
        "iPad Pro 11 英寸(M2)": "iPad Pro (11-inch, 4th generation)",
        "iPad Pro 12.9 英寸(M1)": "iPad Pro (12.9-inch 5th generation)",
        "iPad Pro 11 英寸(M1)": "iPad Pro (11-inch 3rd generation)",
        "iPad Pro 12.9 英寸(A12Z)": "iPad Pro 12.9-inch (4th generation)",
        "iPad Pro 11 英寸(A12Z)": "iPad Pro 11-inch (2nd generation)",
        "iPad Pro 12.9 英寸(A12X)": "iPad Pro (12.9-inch 3rd Generation)",
        "iPad Pro 11 英寸(A12X)": "iPad Pro (11-inch)",
        "iPad Pro 10.5 英寸": "iPad Pro (10.5-inch)",
        "iPad Pro 9.7 英寸": "iPad Pro (9.7-inch)",
        "iPad Pro 12.9 英寸": "iPad Pro (12.9-inch)",
        "iPad Pro 12.9 英寸（第 1 代）": "iPad Pro (12.9-inch)",
        
        # iPad Air系列
        "iPad Air 13 英寸(M3)": "iPad Air 13-inch (M2)",  # 暂无M3数据，使用M2数据
        "iPad Air 11 英寸(M3)": "iPad Air 11-inch (M2)",  # 暂无M3数据，使用M2数据
        "iPad Air 13 英寸(M2)": "iPad Air 13-inch (M2)",
        "iPad Air 11 英寸(M2)": "iPad Air 11-inch (M2)",
        "iPad Air(M1)": "iPad Air (5th generation)",
        "iPad Air（M1）": "iPad Air (5th generation)",
        "iPad Air(A14)": "iPad Air (4th generation)",
        "iPad Air（A14）": "iPad Air (4th generation)",
        "iPad Air 3": "iPad Air (3rd generation)",
        "iPad Air（第 3 代）": "iPad Air (3rd generation)",
        "iPad Air 2": "iPad Air 2",
        "iPad Air": "iPad Air",
        
        # iPad mini系列
        "iPad mini(A17 Pro)": "iPad mini (6th generation)",  # 使用最新的mini 6数据
        "iPad mini(第 6 代)": "iPad mini (6th generation)",
        "iPad mini（第 6 代）": "iPad mini (6th generation)",
        "iPad mini(第 5 代)": "iPad mini (5th generation)",
        "iPad mini（第 5 代）": "iPad mini (5th generation)",
        "iPad mini 4": "iPad mini 4",
        "iPad mini 3": "iPad mini 3",
        "iPad mini 2": "iPad mini 2",
        "iPad mini": "iPad mini",
        
        # iPad标准系列
        "iPad(A16)": "iPad (10th generation)",  # 使用最新的iPad数据
        "iPad(第 10 代)": "iPad (10th generation)",
        "iPad（第 10 代）": "iPad (10th generation)",
        "iPad(第 9 代)": "iPad (9th generation)",
        "iPad（第 9 代）": "iPad (9th generation)",
        "iPad(第 8 代)": "iPad (8th generation)",
        "iPad（第 8 代）": "iPad (8th generation)",
        "iPad(第 7 代)": "iPad (7th generation)",
        "iPad（第 7 代）": "iPad (7th generation)",
        "iPad(第 6 代)": "iPad (6th generation)",
        "iPad（第 6 代）": "iPad (6th generation)",
        "iPad(第 5 代)": "iPad (5th generation)",
        "iPad（第 5 代）": "iPad (5th generation)",
        "iPad(第 4 代)": "iPad (4th generation)",
        "iPad（第 4 代）": "iPad (4th generation)",
        "iPad(第 3 代)": "iPad (3rd generation)",
        "iPad（第 3 代）": "iPad (3rd generation)",
        "iPad 2": "iPad 2",
        "iPad": "iPad"
    }
    
    # 添加一些特殊映射，处理一些特殊情况
    special_mappings = {
        # 特殊情况：某些型号在CSV中没有，但可以使用类似型号的数据
        "iPad Pro 12.9 英寸（M2）": "iPad Pro (12.9-inch, 6th generation)",
        "iPad Pro 11 英寸（M2）": "iPad Pro (11-inch, 4th generation)",
        "iPad Pro 12.9 英寸（M1）": "iPad Pro (12.9-inch 5th generation)",
        "iPad Pro 11 英寸（M1）": "iPad Pro (11-inch 3rd generation)",
        "iPad Pro 12.9 英寸（A12Z）": "iPad Pro 12.9-inch (4th generation)",
        "iPad Pro 11 英寸（A12Z）": "iPad Pro 11-inch (2nd generation)",
        "iPad Pro 12.9 英寸（A12X）": "iPad Pro (12.9-inch 3rd Generation)",
        "iPad Pro 11 英寸（A12X）": "iPad Pro (11-inch)"
    }
    
    # 合并映射
    json_to_csv_mapping.update(special_mappings)
    
    # 更新iPad数据
    updated_count = 0
    
    # 遍历所有iPad型号
    for ipad in ipad_data:
        ipad_name = ipad['name']
        
        # 检查是否有精确匹配
        if ipad_name in json_to_csv_mapping:
            csv_model = json_to_csv_mapping[ipad_name]
            
            # 确保benchmarks字段存在
            if 'benchmarks' not in ipad:
                ipad['benchmarks'] = {}
            
            # 更新基准测试分数
            benchmark_updated = False
            
            if csv_model in single_core_scores:
                ipad['benchmarks']['singleCore'] = single_core_scores[csv_model]
                benchmark_updated = True
            
            if csv_model in multi_core_scores:
                ipad['benchmarks']['multiCore'] = multi_core_scores[csv_model]
                benchmark_updated = True
            
            if csv_model in gpu_scores:
                ipad['benchmarks']['gpu'] = gpu_scores[csv_model]
                benchmark_updated = True
            
            if benchmark_updated:
                updated_count += 1
                print(f"已更新 {ipad_name} 的基准测试分数 (匹配到 {csv_model}):")
                if csv_model in single_core_scores:
                    print(f"  - 单核: {single_core_scores[csv_model]}")
                if csv_model in multi_core_scores:
                    print(f"  - 多核: {multi_core_scores[csv_model]}")
                if csv_model in gpu_scores:
                    print(f"  - GPU: {gpu_scores[csv_model]}")
    
    # 保存更新后的数据
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(ipad_data, f, ensure_ascii=False, indent=2)
    
    print(f"\n总共更新了 {updated_count} 个iPad型号的基准测试分数")
    
    # 检查JSON中有哪些型号未被更新
    updated_models = set()
    for ipad in ipad_data:
        ipad_name = ipad['name']
        if ipad_name in json_to_csv_mapping:
            updated_models.add(ipad_name)
    
    # 获取所有iPad型号
    all_ipad_models = set()
    for ipad in ipad_data:
        all_ipad_models.add(ipad['name'])
    
    # 找出未更新的型号
    unupdated_models = all_ipad_models - updated_models
    if unupdated_models:
        print("\n以下JSON型号未被更新:")
        for model in unupdated_models:
            if 'iPad' in model:  # 只显示iPad型号
                print(f"  - {model}")

if __name__ == "__main__":
    print("开始使用手动映射更新所有iPad产品的跑分数据...\n")
    update_ipad_benchmarks_with_manual_mapping()
    print("\n处理完成!")
