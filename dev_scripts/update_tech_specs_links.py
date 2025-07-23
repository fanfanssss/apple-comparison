#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import os
import re
from bs4 import BeautifulSoup

def extract_tech_specs_links():
    """从备份的HTML文件中提取技术规格链接"""
    backup_dir = '/Users/aron/apple-comparison 备份0623/竞品网站iPad数据'
    html_files = [
        '苹果 iPad Pro 参数对比.html',
        '苹果 iPad Air 参数对比.html',
        '苹果 iPad mini 参数对比.html',
        '苹果 iPad 参数对比.html'
    ]
    
    # 存储提取的数据
    extracted_links = {}
    
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
            
            # 查找技术规格链接
            specs_link_elem = product.select_one('li a[href*="support.apple.com"]')
            if not specs_link_elem:
                continue
            
            specs_link = specs_link_elem.get('href')
            
            if specs_link:
                # 标准化产品名称以匹配JSON文件中的名称
                normalized_name = normalize_product_name(product_name)
                extracted_links[normalized_name] = {
                    'original_name': product_name,
                    'specs_link': specs_link
                }
                print(f"找到链接: {normalized_name} -> {specs_link}")
    
    return extracted_links

def normalize_product_name(name):
    """标准化产品名称以匹配JSON文件中的名称"""
    # 移除括号内容和多余空格
    name = re.sub(r'\(.*?\)', '', name).strip()
    return name

def update_ipad_json(extracted_links):
    """更新iPad JSON文件，添加技术规格链接"""
    json_file = '/Users/aron/CascadeProjects/apple-comparison/public/data/ipad_refined.json'
    
    with open(json_file, 'r', encoding='utf-8') as f:
        ipad_data = json.load(f)
    
    updated_count = 0
    
    # 默认链接，如果找不到匹配的链接，使用这些
    default_links = {
        'iPad Pro': 'https://support.apple.com/zh-cn/ipad-pro',
        'iPad Air': 'https://support.apple.com/zh-cn/ipad-air',
        'iPad mini': 'https://support.apple.com/zh-cn/ipad-mini',
        'iPad': 'https://support.apple.com/zh-cn/ipad'
    }
    
    for ipad in ipad_data:
        ipad_name = ipad['name']
        
        # 尝试匹配产品名称
        matched = False
        for key, data in extracted_links.items():
            if key in ipad_name or ipad_name in key:
                if 'specs_link' in data and data['specs_link']:
                    # 更新为对象格式，包含URL和文本
                    ipad['technicalSpecsLink'] = {
                        'text': '技术规格',
                        'url': data['specs_link']
                    }
                    updated_count += 1
                    matched = True
                    print(f"已更新: {ipad_name} -> 技术规格链接: {data['specs_link']}")
                    break
        
        if not matched:
            # 如果没有找到匹配的链接，使用默认链接
            default_link = None
            for series_name, link in default_links.items():
                if series_name in ipad_name:
                    default_link = link
                    break
            
            if default_link:
                ipad['technicalSpecsLink'] = {
                    'text': '技术规格',
                    'url': default_link
                }
                updated_count += 1
                print(f"已使用默认链接: {ipad_name} -> 技术规格链接: {default_link}")
            else:
                # 如果没有找到默认链接，使用通用的iPad支持页面
                ipad['technicalSpecsLink'] = {
                    'text': '技术规格',
                    'url': 'https://support.apple.com/zh-cn/ipad'
                }
                updated_count += 1
                print(f"已使用通用链接: {ipad_name} -> 技术规格链接: https://support.apple.com/zh-cn/ipad")
    
    # 保存更新后的数据
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(ipad_data, f, ensure_ascii=False, indent=2)
    
    print(f"\n总共更新了 {updated_count} 个iPad型号的技术规格链接")

if __name__ == "__main__":
    print("开始从备份数据中提取技术规格链接...")
    extracted_links = extract_tech_specs_links()
    
    print("\n开始更新iPad JSON数据...")
    update_ipad_json(extracted_links)
    
    print("\n处理完成!")
