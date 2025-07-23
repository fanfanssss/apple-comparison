#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import os
import re
from bs4 import BeautifulSoup

def extract_ram_type_from_backup():
    """从备份的HTML文件中提取内存规格数据"""
    backup_dir = '/Users/aron/apple-comparison 备份0623/竞品网站iPad数据'
    html_files = [
        '苹果 iPad Pro 参数对比.html',
        '苹果 iPad Air 参数对比.html',
        '苹果 iPad mini 参数对比.html',
        '苹果 iPad 参数对比.html'
    ]
    
    # 存储提取的数据
    extracted_data = {}
    
    for html_file in html_files:
        file_path = os.path.join(backup_dir, html_file)
        if not os.path.exists(file_path):
            print(f"文件不存在: {file_path}")
            continue
        
        print(f"处理文件: {html_file}")
        with open(file_path, 'r', encoding='utf-8') as f:
            html_content = f.read()
        
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # 查找所有产品列
        products = soup.select('.product')
        
        for product in products:
            # 获取产品名称
            product_name_elem = product.select_one('.top-info h3')
            if not product_name_elem:
                continue
            
            product_name = product_name_elem.get_text(strip=True).replace('\n', ' ')
            
            # 查找RAM信息
            ram_elems = product.select('li .li-div-npu')
            if not ram_elems:
                continue
            
            ram_type = None
            
            for elem in ram_elems:
                text = elem.get_text(strip=True).replace('\n', ' ')
                
                # 提取内存类型信息
                ram_type_match = re.search(r'LPDDR\w+', text)
                if ram_type_match:
                    ram_type = ram_type_match.group(0)
                    break
            
            if ram_type:
                # 标准化产品名称以匹配JSON文件中的名称
                normalized_name = normalize_product_name(product_name)
                extracted_data[normalized_name] = {
                    'original_name': product_name,
                    'ramType': ram_type
                }
    
    return extracted_data

def normalize_product_name(name):
    """标准化产品名称以匹配JSON文件中的名称"""
    # 移除括号内容和多余空格
    name = re.sub(r'\(.*?\)', '', name).strip()
    return name

def update_ipad_json(extracted_data):
    """更新iPad JSON文件，添加内存规格信息"""
    json_file = '/Users/aron/CascadeProjects/apple-comparison/public/data/ipad_refined.json'
    
    with open(json_file, 'r', encoding='utf-8') as f:
        ipad_data = json.load(f)
    
    updated_count = 0
    
    for ipad in ipad_data:
        ipad_name = ipad['name']
        
        # 尝试匹配产品名称
        matched = False
        for key, data in extracted_data.items():
            if key in ipad_name or ipad_name in key:
                if 'ramType' in data and data['ramType']:
                    ipad['ramType'] = data['ramType']
                    updated_count += 1
                    matched = True
                    print(f"已更新: {ipad_name} -> 内存规格: {data['ramType']}")
                    break
        
        if not matched:
            # 根据设备型号和发布日期推断内存类型
            if 'M4' in ipad.get('processor', ''):
                ipad['ramType'] = 'LPDDR5X'
                updated_count += 1
                print(f"已推断: {ipad_name} -> 内存规格: LPDDR5X (基于 M4 处理器)")
            elif 'M3' in ipad.get('processor', ''):
                ipad['ramType'] = 'LPDDR5'
                updated_count += 1
                print(f"已推断: {ipad_name} -> 内存规格: LPDDR5 (基于 M3 处理器)")
            elif 'M2' in ipad.get('processor', ''):
                ipad['ramType'] = 'LPDDR5'
                updated_count += 1
                print(f"已推断: {ipad_name} -> 内存规格: LPDDR5 (基于 M2 处理器)")
            elif 'M1' in ipad.get('processor', ''):
                ipad['ramType'] = 'LPDDR4X'
                updated_count += 1
                print(f"已推断: {ipad_name} -> 内存规格: LPDDR4X (基于 M1 处理器)")
            elif 'A14' in ipad.get('processor', '') or 'A15' in ipad.get('processor', '') or 'A16' in ipad.get('processor', '') or 'A17' in ipad.get('processor', ''):
                ipad['ramType'] = 'LPDDR4X'
                updated_count += 1
                print(f"已推断: {ipad_name} -> 内存规格: LPDDR4X (基于 A14-A17 处理器)")
            elif 'A12' in ipad.get('processor', '') or 'A13' in ipad.get('processor', ''):
                ipad['ramType'] = 'LPDDR4X'
                updated_count += 1
                print(f"已推断: {ipad_name} -> 内存规格: LPDDR4X (基于 A12-A13 处理器)")
            elif 'A10' in ipad.get('processor', '') or 'A11' in ipad.get('processor', ''):
                ipad['ramType'] = 'LPDDR4'
                updated_count += 1
                print(f"已推断: {ipad_name} -> 内存规格: LPDDR4 (基于 A10-A11 处理器)")
            elif 'A8' in ipad.get('processor', '') or 'A9' in ipad.get('processor', ''):
                ipad['ramType'] = 'LPDDR3'
                updated_count += 1
                print(f"已推断: {ipad_name} -> 内存规格: LPDDR3 (基于 A8-A9 处理器)")
            elif 'A5' in ipad.get('processor', '') or 'A6' in ipad.get('processor', '') or 'A7' in ipad.get('processor', ''):
                ipad['ramType'] = 'LPDDR2'
                updated_count += 1
                print(f"已推断: {ipad_name} -> 内存规格: LPDDR2 (基于 A5-A7 处理器)")
            elif 'A4' in ipad.get('processor', ''):
                ipad['ramType'] = 'LPDDR'
                updated_count += 1
                print(f"已推断: {ipad_name} -> 内存规格: LPDDR (基于 A4 处理器)")
            else:
                print(f"未找到匹配且无法推断: {ipad_name}")
    
    # 保存更新后的数据
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(ipad_data, f, ensure_ascii=False, indent=2)
    
    print(f"\n总共更新了 {updated_count} 个iPad型号的内存规格信息")

if __name__ == "__main__":
    print("开始从备份数据中提取内存规格信息...")
    extracted_data = extract_ram_type_from_backup()
    
    print("\n开始更新iPad JSON数据...")
    update_ipad_json(extracted_data)
    
    print("\n处理完成!")
