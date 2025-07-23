#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import json
import re
from bs4 import BeautifulSoup
import hashlib

# 定义数据源文件路径
data_dir = "/Users/aron/CascadeProjects/apple-comparison/竞品网站watch数据"
html_files = [
    os.path.join(data_dir, "苹果 Apple Watch Series 参数对比.html"),
    os.path.join(data_dir, "苹果 Apple Watch Ultra 参数对比.html"),
    os.path.join(data_dir, "苹果 Apple Watch SE 参数对比.html")
]

# 定义输出文件路径
output_file = "/Users/aron/CascadeProjects/apple-comparison/public/data/watch_refined.json"

# 参数映射表，将HTML中的参数名映射到JSON中的键名
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
    "无线芯片": "wirelessChip",
    "超宽频芯片": "ultraWidebandChip",
    "屏幕参数": "displayResolution",
    "屏幕材质": "displayTechnology",
    "亮度": "displayBrightness",
    "表镜材质": "displayGlass",
    "表背材质": "backMaterial",
    "基带(蜂窝版)": "baseband",
    "无线局域网": "wifiStandard",
    "蓝牙": "bluetoothVersion",
    "电池容量": "batteryCapacity",
    "续航时间": "batteryLife",
    "防尘防水": "waterResistance",
    "传感器": "sensors",
    "规格与手册": "technicalSpecsLink"
}

# 提取颜色信息的函数
def extract_colors(color_div):
    colors = []
    if not color_div:
        return colors
    
    color_elements = color_div.find_all("div", class_="li-div-color-a")
    for color_element in color_elements:
        color_name = color_element.get("title", "")
        color_code = color_element.get("style", "").split("background-color: ")[1].split(";")[0]
        if color_name and color_code:
            colors.append({"name": color_name, "code": color_code})
    
    return colors

# 提取所有Apple Watch数据
def extract_watch_data():
    all_watches = []
    
    for html_file in html_files:
        print(f"处理文件: {html_file}")
        
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        soup = BeautifulSoup(content, 'html.parser')
        
        # 获取产品列表
        product_columns = soup.select('.cd-products-columns .product')
        
        # 获取参数名列表
        param_names = [li.get_text().strip() for li in soup.select('.cd-features-list.ul-ext-right li')]
        
        for product in product_columns:
            watch_data = {}
            
            # 提取产品名称
            name_element = product.select_one('.top-info h3')
            if name_element:
                watch_name = name_element.get_text().strip()
                watch_data["name"] = watch_name
                
                # 生成唯一ID
                watch_id = "watch-" + re.sub(r'[^a-zA-Z0-9]', '-', watch_name.lower())
                watch_data["id"] = watch_id
            
            # 提取参数值
            param_values = [li for li in product.select('ul.cd-features-list li')]
            
            for i, param_name in enumerate(param_names):
                if i < len(param_values):
                    param_value = param_values[i]
                    
                    # 处理颜色信息
                    if param_name == "外观颜色":
                        color_div = param_value.select_one('.li-div-color')
                        if color_div:
                            watch_data["colors"] = extract_colors(color_div)
                        continue
                    
                    # 处理RAM和ROM
                    if param_name == "RAM\nROM":
                        ram_rom_div = param_value.select_one('.li-div-npu')
                        if ram_rom_div:
                            text = ram_rom_div.get_text().strip()
                            ram_match = re.search(r'(\d+)GB', text)
                            rom_match = re.search(r'(\d+)GB', text[text.find('\n'):] if '\n' in text else "")
                            
                            if ram_match:
                                watch_data["ram"] = f"{ram_match.group(1)}GB"
                            if rom_match:
                                watch_data["storage"] = f"{rom_match.group(1)}GB"
                        continue
                    
                    # 处理屏幕参数
                    if param_name == "屏幕参数":
                        display_divs = param_value.select('.li-div-cpu')
                        if display_divs:
                            resolutions = []
                            for div in display_divs:
                                text = div.get_text().strip()
                                resolution = text.split('(')[0].strip()
                                size = text.split('(')[1].split(')')[0].strip() if '(' in text else ""
                                resolutions.append(f"{resolution} ({size})")
                            watch_data["displayResolution"] = ", ".join(resolutions)
                        continue
                    
                    # 处理其他参数
                    if param_name in param_mapping:
                        key = param_mapping[param_name]
                        value = param_value.get_text().strip()
                        if value and value != "—":
                            watch_data[key] = value
            
            if watch_data:
                all_watches.append(watch_data)
    
    return all_watches

# 主函数
def main():
    print("开始提取Apple Watch数据...")
    watches = extract_watch_data()
    
    # 按发布日期排序（降序）
    watches.sort(key=lambda x: x.get("releaseDate", ""), reverse=True)
    
    print(f"成功提取 {len(watches)} 个Apple Watch型号的数据")
    
    # 保存为JSON文件
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(watches, f, ensure_ascii=False, indent=2)
    
    print(f"数据已保存到: {output_file}")

if __name__ == "__main__":
    main()
