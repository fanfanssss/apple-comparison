#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import csv
import os
import re

def normalize_model_name(name):
    """标准化型号名称，便于匹配"""
    name = name.lower()
    name = re.sub(r'[()（）,，\s]', '', name)
    name = name.replace('英寸', '')
    name = name.replace('generation', 'gen')
    name = name.replace('第', '')
    name = name.replace('代', 'gen')
    return name

def update_all_ipad_benchmarks():
    """根据CSV文件更新所有iPad产品的跑分数据"""
    
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
    
    # 创建详细的映射表，将CSV中的型号名称映射到JSON中的型号名称
    model_mapping = {
        # iPad Pro系列
        "iPad Pro 13-inch (M4)": ["iPad Pro 13 英寸(M4)"],
        "iPad Pro 11-inch (M4)": ["iPad Pro 11 英寸(M4)"],
        "iPad Pro (12.9-inch, 6th generation)": ["iPad Pro 12.9 英寸(M2)", "iPad Pro 12.9 英寸（M2）"],
        "iPad Pro (11-inch, 4th generation)": ["iPad Pro 11 英寸(M2)", "iPad Pro 11 英寸（M2）"],
        "iPad Pro (12.9-inch 5th generation)": ["iPad Pro 12.9 英寸(M1)", "iPad Pro 12.9 英寸（M1）"],
        "iPad Pro (11-inch 3rd generation)": ["iPad Pro 11 英寸(M1)", "iPad Pro 11 英寸（M1）"],
        "iPad Pro 12.9-inch (4th generation)": ["iPad Pro 12.9 英寸(A12Z)", "iPad Pro 12.9 英寸（A12Z）"],
        "iPad Pro 11-inch (2nd generation)": ["iPad Pro 11 英寸(A12Z)", "iPad Pro 11 英寸（A12Z）"],
        "iPad Pro (12.9-inch 3rd Generation)": ["iPad Pro 12.9 英寸(A12X)", "iPad Pro 12.9 英寸（A12X）"],
        "iPad Pro (11-inch)": ["iPad Pro 11 英寸(A12X)", "iPad Pro 11 英寸（A12X）"],
        "iPad Pro (10.5-inch)": ["iPad Pro 10.5 英寸"],
        "iPad Pro 9.7-inch": ["iPad Pro 9.7 英寸"],
        "iPad Pro 12.9-inch": ["iPad Pro 12.9 英寸", "iPad Pro 12.9 英寸（第 1 代）"],
        
        # iPad Air系列
        "iPad Air 13-inch (M2)": ["iPad Air 13 英寸(M2)", "iPad Air 13 英寸（M2）"],
        "iPad Air 11-inch (M2)": ["iPad Air 11 英寸(M2)", "iPad Air 11 英寸（M2）"],
        "iPad Air (5th generation)": ["iPad Air(M1)", "iPad Air（M1）"],
        "iPad Air (4th generation)": ["iPad Air(A14)", "iPad Air（A14）"],
        "iPad Air (3rd generation)": ["iPad Air 3", "iPad Air（第 3 代）"],
        "iPad Air 2": ["iPad Air 2"],
        "iPad Air": ["iPad Air"],
        
        # iPad mini系列
        "iPad mini (6th generation)": ["iPad mini(第 6 代)", "iPad mini（第 6 代）"],
        "iPad mini (5th generation)": ["iPad mini(第 5 代)", "iPad mini（第 5 代）"],
        "iPad mini 4": ["iPad mini 4"],
        "iPad mini 3": ["iPad mini 3"],
        "iPad mini 2": ["iPad mini 2"],
        "iPad mini": ["iPad mini"],
        
        # iPad标准系列
        "iPad (10th generation)": ["iPad(第 10 代)", "iPad（第 10 代）"],
        "iPad (9th generation)": ["iPad(第 9 代)", "iPad（第 9 代）"],
        "iPad (8th generation)": ["iPad(第 8 代)", "iPad（第 8 代）"],
        "iPad (7th generation)": ["iPad(第 7 代)", "iPad（第 7 代）"],
        "iPad (6th generation)": ["iPad(第 6 代)", "iPad（第 6 代）"],
        "iPad (5th generation)": ["iPad(第 5 代)", "iPad（第 5 代）"],
        "iPad (4th generation)": ["iPad(第 4 代)", "iPad（第 4 代）"],
        "iPad (3rd generation)": ["iPad(第 3 代)", "iPad（第 3 代）"],
        "iPad 2": ["iPad 2"],
        "iPad": ["iPad"]
    }
    
    # 创建反向映射，从JSON名称映射到CSV名称
    reverse_mapping = {}
    for csv_name, json_names in model_mapping.items():
        for json_name in json_names:
            reverse_mapping[json_name] = csv_name
    
    # 创建标准化名称的映射
    normalized_mapping = {}
    for json_model in ipad_data:
        name = json_model['name']
        normalized_name = normalize_model_name(name)
        normalized_mapping[normalized_name] = name
    
    # 更新iPad数据
    updated_count = 0
    
    # 遍历所有iPad型号
    for ipad in ipad_data:
        ipad_name = ipad['name']
        
        # 尝试直接匹配
        csv_model = None
        if ipad_name in reverse_mapping:
            csv_model = reverse_mapping[ipad_name]
        else:
            # 尝试通过标准化名称匹配
            for csv_name in model_mapping:
                normalized_csv = normalize_model_name(csv_name)
                normalized_ipad = normalize_model_name(ipad_name)
                
                if normalized_csv in normalized_ipad or normalized_ipad in normalized_csv:
                    csv_model = csv_name
                    break
        
        # 如果找到匹配的CSV型号，更新跑分
        if csv_model:
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
    
    # 打印未匹配的CSV型号
    all_csv_models = set(single_core_scores.keys()) | set(multi_core_scores.keys()) | set(gpu_scores.keys())
    matched_models = set()
    for ipad in ipad_data:
        ipad_name = ipad['name']
        if ipad_name in reverse_mapping:
            matched_models.add(reverse_mapping[ipad_name])
    
    unmatched_models = all_csv_models - matched_models
    if unmatched_models:
        print("\n以下CSV型号未匹配到JSON数据:")
        for model in unmatched_models:
            print(f"  - {model}")

if __name__ == "__main__":
    print("开始更新所有iPad产品的跑分数据...\n")
    update_all_ipad_benchmarks()
    print("\n处理完成!")
