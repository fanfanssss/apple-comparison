#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
提取 iPad 的 Geekbench 跑分数据并更新到 JSON 文件中
"""

import json
import re
import requests
from bs4 import BeautifulSoup
import time
import os

# 设置请求头，模拟浏览器访问
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
}

# iPad 型号与 Geekbench URL 的映射关系
IPAD_BENCHMARK_URLS = {
    "iPad Pro 13 英寸(M4)": "https://browser.geekbench.com/ios_devices/ipad-pro-13-inch-m4-10c-cpu",
    "iPad Pro 11 英寸(M4)": "https://browser.geekbench.com/ios_devices/ipad-pro-11-inch-m4-10c-cpu",
    "iPad Air 13 英寸(M2)": "https://browser.geekbench.com/ios_devices/ipad-air-13-inch-m2",
    "iPad Air 11 英寸(M2)": "https://browser.geekbench.com/ios_devices/ipad-air-11-inch-m2",
    "iPad Pro 12.9 英寸(第 6 代)": "https://browser.geekbench.com/ios_devices/ipad14-5",
    "iPad Pro 11 英寸(第 4 代)": "https://browser.geekbench.com/ios_devices/ipad-pro-11-inch-4th-generation",
    "iPad Pro 12.9 英寸(第 5 代)": "https://browser.geekbench.com/ios_devices/ipad-pro-12-9-inch-5th-generation",
    "iPad Pro 11 英寸(第 3 代)": "https://browser.geekbench.com/ios_devices/ipad-pro-11-inch-3rd-generation",
    "iPad Air(第 5 代)": "https://browser.geekbench.com/ios_devices/ipad-air-5th-generation",
    "iPad mini(第 6 代)": "https://browser.geekbench.com/ios_devices/ipad-mini-6th-generation",
    "iPad Air(第 4 代)": "https://browser.geekbench.com/ios_devices/ipad-air-4th-generation",
    "iPad(第 9 代)": "https://browser.geekbench.com/ios_devices/ipad-9th-generation",
    "iPad Pro 12.9 英寸(第 4 代)": "https://browser.geekbench.com/ios_devices/ipad-pro-12-9-inch-4th-generation",
    "iPad Pro 11 英寸(第 2 代)": "https://browser.geekbench.com/ios_devices/ipad-pro-11-inch-2nd-generation",
    "iPad Pro 11 英寸(第 1 代)": "https://browser.geekbench.com/ios_devices/ipad-pro-11-inch",
    "iPad Air(第 3 代)": "https://browser.geekbench.com/ios_devices/ipad-air-3rd-generation",
    "iPad Pro 12.9 英寸(第 3 代)": "https://browser.geekbench.com/ios_devices/ipad-pro-12-9-inch-3rd-generation",
    "iPad mini(第 5 代)": "https://browser.geekbench.com/ios_devices/ipad-mini-5th-generation",
    "iPad(第 8 代)": "https://browser.geekbench.com/ios_devices/ipad-8th-generation",
    "iPad Pro 10.5 英寸": "https://browser.geekbench.com/ios_devices/ipad-pro-10-5-inch",
    "iPad Pro 12.9 英寸(第 2 代)": "https://browser.geekbench.com/ios_devices/ipad-pro-12-9-inch-2nd-generation",
    "iPad(第 7 代)": "https://browser.geekbench.com/ios_devices/ipad-7th-generation",
    "iPad(第 6 代)": "https://browser.geekbench.com/ios_devices/ipad-6th-generation",
    "iPad Pro 12.9 英寸": "https://browser.geekbench.com/ios_devices/ipad-pro-12-9-inch",
    "iPad Pro 9.7 英寸": "https://browser.geekbench.com/ios_devices/ipad-pro-9-7-inch",
    "iPad(第 5 代)": "https://browser.geekbench.com/ios_devices/ipad-5th-generation",
    "iPad Air 2": "https://browser.geekbench.com/ios_devices/ipad-air-2",
    "iPad mini 4": "https://browser.geekbench.com/ios_devices/ipad-mini-4",
    # 添加更多 iPad 型号和对应的 URL
}

# 名称映射，处理名称不完全匹配的情况
NAME_MAPPING = {
    "iPad Pro 12.9 英寸(第 6 代)": "iPad Pro 12.9 英寸(M4)",
    "iPad Pro 11 英寸(第 4 代)": "iPad Pro 11 英寸(M2)",
    # 添加更多名称映射
}

def get_benchmark_data(url):
    """
    从 Geekbench 网站获取跑分数据
    """
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 提取单核、多核和 GPU 跑分
        scores = {}
        
        # 查找跑分数据表格
        score_table = soup.find('div', class_='row scores')
        if score_table:
            score_divs = score_table.find_all('div', class_='col-12 col-md-4')
            
            for div in score_divs:
                score_type = div.find('h6').text.strip() if div.find('h6') else None
                score_value = div.find('div', class_='score').text.strip() if div.find('div', class_='score') else None
                
                if score_type and score_value:
                    if 'Single-Core' in score_type:
                        scores['singleCore'] = score_value
                    elif 'Multi-Core' in score_type:
                        scores['multiCore'] = score_value
                    elif 'Metal' in score_type:
                        scores['gpu'] = score_value
        
        return scores
    except Exception as e:
        print(f"获取跑分数据时出错: {e}")
        return {}

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
        
        # 检查是否有对应的 Geekbench URL
        if mapped_name in IPAD_BENCHMARK_URLS:
            url = IPAD_BENCHMARK_URLS[mapped_name]
            print(f"正在获取 {mapped_name} 的跑分数据...")
            
            # 获取跑分数据
            benchmark_data = get_benchmark_data(url)
            
            if benchmark_data:
                # 更新 JSON 数据
                ipad['benchmarks'] = benchmark_data
                updated_count += 1
                print(f"已更新 {mapped_name} 的跑分数据: {benchmark_data}")
            else:
                print(f"未能获取 {mapped_name} 的跑分数据")
            
            # 添加延迟，避免请求过于频繁
            time.sleep(1)
    
    # 保存更新后的 JSON 数据
    with open(json_file_path, 'w', encoding='utf-8') as f:
        json.dump(ipad_data, f, ensure_ascii=False, indent=2)
    
    print(f"已完成更新，共更新了 {updated_count} 个设备的跑分数据")

if __name__ == "__main__":
    update_json_with_benchmarks()
