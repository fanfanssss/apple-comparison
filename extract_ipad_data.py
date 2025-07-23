#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import json
import re
from bs4 import BeautifulSoup
from datetime import datetime

# 定义数据提取目录
DATA_DIR = "/Users/aron/CascadeProjects/apple-comparison/竞品网站iPad数据"
OUTPUT_FILE = "/Users/aron/CascadeProjects/apple-comparison/public/data/ipad_refined.json"

# iPad 系列文件
ipad_files = {
    "pro": os.path.join(DATA_DIR, "苹果 iPad Pro 参数对比.html"),
    "air": os.path.join(DATA_DIR, "苹果 iPad Air 参数对比.html"),
    "mini": os.path.join(DATA_DIR, "苹果 iPad mini 参数对比.html"),
    "standard": os.path.join(DATA_DIR, "苹果 iPad 参数对比.html")
}

# 参数映射表 - 将竞品网站的参数名映射到我们的JSON字段
param_mapping = {
    "宣传口号": "marketingSlogan",
    "发布时间": "releaseDate",
    "支持系统": "os",
    "型号标识": "model",
    "外观颜色": "colors",
    "增强现实": "arSupport",
    "芯片": "processor",
    "RAM": "ram",
    "ROM": "storage",
    "屏幕参数": "displayTechnology",
    "分辨率": "displayResolution",
    "刷新率": "displayRefreshRate",
    "亮度(nits)": "displayBrightness",
    "色彩": "displayColorGamut",
    "后置摄像头": "camera",
    "前置摄像头": "frontCamera",
    "激光雷达": "lidar",
    "笔": "pencilSupport",
    "有线接口": "ports",
    "基带(蜂窝版)": "baseband",
    "无线局域网": "wifiStandard",
    "蓝牙": "bluetoothVersion",
    "解锁方式": "security",
    "电池容量": "batteryCapacity",
    "续航时长": "batteryLife",
    "输入输出": "audioFeatures",
    "尺寸重量": "dimensions",
    "规格与手册": "technicalSpecsLink"
}

# 提取颜色信息的函数
def extract_colors(color_div):
    colors = []
    if not color_div:
        return colors
    
    color_elements = color_div.find_all("div", class_="li-div-color-a")
    for color_elem in color_elements:
        color_style = color_elem.get("style", "")
        color_name = color_elem.get("title", "未知颜色")
        color_code_match = re.search(r'background-color: (#[0-9a-fA-F]{3,6}|[a-z]+)', color_style)
        color_code = color_code_match.group(1) if color_code_match else "#FFFFFF"
        
        colors.append({
            "name": color_name,
            "code": color_code
        })
    
    return colors

# 生成唯一ID的函数
def generate_id(name):
    # 将名称转换为小写，替换空格为连字符，移除特殊字符
    name = name.lower()
    name = re.sub(r'[^\w\s]', '', name)
    name = name.replace(" ", "-")
    # 替换中文为拼音或移除（简化处理）
    name = name.replace("英寸", "inch")
    name = re.sub(r'[^\x00-\x7F]', '', name)
    # 移除多余的连字符
    name = re.sub(r'-+', '-', name)
    name = name.strip('-')
    return f"ipad-{name}"

# 主数据提取函数
def extract_ipad_data():
    all_ipads = []
    
    for ipad_type, file_path in ipad_files.items():
        print(f"处理 {ipad_type} 系列数据...")
        
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                html_content = file.read()
        except Exception as e:
            print(f"无法读取文件 {file_path}: {e}")
            continue
        
        soup = BeautifulSoup(html_content, 'html.parser')
        products = soup.select('.product')
        
        for product in products:
            ipad_data = {}
            
            # 提取名称
            name_elem = product.select_one('.top-info h3')
            if name_elem:
                full_name = name_elem.get_text(strip=True).replace('\n', ' ')
                ipad_data["name"] = full_name
                ipad_data["id"] = generate_id(full_name)
            
            # 提取参数
            feature_items = product.select('ul.cd-features-list li')
            feature_labels = soup.select('.features .cd-features-list.ul-ext-right li')
            
            for i, item in enumerate(feature_items):
                if i < len(feature_labels):
                    label = feature_labels[i].get_text(strip=True)
                    if label in param_mapping:
                        field_name = param_mapping[label]
                        
                        # 特殊处理颜色
                        if field_name == "colors":
                            color_div = item.select_one('.li-div-color')
                            ipad_data[field_name] = extract_colors(color_div)
                        else:
                            value = item.get_text(strip=True)
                            if value and value != "暂无" and value != "-":
                                ipad_data[field_name] = value
            
            # 添加系列信息
            ipad_data["series"] = ipad_type.capitalize()
            
            # 添加其他必要字段
            if "displayTechnology" in ipad_data and "displaySize" not in ipad_data:
                display_size_match = re.search(r'(\d+\.?\d*)英寸', ipad_data["displayTechnology"])
                if display_size_match:
                    ipad_data["displaySize"] = f"{display_size_match.group(1)}英寸"
            
            # 处理重量和尺寸
            if "dimensions" in ipad_data:
                dims = ipad_data["dimensions"]
                weight_match = re.search(r'(\d+\.?\d*)\s*克', dims)
                if weight_match:
                    ipad_data["weight"] = f"{weight_match.group(1)} g"
                
                # 提取尺寸
                dim_match = re.search(r'(\d+\.?\d*)\s*×\s*(\d+\.?\d*)\s*×\s*(\d+\.?\d*)\s*毫米', dims)
                if dim_match:
                    ipad_data["dimensions"] = f"{dim_match.group(1)} x {dim_match.group(2)} x {dim_match.group(3)} mm"
            
            # 添加水印和防水等级
            ipad_data["waterResistance"] = "无官方防水等级"
            
            # 添加连接性
            if "wifiStandard" in ipad_data or "bluetoothVersion" in ipad_data:
                connectivity = []
                if "wifiStandard" in ipad_data:
                    connectivity.append(ipad_data["wifiStandard"])
                if "bluetoothVersion" in ipad_data:
                    connectivity.append(f"蓝牙 {ipad_data['bluetoothVersion']}")
                
                ipad_data["connectivity"] = ", ".join(connectivity)
            
            all_ipads.append(ipad_data)
    
    # 按发布日期排序（新到旧）
    def parse_date(date_str):
        if not date_str:
            return datetime(1900, 1, 1)  # 默认很早的日期
        
        match = re.search(r'(\d{4})年(\d{1,2})月', date_str)
        if match:
            year = int(match.group(1))
            month = int(match.group(2))
            return datetime(year, month, 1)
        return datetime(1900, 1, 1)
    
    all_ipads.sort(key=lambda x: parse_date(x.get("releaseDate", "")), reverse=True)
    
    return all_ipads

# 主函数
def main():
    print("开始提取 iPad 数据...")
    ipad_data = extract_ipad_data()
    
    print(f"共提取了 {len(ipad_data)} 款 iPad 的数据")
    
    # 保存为 JSON 文件
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(ipad_data, f, ensure_ascii=False, indent=2)
    
    print(f"数据已保存到 {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
