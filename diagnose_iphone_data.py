#!/usr/bin/env python3
import json
import sys

print("诊断iPhone JSON数据问题...")

try:
    # 读取JSON文件
    with open('public/data/iphone_refined.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    print(f"成功加载JSON数据，共{len(data)}个iPhone产品")
    
    # 检查第一个产品的关键字段
    if data and len(data) > 0:
        sample = data[0]
        print("\n第一个产品样本:")
        print(f"ID: {sample.get('id', 'N/A')}")
        print(f"Model: {sample.get('model', 'N/A')}")
        
        # 检查名称字段是否正确
        name_field = sample.get('name', 'N/A')
        print(f"Name: {name_field} (类型: {type(name_field).__name__})")
        
        # 检查发布日期字段是否正确
        release_date = sample.get('releaseDate', 'N/A')
        print(f"Release Date: {release_date} (类型: {type(release_date).__name__})")
        
        # 检查其他关键字段
        print(f"\n关键字段类型检查:")
        key_fields = ['displaySize', 'processor', 'ram', 'materials', 'dimensions', 'weight']
        for field in key_fields:
            value = sample.get(field, 'N/A')
            print(f"{field}: {type(value).__name__}")
            if isinstance(value, dict):
                print(f"  - 键: {list(value.keys())}")
                
        # 检查第一个产品是否有基本属性
        print("\n基本属性检查:")
        required_fields = ['id', 'name', 'model', 'releaseDate']
        for field in required_fields:
            if field not in sample:
                print(f"警告：缺少必要字段 '{field}'")
        
        # 检查所有产品ID是否唯一
        ids = [p.get('id') for p in data]
        unique_ids = set(ids)
        if len(ids) != len(unique_ids):
            print(f"\n警告：产品ID不唯一！有{len(ids) - len(unique_ids)}个重复ID")
        
    else:
        print("警告：iPhone数据为空！")
        
    # 检查JSON文件整体结构
    if not isinstance(data, list):
        print(f"\n错误：JSON数据根节点不是列表！而是 {type(data).__name__}")
        
except json.JSONDecodeError as e:
    print(f"错误：JSON解析失败 - {e}")
    sys.exit(1)
except FileNotFoundError:
    print(f"错误：找不到JSON文件 'public/data/iphone_refined.json'")
    sys.exit(1)
except Exception as e:
    print(f"未知错误：{e}")
    sys.exit(1)
    
print("\n诊断完成。")
