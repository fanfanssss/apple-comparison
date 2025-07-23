#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import os
import re
from bs4 import BeautifulSoup

def extract_memory_storage_from_backup():
    """从备份的HTML文件中提取内存和存储容量数据"""
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
            
            # 查找RAM和ROM信息
            ram_rom_elem = product.select('li .li-div-npu')
            if not ram_rom_elem:
                continue
            
            ram_data = []
            storage_data = []
            
            for elem in ram_rom_elem:
                text = elem.get_text(strip=True).replace('\n', ' ')
                
                # 提取RAM信息
                ram_match = re.search(r'(\d+)G\s+LPDDR\w+', text)
                if ram_match:
                    ram = f"{ram_match.group(1)}GB"
                    if ram not in ram_data:
                        ram_data.append(ram)
                
                # 提取存储容量信息
                storage_matches = re.findall(r'(\d+)[GT]', text)
                for match in storage_matches[1:]:  # 跳过第一个匹配（RAM）
                    storage = f"{match}GB" if match != '1' and match != '2' else f"{match}TB"
                    if storage not in storage_data:
                        storage_data.append(storage)
            
            if ram_data or storage_data:
                # 标准化产品名称以匹配JSON文件中的名称
                normalized_name = normalize_product_name(product_name)
                extracted_data[normalized_name] = {
                    'original_name': product_name,
                    'ram': ram_data,
                    'storage': storage_data
                }
    
    return extracted_data

def normalize_product_name(name):
    """标准化产品名称以匹配JSON文件中的名称"""
    # 移除括号内容和多余空格
    name = re.sub(r'\(.*?\)', '', name).strip()
    return name

def update_ipad_json(extracted_data):
    """更新iPad JSON文件，添加内存和存储容量信息"""
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
                if 'ram' in data and data['ram']:
                    ipad['ram'] = data['ram']
                if 'storage' in data and data['storage']:
                    ipad['storage'] = data['storage']
                updated_count += 1
                matched = True
                print(f"已更新: {ipad_name} -> RAM: {data.get('ram', [])}, 存储: {data.get('storage', [])}")
                break
        
        if not matched:
            print(f"未找到匹配: {ipad_name}")
    
    # 保存更新后的数据
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(ipad_data, f, ensure_ascii=False, indent=2)
    
    print(f"\n总共更新了 {updated_count} 个iPad型号的内存和存储容量信息")

if __name__ == "__main__":
    print("开始从备份数据中提取内存和存储容量信息...")
    extracted_data = extract_memory_storage_from_backup()
    
    print("\n开始更新iPad JSON数据...")
    update_ipad_json(extracted_data)
    
    print("\n处理完成!")
